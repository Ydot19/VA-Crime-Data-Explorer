from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="ARREST_TYPE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="ARREST_TYPE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="ARREST_TYPE_NAME", sql_type=SQLConfig.Types.STRING),
    ]
