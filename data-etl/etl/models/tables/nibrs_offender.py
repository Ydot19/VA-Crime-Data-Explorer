from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="OFFENDER_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="INCIDENT_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="OFFENDER_SEQ_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="AGE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="AGE_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="SEX_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="RACE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="ETHNICITY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="AGE_RANGE_LOW_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="AGE_RANGE_HIGH_NUM", sql_type=SQLConfig.Types.INTEGER),
    ]
