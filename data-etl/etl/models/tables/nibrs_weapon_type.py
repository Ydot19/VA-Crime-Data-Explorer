from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="WEAPON_ID", sql_type=SQLConfig.Types.INTEGER, is_primary=True),
        TableField(name="WEAPON_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="WEAPON_NAME", sql_type=SQLConfig.Types.STRING),
        TableField(name="SHR_FLAG", sql_type=SQLConfig.Types.STRING),
    ]
