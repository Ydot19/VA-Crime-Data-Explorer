from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="ETHNICITY_ID", sql_type=SQLConfig.Types.STRING),
        TableField(name="ETHNICITY_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="ETHNICITY_NAME", sql_type=SQLConfig.Types.STRING),
    ]
