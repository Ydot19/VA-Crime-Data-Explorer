"""
Used to create the models for the tables

This reduces repetitive copy and paste actions
"""
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))


def create_headers():
    arg = input("Enter Column Data:\t")
    pre_processed = arg.split(",")
    returnable = ""
    for pp in pre_processed:
        returnable += f"\t\tTableField(name={pp}, sql_type=SQLConfig.Types.STRING),\n"

    returnable = f"[\n{returnable}\n\t]"
    returnable = returnable[::-1].replace(",", "", 1).replace("\n", "", 1)[::-1]
    return returnable


def write_out(headers: str):
    fn = input("\nEnter Filename:\t")
    fn_path = f"spark_bulk_data/models/tables/{fn}"
    lines = [
        "from spark_bulk_data.models.TableFieldDataClass import TableField\n",
        "from spark_bulk_data.config import SQLConfig\n\n\n",
        "def get_headers() -> list[TableField]:\n" f"\treturn {headers}",
    ]
    with open(fn_path, "a") as pyfile:
        pyfile.writelines(lines)


if __name__ == "__main__":
    head = create_headers()
    write_out(headers=head)
