from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="PROP_DESC_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="PROP_DESC_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="PROP_DESC_NAME", sql_type=SQLConfig.Types.STRING),
    ]
