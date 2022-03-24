from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="CIRCUMSTANCES_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="CIRCUMSTANCES_TYPE", sql_type=SQLConfig.Types.STRING),
        TableField(name="CIRCUMSTANCES_CODE", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="CIRCUMSTANCES_NAME", sql_type=SQLConfig.Types.STRING),
    ]
