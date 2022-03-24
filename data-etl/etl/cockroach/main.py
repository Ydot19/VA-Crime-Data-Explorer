import string

import pyspark.sql
from config import BaseConfig
from etl.models.TableFieldDataClass import TableField


class CockRoachDBInteractions:
    """
    Used to complete the cockroach db transactions from apache spark
    """

    def __init__(self, conn):
        """
        Set up the DB connection
        :param conn:
        """
        self.__conn = conn

    @staticmethod
    def drop_table_statement(table_name: str):
        """
        Creates a drop table statement
        :param table_name:
        :return:
        """
        return f"""DROP TABLE IF EXISTS {table_name}"""

    @staticmethod
    def create_table_statement(table_name: str, column_mapping: list[TableField]):
        """
        Generates the table and the associated columns by type and sets the relevant primary keys
        :param table_name:
        :param column_mapping:
        :return:
        """
        fields = ""
        primary = []
        for tf in column_mapping:
            end = ","
            if tf.is_primary:
                end = " NOT NULL,"
                primary.append(tf.name)
            column_mapping = f'\n"{tf.name.lower()}" {tf.sql_type}{end}'
            fields += column_mapping
        generated_create_table_sql_statement = f"""CREATE TABLE IF NOT EXISTS {table_name}({fields}
        PRIMARY KEY ({','.join(primary)})
        );"""
        return generated_create_table_sql_statement

    @staticmethod
    def bulk_import_statement(table_name: str, gzip_file_paths: list[str]):
        """
        Bulk import data from gzip compressed file
        :param table_name:
        :param gzip_file_paths: path on local node
        :return:
        """
        file_paths = ",\n".join(gzip_file_paths)
        generated_bulk_import_sql_statement = f"""SET DATABASE = '{BaseConfig.COCKROACH_DATABASE}';
        IMPORT INTO {table_name}
        CSV DATA({file_paths})
        WITH 
        detached,
        decompress='gzip',
        skip='1';"""

        split_statement = generated_bulk_import_sql_statement.splitlines(True)
        breakpoint()
        generated_bulk_import_sql_statement = "".join(
            list(map(lambda l: l.lstrip(), split_statement))
        )
        generated_bulk_import_sql_statement = (
            generated_bulk_import_sql_statement.replace("detached", "\tdetached")
            .replace("decompress", "\tdecompress")
            .replace("skip", "\tskip")
        )
        breakpoint()
        return generated_bulk_import_sql_statement

    @staticmethod
    def copy_gzip_files_to_node_dir(gzip_file_paths: list[str]) -> [str]:
        """
        Copies gzip file to local node directory
        :param gzip_file_paths:
        :return:
        """
        from subprocess import run, PIPE

        node_local_paths = []
        for filepath in gzip_file_paths:
            filename = filepath.split("/")[len(filepath.split("/")) - 1]
            command_statement = (
                f"cockroach nodelocal upload {filepath} {filename} "
                f"--host=localhost:{BaseConfig.COCKROACH_PORT} -u=root "
                f"--certs-dir={BaseConfig.COCKROACH_SSL_CERT.rsplit('/', 1)[0]}"
            )
            res = run(command_statement.split(), stderr=PIPE, stdout=PIPE)
            # TODO: handle error when return code is non-zero
            res.check_returncode()
            stdout_statement = str(res.stdout, "utf-8")
            node_local_path = stdout_statement.split("uploaded to ")[1].strip()
            node_local_paths.append(node_local_path)

        return node_local_paths

    def push_df_to_db(
        self,
        spark_df: pyspark.sql.DataFrame,
        cdb_table: str,
        column_mapping: list[TableField],
        file_paths: str or None,
    ):
        """
        Saves the spark dataframe to persistent storage unit
        :param spark_df: Current Spark Session object
        :param cdb_table: cockroach db table name
        :param column_mapping: mapping based on models/tables directory
        :param file_paths: gzipped csv file paths if they were created otherwise this returns None
        :return: None
        """

        sql_statement = self.create_table_statement(cdb_table, column_mapping)
        self._execute_sql(sql_statement)

        # Preparing the jdbc connection
        # see: https://www.cockroachlabs.com/docs/stable/build-a-spring-app-with-cockroachdb-jdbc.html for more info
        jdbc_url = (
            f"jdbc:postgresql://{BaseConfig.COCKROACH_HOST}:{BaseConfig.COCKROACH_PORT}/"
            f"{BaseConfig.COCKROACH_DATABASE}?sslmode=verify-full&"
            f"sslrootcert={BaseConfig.COCKROACH_SSL_ROOT_CERT}"
        )

        table_name = f"public.{cdb_table}"

        properties = {
            "user": BaseConfig.COCKROACH_USER,
            "password": BaseConfig.COCKROACH_PASSWORD,
            "driver": "org.postgresql.Driver",
        }

        spark_df = spark_df.dropDuplicates()
        breakpoint()
        # Dynamically Partition the data to be sent to
        print(
            f"\n\nStatus: Started\nName of Data: {cdb_table}\nCockroach DB URL: {jdbc_url}\nDB Table: {table_name}"
        )
        self._upload_executor(
            spark_df=spark_df,
            cdb_table=cdb_table,
            jdbc_url=jdbc_url,
            properties=properties,
            file_paths=file_paths,
        )
        print(
            f"\n\nStatus: Completed\nName of Data: {cdb_table}\nCockroach DB URL: {jdbc_url}\nDB Table: {table_name}"
        )

    def _upload_executor(
        self,
        spark_df: pyspark.sql.DataFrame,
        cdb_table: str,
        jdbc_url: str,
        properties: dict,
        file_paths: str or None,
    ):
        """
        Either uploads the dataframes directory or creates a gzip compressed file and uploads to
        cockroach db
        :param spark_df: spark dataframe
        :param cdb_table: cockroach db table name
        :param: jdbc_url: url with parameters to the cockroachdb
        :param file_paths: gzipped csv filepath if one was created otherwise this returns None
        :return:
        """
        if file_paths is None:
            table_name = f"public.{cdb_table}"
            spark_df.write.option("batchsize", "2000").option(
                "numPartitions", "10"
            ).jdbc(url=jdbc_url, table=table_name, mode="append", properties=properties)
        else:
            gzip_file_paths = self.copy_gzip_files_to_node_dir(
                gzip_file_paths=file_paths
            )
            sql_statement = self.bulk_import_statement(
                table_name=cdb_table, gzip_file_paths=gzip_file_paths
            )
            self._execute_sql(sql_statement=sql_statement)

    def _execute_sql(self, sql_statement: str):
        """
        Private method that creates that creates the table if does not exist in the database
        :param sql_statement: statement to execut on the cluster
        :return:
        """
        with self.__conn.cursor() as cur:
            cur.execute(sql_statement)

        self.__conn.commit()
