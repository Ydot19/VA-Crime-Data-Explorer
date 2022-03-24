from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField("DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField("ARRESTEE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField("INCIDENT_ID", sql_type=SQLConfig.Types.STRING, is_primary=True),
        TableField("ARRESTEE_SEQ_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField("ARREST_DATE", sql_type=SQLConfig.Types.STRING),
        TableField("ARREST_TYPE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField("MULTIPLE_INDICATOR", sql_type=SQLConfig.Types.STRING),
        TableField("OFFENSE_TYPE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField("AGE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField("AGE_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField("SEX_CODE", sql_type=SQLConfig.Types.STRING),
        TableField("RACE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField("ETHNICITY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField("RESIDENT_CODE", sql_type=SQLConfig.Types.STRING),
        TableField("UNDER_18_DISPOSITION_CODE", sql_type=SQLConfig.Types.STRING),
        TableField("CLEARANCE_IND", sql_type=SQLConfig.Types.STRING),
        TableField("AGE_RANGE_LOW_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField("AGE_RANGE_HIGH_NUM", sql_type=SQLConfig.Types.INTEGER),
    ]
