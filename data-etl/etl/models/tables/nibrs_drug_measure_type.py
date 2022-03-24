from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(
            name="DRUG_MEASURE_TYPE_ID",
            sql_type=SQLConfig.Types.INTEGER,
            is_primary=True,
        ),
        TableField(name="DRUG_MEASURE_CODE", sql_type=SQLConfig.Types.STRING),
        TableField(name="DRUG_MEASURE_NAME", sql_type=SQLConfig.Types.STRING),
    ]
