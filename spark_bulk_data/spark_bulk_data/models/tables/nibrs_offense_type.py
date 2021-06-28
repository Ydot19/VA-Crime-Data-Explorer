from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="OFFENSE_TYPE_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True
        ),
        TableField(name="OFFENSE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="OFFENSE_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="CRIME_AGAINST", sql_type=SQLConfig.Types.STRING),
        TableField(name="CT_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="HC_FLAG", sql_type=SQLConfig.Types.STRING),
        TableField(name="HC_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="OFFENSE_CATEGORY_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="OFFENSE_GROUP", sql_type=SQLConfig.Types.STRING),
    ]
