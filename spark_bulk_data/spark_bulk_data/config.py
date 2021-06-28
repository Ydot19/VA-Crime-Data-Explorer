import os


class BaseConfig:
    DATA_FOLDER_BASE_PATH = os.getenv("DATA_FOLDER_BASE_PATH")
    ## BELOW: CONFIGURATION FOR DATABASE CONNECTION
    COCKROACH_DATABASE = os.getenv("DATABASE")
    COCKROACH_HOST = os.getenv("HOST")
    COCKROACH_PORT = os.getenv("PORT")
    COCKROACH_USER = os.getenv("USER")
    COCKROACH_PASSWORD = os.getenv("PASSWORD")
    COCKROACH_SSL_ROOT_CERT = os.getenv("SSL_ROOT_CERT")
    COCKROACH_SSL_KEY = os.getenv("SSL_KEY")
    COCKROACH_SSL_CERT = os.getenv("SSL_CERT")


class SQLConfig:
    class Types:
        INTEGER = "INTEGER"
        STRING = "STRING"
        DATE = "DATE"
