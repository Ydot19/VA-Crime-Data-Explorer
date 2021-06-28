from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="OFFENSE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="INCIDENT_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="OFFENSE_TYPE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="ATTEMPT_COMPLETE_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="LOCATION_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="NUM_PREMISES_ENTERED", sql_type=SQLConfig.Types.STRING),
        TableField(name="METHOD_ENTRY_CODE", sql_type=SQLConfig.Types.STRING),
    ]
