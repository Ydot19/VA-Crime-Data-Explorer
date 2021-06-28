from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="SUSPECT_USING_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="SUSPECT_USING_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="SUSPECT_USING_NAME", sql_type=SQLConfig.Types.STRING),
    ]
