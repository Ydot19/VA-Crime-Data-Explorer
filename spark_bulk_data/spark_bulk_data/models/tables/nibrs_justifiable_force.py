from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="JUSTIFIABLE_FORCE_ID", sql_type=SQLConfig.Types.STRING),
        TableField(name="JUSTIFIABLE_FORCE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="JUSTIFIABLE_FORCE_NAME", sql_type=SQLConfig.Types.STRING),
    ]
