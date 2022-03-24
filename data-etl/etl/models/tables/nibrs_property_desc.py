from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="PROPERTY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="PROP_DESC_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="PROPERTY_VALUE", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="DATE_RECOVERED", sql_type=SQLConfig.Types.DATE),
        TableField(
            name="NIBRS_PROP_DESC_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
    ]
