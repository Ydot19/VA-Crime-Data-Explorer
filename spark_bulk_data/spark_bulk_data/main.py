import spark_bulk_data.utils.relationship as rs
import spark_bulk_data.utils.spark_data_reader as dr
import spark_bulk_data.utils.data_prep as dp
import spark_bulk_data.cockroach.main as cdb
import spark_bulk_data.cockroach.client as cdb_connection
import spark_bulk_data.utils.spark_client as sc
import os
import shutil

from spark_bulk_data.config import BaseConfig


def prepare_folder():
    """
    Creates the folder if it does not exist
    There is a raw folder where partitioned data will be held from pyspark dataframes
    There is a cumulative folder that holds all the gzip files as one file to be upload to the db
    :return:
    """
    temp_dir = f"{BaseConfig.PROJECT_DIR}/temp"
    if os.path.isdir(temp_dir):
        shutil.rmtree(temp_dir)

    temp_dir_sub_folders = [f"{temp_dir}/raw", f"{temp_dir}/cumulative"]

    for sub in temp_dir_sub_folders:
        os.makedirs(name=sub)

    return {"raw": temp_dir_sub_folders[0], "cumulative": temp_dir_sub_folders[1]}


def execute():
    """
    Executes the generation of the data frames to spark
    - Get the clients
    - Get the relationships
    - Conglomerate the data
    - Validate the headers
    - Drop any unnecessary columns
    - Upload to Cockroach
    :return:
    """
    temp_folders = prepare_folder()
    spark_session = sc.get_spark_client()
    cockroach_connection = cdb_connection.get_db_client()
    cockroach_client = cdb.CockRoachDBInteractions(cockroach_connection)
    data_reader = dr.VaCrimeDataReader(
        spark=spark_session, data_folder_path=BaseConfig.DATA_DIR
    )

    relations = rs.get_relationship()
    filenames = ["agencies.csv", "NIBRS_ACTIVITY_TYPE.csv"]
    filename = "NIBRS_ARRESTEE.csv"
    cdb_table = filename[: filename.index(".csv")].lower()

    agency = relations[filename]
    relation_headers = [tf.name for tf in agency]
    _ = data_reader.set_data(filename, True)
    spark_session = data_reader.get_spark_session()

    # spark_session.sql()
    df = spark_session.table("DfTemp")
    if not dp.verify_data(df.columns, relation_headers):
        to_drop = list(set(df.columns) - set(relation_headers))
        df_trimmed = data_reader.remove_columns(df, to_drop)
        df = df_trimmed

    gzip_file_paths = dp.create_gzip_from_spark_df(
        spark_df=df, table_name=cdb_table, folders=temp_folders
    )
    cockroach_client.push_df_to_db(
        spark_df=df,
        cdb_table=cdb_table,
        column_mapping=agency,
        file_paths=gzip_file_paths,
    )


if __name__ == "__main__":
    execute()
