from unittest import TestCase
from unittest import mock
from spark_bulk_data.utils import spark_runner as runner


class TestSparkRunner(TestCase):
    @staticmethod
    def runner_method(spark):
        """
        static runner to use
        :param spark: Spark Session or Context Object
        :return:
        """
        return None

    @mock.patch("pyspark.sql.SparkSession.builder.getOrCreate")
    def test_session_runner(self, mocked: mock.MagicMock):
        # Arrange
        options = dict({"build_config": dict({"master": "local"})})
        # Act
        runner.spark_session_runner(
            runner=self.runner_method, app_name="TestSessionRunner", **options
        )
        # Assert
        mocked.assert_called_once()
