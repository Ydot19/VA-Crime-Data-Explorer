from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="CLEARED_EXCEPT_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="CLEARED_EXCEPT_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="CLEARED_EXCEPT_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="CLEARED_EXCEPT_DESC", sql_type=SQLConfig.Types.STRING),
    ]
