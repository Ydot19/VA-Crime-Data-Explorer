from spark_bulk_data.models.TableFieldDataClass import TableField
from spark_bulk_data.config import SQLConfig


def get_headers() -> list[TableField]:
    return [
        TableField(name="DATA_YEAR", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="SUSPECTED_DRUG_TYPE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="PROPERTY_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="EST_DRUG_QTY", sql_type=SQLConfig.Types.INTEGER),
        TableField(name="DRUG_MEASURE_TYPE_ID", sql_type=SQLConfig.Types.INTEGER),
        TableField(
            name="NIBRS_SUSPECTED_DRUG_ID",
            sql_type=SQLConfig.Types.INTEGER,
            is_primary=True,
        ),
    ]
