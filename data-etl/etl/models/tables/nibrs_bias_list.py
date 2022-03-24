from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="BIAS_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField(name="BIAS_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="BIAS_CATEGORY", sql_type=SQLConfig.Types.STRING),
        TableField(name="BIAS_DESC", sql_type=SQLConfig.Types.STRING),
    ]
