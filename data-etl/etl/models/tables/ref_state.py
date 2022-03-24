from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="STATE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField(name="DIVISION_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="STATE_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="STATE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="STATE_ABBR", sql_type=SQLConfig.Types.STRING),
        TableField(name="STATE_POSTAL_ABBR", sql_type=SQLConfig.Types.STRING),
        TableField(name="STATE_FIPS_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="STATE_PUB_FREQ_MONTHS", sql_type=SQLConfig.Types.STRING),
        TableField(name="CHANGE_USER", sql_type=SQLConfig.Types.STRING),
    ]
