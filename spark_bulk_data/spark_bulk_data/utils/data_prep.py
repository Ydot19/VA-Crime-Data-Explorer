"""
Cleansing the data from the csv and preparing for db upload
"""
from pyspark.sql import DataFrame, SparkSession


def verify_data(df_columns: list[str], table_columns: list[str]):
    assert sorted(df_columns) == sorted(table_columns)


if __name__ == "__main__":
    from spark_bulk_data.utils.data_reader import VaCrimeDataReader
    from spark_bulk_data.config import BaseConfig
    from spark_bulk_data.utils import relationship

    options = dict({"build_config": dict({"master": "local"})})
    spark_session = (
        SparkSession.builder.master(
            f"{options.get('build_config', {}).get('master', 'local')}"
        )
        .config("spark.driver.bindAddress", "127.0.0.1")
        .appName("DEBUG")
        .getOrCreate()
    )
    name = "NIBRS_VICTIM_CIRCUMSTANCES.csv"
    dreader = VaCrimeDataReader(spark_session, BaseConfig.DATA_DIR)
    dframe: DataFrame = dreader.get_data(name, True)
    relationships = relationship.get_relationship()
    tb_columns = [col.name for col in relationships.get(name)]
    if "DATA_YEAR" not in tb_columns:
        dframe = dreader.remove_columns(dframe, ["DATA_YEAR"])

    verify_data(dframe.columns, tb_columns)
