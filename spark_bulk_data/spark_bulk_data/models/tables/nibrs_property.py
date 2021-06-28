from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="PROPERTY_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="INCIDENT_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="PROP_LOSS_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="STOLEN_COUNT", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="RECOVERED_COUNT", sql_type=SQLConfig.Types.INTEGER),
    ]
