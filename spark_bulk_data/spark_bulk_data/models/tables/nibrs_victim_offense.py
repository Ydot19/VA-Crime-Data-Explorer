from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="VICTIM_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="OFFENSE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
    ]
