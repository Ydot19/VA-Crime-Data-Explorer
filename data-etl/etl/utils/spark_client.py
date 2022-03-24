from pyspark.sql import SparkSession
from config import BaseConfig


def get_spark_client() -> SparkSession:
    """
    Gets the spark session object
    :return:
    """
    return (
        SparkSession.builder.master("local[*]")
        .appName("NIBRS Crime Spark Session")
        .config("spark.jars", BaseConfig.JDBC_JAR)
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.driver.memory", "15g")
        .config("spark.ui.port", "8443")
        .config("spark.sql.debug.maxToStringFields", "100")
        .getOrCreate()
    )
