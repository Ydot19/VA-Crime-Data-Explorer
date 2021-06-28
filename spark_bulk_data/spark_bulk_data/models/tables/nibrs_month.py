from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="NIBRS_MONTH_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="AGENCY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="MONTH_NUM", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="REPORTED_STATUS", sql_type=SQLConfig.Types.STRING),
        TableField(name="REPORT_DATE", sql_type=SQLConfig.Types.STRING),
        TableField(name="UPDATE_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="ORIG_FORMAT", sql_type=SQLConfig.Types.STRING),
        TableField(name="DATA_HOME", sql_type=SQLConfig.Types.STRING),
        TableField(name="DDOCNAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="DID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="MONTH_PUB_STATUS", sql_type=SQLConfig.Types.INTEGER),
    ]
