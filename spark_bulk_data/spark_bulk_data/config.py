import os


class BaseConfig:
    ## Dataset info
    DATA_START_YEAR = os.getenv("START_YEAR")
    DATA_END_YEAR = os.getenv("END_YEAR")
    DATA_DIR = os.getenv("DATA_DIR")
    DATA_TEMP_DIR = "/temp"

    ## Below: CONFIGURATION FOR DATABASE CONNECTION
    COCKROACH_CLUSTER = os.getenv("CLUSTER")
    COCKROACH_DATABASE = os.getenv("DATABASE")
    COCKROACH_HOST = os.getenv("HOST")
    COCKROACH_PORT = os.getenv("PORT")
    COCKROACH_USER = os.getenv("USER")
    COCKROACH_PASSWORD = os.getenv("PASSWORD")
    COCKROACH_SSL_ROOT_CERT = os.getenv("SSL_ROOT_CERT")
    COCKROACH_SSL_KEY = os.getenv("SSL_KEY")
    COCKROACH_SSL_CERT = os.getenv("SSL_CERT")

    ## Configuration for PySpark JDBC
    JDBC_JAR = os.getenv("JDBC_JAR")


class SQLConfig:
    class Types:
        INTEGER = "INTEGER"
        STRING = "STRING"
        DATE = "DATE"
