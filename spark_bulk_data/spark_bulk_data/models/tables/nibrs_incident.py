from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="AGENCY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="INCIDENT_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="NIBRS_MONTH_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="CARGO_THEFT_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="SUBMISSION_DATE", sql_type=SQLConfig.Types.DATE),
        TableField(name="INCIDENT_DATE", sql_type=SQLConfig.Types.DATE),
        TableField(name="REPORT_DATE_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="INCIDENT_HOUR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="CLEARED_EXCEPT_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="CLEARED_EXCEPT_DATE", sql_type=SQLConfig.Types.DATE),
        TableField(name="INCIDENT_STATUS", sql_type=SQLConfig.Types.STRING),
        TableField(name="DATA_HOME", sql_type=SQLConfig.Types.STRING),
        TableField(name="ORIG_FORMAT", sql_type=SQLConfig.Types.STRING),
        TableField(name="DID", sql_type=SQLConfig.Types.INTEGER),
    ]
