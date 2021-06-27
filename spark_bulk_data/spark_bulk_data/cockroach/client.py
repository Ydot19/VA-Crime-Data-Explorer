import psycopg2
from spark_bulk_data.config import BaseConfig


def get_db_client():
    """
    returns the db client
    :return:
    """
    return psycopg2.connect(
        database=BaseConfig.COCKROACH_DATABASE,
        user=BaseConfig.COCKROACH_USER,
        sslmode="verify-full",
        sslrootcert=BaseConfig.COCKROACH_SSL_ROOT_CERT,
        sslkey=BaseConfig.COCKROACH_SSL_KEY,
        sslcert=BaseConfig.COCKROACH_SSL_CERT,
        port=BaseConfig.COCKROACH_PORT,
        host=BaseConfig.COCKROACH_HOST,
    )
