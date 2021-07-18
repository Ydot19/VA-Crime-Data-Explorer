from pyspark.sql.session import SparkSession

from config import BaseConfig
from spark_bulk_data.cockroach import client
from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.models.tables import agencies as ag


class CockRoachDBInteractions:
    def __init__(self, conn):
        """
        Set up the DB connection
        :param conn:
        """
        self.__conn = conn

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

    def bulk_insert(
        self, spark: SparkSession, cbd_table: str, column_mapping: list[TableField]
    ):
        """
        Saves the spark dataframe to persistent storage unit
        :param spark: Current Spark Session object
        :param cbd_table: cockroach db table name
        :param column_mapping: mapping based on models/tables directory
        :return: None
        """

        self._create_table(cbd_table, column_mapping=column_mapping)

        # Preparing the jdbc connection

        # see: https://www.cockroachlabs.com/docs/stable/build-a-spring-app-with-cockroachdb-jdbc.html for more info
        jdbc_url = (
            f"jdbc:postgresql://{BaseConfig.COCKROACH_HOST}:{BaseConfig.COCKROACH_PORT}/"
            f"{BaseConfig.COCKROACH_CLUSTER}.roach_data?sslmode=verify-full&sslrootcert={BaseConfig.COCKROACH_SSL_ROOT_CERT}"
        )
        df = spark.table("DfTemp")
        df.write.format("jdbc").option("url", jdbc_url).option(
            "dbtable", f"schema.{cbd_table}"
        ).option("user", BaseConfig.COCKROACH_USER).option(
            "password", BaseConfig.COCKROACH_PASSWORD
        ).save()

    def _create_table(self, table_name: str, column_mapping: list[TableField]):
        """
        Private method that creates that creates the table if does not exist in the database
        :param table_name:
        :param column_mapping:
        :return:
        """
        sql_statement = self.create_table_statement(
            table_name=table_name, column_mapping=column_mapping
        )
        with self.__conn.cursor() as cur:
            cur.execute(sql_statement)

        self.__conn.commit()
