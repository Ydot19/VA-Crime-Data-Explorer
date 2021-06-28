from dataclasses import dataclass


@dataclass
class TableField:
    name: str
    sql_type: str
    is_primary: bool = False
