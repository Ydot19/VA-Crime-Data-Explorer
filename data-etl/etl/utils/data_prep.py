"""
Cleansing the data from the csv and preparing for db upload
"""
import os
import shutil

import pyspark.sql


def verify_data(df_columns: list[str], table_columns: list[str]):
    """
    Verifies that the data frame contains only the relevant columns
    :param df_columns: pyspark dataframe columns
    :param table_columns: table columns from spark_bulk_data/models/tables directory
    :return:
    """

    return sorted(df_columns) == sorted(table_columns)


def columns_to_drop(df_columns: list[str], table_columns: list[str]):
    """
    Get the elements in one table_columns but not in df_columns
    :param df_columns:
    :param table_columns:
    :return:
    """
    return list(set(df_columns) - set(table_columns))


def create_gzip_from_spark_df(
    spark_df: pyspark.sql.DataFrame, table_name: str, folders: dict
) -> list[str] or None:
    """
    Creates a compressed gzip if there are more than 50k records
    :param spark_df:
    :param table_name:
    :param folders: raw data folder and cumulative data folder
    :return:
    """

    records = spark_df.count()
    if records > 50_000:
        folder_path = f"{folders['raw']}/{table_name}"
        spark_df.write.csv(
            path=folder_path, header=True, compression="gzip", mode="overwrite"
        )
        spark_written_files = os.listdir(folder_path)
        upload_able_files = list(
            filter(
                lambda f: ".crc" not in f and "_SUCCESS" not in f, spark_written_files
            )
        )
        gzipped_file_paths = [
            f"{folders['cumulative']}/{table_name}_{index}.csv.gz"
            for _, index in enumerate(upload_able_files)
        ]

        # cumulative_gzip = f"{folders['cumulative']}/{table_name}_cumulative.csv.gz"
        # with open(cumulative_gzip, "wb") as fwb:
        #     for filename in os.listdir(folder_path):
        #         if "csv.gz.crc" not in filename:
        #             with open(f"{folder_path}/{filename}", "rb") as frb:
        #                 shutil.copyfileobj(frb, fwb)

        return gzipped_file_paths

    return None
