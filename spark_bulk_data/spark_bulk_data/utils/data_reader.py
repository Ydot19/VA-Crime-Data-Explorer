import zipfile
from pyspark.sql import SparkSession, DataFrame, Row
from spark_bulk_data.utils.spark_runner import spark_session_runner


def read_zip_folder(spark: SparkSession, zip_path: str, file_in_zip: str) -> DataFrame:
    """
    Reads the csv file in a zip file and returns the data frame
    :param spark: Spark session object
    :param zip_path: Data Folder
    :param file_in_zip: File to read
    :return:
    """
    zip_files = zipfile.ZipFile(file=zip_path, mode="r")
    csv_list = zip_files.read(name=file_in_zip).decode(encoding="utf-8").split("\n")
    csv_tuples = [
        tuple(part for part in x.split(",") if part) for x in csv_list[1:][:-1]
    ]
    # use first row as column headers
    all_headers: str = csv_list[0]
    headers_split: tuple[str] = tuple(
        header for header in all_headers.split(",") if header
    )
    columns = Row(*headers_split)
    # Spread tuple to arguments
    ret: DataFrame = spark.createDataFrame([columns(*x) for x in csv_tuples])

    return ret


if __name__ == "__main__":
    options = dict(
        {
            "zip_path": "spark_bulk_data/data/VA-2000.zip",
            "file_in_zip": "nibrs_bias_motivation.csv",
        }
    )
    data: DataFrame = spark_session_runner(
        runner=read_zip_folder, app_name="TestReadCSVZip", **options
    )
    # read_zip_folder(zip_path=file, file_in_zip=name)
