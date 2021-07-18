from zipfile import ZipFile

from pyspark.sql import SparkSession, DataFrame
from spark_bulk_data.config import BaseConfig

import pandas as pd
import io


class VaCrimeDataReader:
    def __init__(self, spark: SparkSession, data_folder_path: str):
        """
        Reads data set by year
        Data is in zip files with following naming convention
        VA-{year}.zip
        :param year:
        """

        self.__start_year: int = int(BaseConfig.DATA_START_YEAR)
        self.__end_year: int = int(BaseConfig.DATA_END_YEAR)
        self.year = self.__end_year
        self.__folder_path: str = data_folder_path
        self.__spark_session: SparkSession = spark
        self.__zip = ZipFile(f"{self.__folder_path}/VA-{self.year}.zip")
        self.__pandas_df: pd.DataFrame or None = None

    def get_spark_session(self):
        """
        Return spark session
        Loaded with the Global Temp Table needed to import to cockroachdb
        :return:
        """
        return self.__spark_session

    def set_year(self, year: int):
        """
        Set the year to investigate the data against
        :param year:
        :return:
        """
        self.year = year
        self.__zip = ZipFile(f"{self.__folder_path}/VA-{self.year}.zip")
        return self

    def set_data(self, csv_filename, get_for_range_of_years: bool = False):
        """
        Returns the csv data as a dataframe
        csv file must

        If get_for_range_of_years set to true, this method will retrieve a summarized data across all the years
        :param get_for_range_of_years:
        :param csv_filename:
        :return:
        """

        if get_for_range_of_years:
            all_data = self.__all_data(csv_filename)
            return self.__spark_session.createDataFrame(all_data)

        csv_filename = self.get_file_name(csv_filename)
        if csv_filename is None:
            return None

        self.__fetch_csv_content(csv_filename)
        self.__spark_session.conf.set("spark.sql.execution.arrow.enabled", "true")
        self.__spark_session.createDataFrame(self.__pandas_df).createOrReplaceTempView(
            "DfTemp"
        )

    def print_zip_file_names(self):
        print(self.__zip.namelist())

    def get_file_name(self, base_csv_filename: str):
        """
        Searches for the file by name and tries to find it regardless of directory
        or case sensitivity
        :param base_csv_filename:
        :return:
        """
        files_in_zip = self.__zip.namelist()
        lowered_base_csv_filename = base_csv_filename.lower()
        for file in files_in_zip:
            lowered_file_name = file.lower()
            if lowered_base_csv_filename in lowered_file_name:
                return file

        return None

    def __fetch_csv_content(self, csv_filename: str):
        # fiz = file in zipfile
        with self.__zip.open(csv_filename) as fiz:
            raw_string = fiz.read().decode("UTF-8")
            self.__pandas_df = pd.read_csv(io.StringIO(raw_string), sep=",")
            self.__pandas_df.columns = self.__pandas_df.columns.str.upper()
            if "DATA_YEAR" not in self.__pandas_df.columns:
                self.__pandas_df["DATA_YEAR"] = self.year
            self.__pandas_df = self.__pandas_df.astype(str)

    def __all_data(self, csv_filename) -> pd.DataFrame:
        """
        Returns all available data between the designated start date and end date
        :return:
        """
        df_all: pd.DataFrame or None = None

        for year in range(self.__start_year, self.__end_year + 1):
            self.set_year(year)
            csv_filename = self.get_file_name(csv_filename)
            if csv_filename is None:
                continue
            self.__fetch_csv_content(csv_filename)
            if df_all is None:
                df_all = self.__pandas_df.copy()
            else:
                df_all = df_all.append(self.__pandas_df.copy())

        return df_all

    @staticmethod
    def remove_columns(df: DataFrame, columns_to_drop: list[str]) -> DataFrame:
        """
        Remove unnecessary columns from a spark data frame
        """
        df.drop(*columns_to_drop)
        return df
