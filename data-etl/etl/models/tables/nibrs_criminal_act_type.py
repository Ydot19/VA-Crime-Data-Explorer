from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="CRIMINAL_ACT_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="CRIMINAL_ACT_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="CRIMINAL_ACT_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="CRIMINAL_ACT_DESC", sql_type=SQLConfig.Types.STRING),
    ]
