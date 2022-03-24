from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="AGE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField(name="AGE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="AGE_NAME", sql_type=SQLConfig.Types.STRING),
    ]
