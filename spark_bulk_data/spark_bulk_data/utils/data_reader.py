from pyspark.sql import SparkSession, DataFrame
from zipfile import ZipFile


class VaCrimeDataReader:
    def __init__(self, spark: SparkSession, year: int, data_folder_path: str):
        """
        Reads data set by year
        Data is in zip files with following naming convention
        VA-{year}.zip
        :param year:
        """
        if year < 2000 or year > 2019:
            raise ValueError("Year should be between 2000 and 2019")

        self.year: int = year
        self.__folder_path: str = data_folder_path
        self.__spark_session: SparkSession = spark
        self.__zip = ZipFile(f"{self.__folder_path}/VA-{self.year}.zip")

    def set_year(self, year: int):
        """
        Set the year to investigate the data against
        :param year:
        :return:
        """
        self.year = year
        return self

    def get_data(self, csv_filename) -> DataFrame or None:
        """
        Returns the csv data as a dataframe
        csv file must
        :param csv_filename:
        :return:
        """
        csv_filename = f"VA/{csv_filename}"
        csv_file_content = self.__fetch_csv_content(csv_filename)
        header = self.__get_header(csv_file_content)
        data = self.__get_data(csv_file_content)
        rdd = self.__spark_session.sparkContext.parallelize(data)
        return self.__spark_session.createDataFrame(rdd, header)

    def print_zip_file_names(self):
        print(self.__zip.namelist())

    def __fetch_csv_content(self, csv_filename: str):
        # fiz = file in zipfile
        with self.__zip.open(csv_filename) as fiz:
            raw_string = fiz.read().decode("UTF-8")

        return self.__cleanse_csv_raw_string(raw_string=raw_string)

    @staticmethod
    def __cleanse_csv_raw_string(raw_string: str):
        reformatted = raw_string.replace('"', "").split("\r\n")
        return list(map(lambda row: row.split(","), reformatted))

    @staticmethod
    def __get_header(csv_content: list[list[str]]):
        return csv_content[0]

    @staticmethod
    def __get_data(csv_content: list[list[str]]):
        # remove empty rows
        csv_content_no_empty_rows = list(
            filter(lambda row: not (len(row) == 1 and "" in row), csv_content)
        )
        return list(map(lambda x: tuple(x), csv_content_no_empty_rows[1:]))

    @staticmethod
    def remove_columns(df: DataFrame, columns_to_drop: list[str]) -> DataFrame:
        """
        Remove unnecessary columns from dataframe
        :param df: Dataframe about
        :param columns_to_drop: list of column, by name, to drop
        :return: Dataframe with the updated columns
        """
        return df.drop(*columns_to_drop)
