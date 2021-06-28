from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="RACE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField(name="RACE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="RACE_DESC", sql_type=SQLConfig.Types.STRING),
        TableField(name="SORT_ORDER", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="START_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="END_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="NOTES", sql_type=SQLConfig.Types.STRING),
    ]
