from unittest import TestCase, mock
from pyspark.sql import SparkSession, DataFrame
from spark_bulk_data.utils.data_reader import read_zip_folder
import zipfile
import os


class TestReadingZipFolders(TestCase):
    spark: SparkSession = None
    temp_zip: str = "tests/unit/data_reader.zip"
    sample_data_file = "tests/unit/data/sample_csv_data.csv"

    @classmethod
    def create_spark_session(cls) -> SparkSession:
        return (
            SparkSession.builder.master("local")
            .config("spark.driver.bindAddress", "127.0.0.1")
            .appName("ReadZipFile")
            .getOrCreate()
        )

    @classmethod
    def create_temp_directory(cls):
        zipfile.ZipFile(
            file=cls.temp_zip, mode="w", compression=zipfile.ZIP_DEFLATED
        ).write(cls.sample_data_file)

    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = cls.create_spark_session()
        cls.create_temp_directory()

    def test_read_zip_folder(self):
        # Arrange
        # Act
        df: DataFrame = read_zip_folder(
            spark=self.spark, zip_path=self.temp_zip, file_in_zip=self.sample_data_file
        )

        # Assert
        expected_columns = ["Date", "SP500", "Real Earnings", "Long Interest Rate"]
        assert all(column in df.columns for column in expected_columns)
        assert df.count() > 0

    @classmethod
    def tearDownClass(cls) -> None:
        cls.spark.stop()
        os.remove(path=cls.temp_zip)
