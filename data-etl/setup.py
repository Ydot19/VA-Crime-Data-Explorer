"""
Used to set up the data needed for this section of the project
File has no dependency on pipenv environment and can be used outside the environment
"""
import curses
from curses import wrapper
from typing import Callable, List


def meta_name(func_name: str):
    def decorator(f: Callable):
        f.__name__ = func_name
        return f
    return decorator


@meta_name("Unpack Source Data From Tar File")
def unpack_source_data():
    import tarfile
    import os
    from pathlib import Path

    temp_dir_path = f"{Path().resolve()}/temp"
    print("STARTED  UNPACKING THE TAR FILE...\n")
    with tarfile.open("data.tar.gz") as tarred:
        if not os.path.exists(temp_dir_path):
            os.makedirs(f"{temp_dir_path}")
        tarred.extractall(f"{temp_dir_path}")
    print("FINISHED UNPACKING THE TAR FILE...\n")


@meta_name("Create Env Example File")
def create_env_file():
    import inspect

    file_content = """# COPY THIS FILE TO A .env File and then start/restart your pipenv environment
    
    # Used to set the python python to current working directory
    PYTHONPATH =${PYTHONPATH}:${PWD}

    # DATA
    DATA_DIR = "Relative path to zip files containing each years csv files"
    START_YEAR = 2000
    END_YEAR = 2019

    # DATABASE CONFIGURATIONS
    CLUSTER = "YOUR CLUSTERS NAME HERE"
    DATABASE = "YOUR DATABASE NAME HERE"
    USER = "USER NAME"
    PASSWORD = "DB USER Password"
    HOST = localhost  # Defaults to local host, feel free to change
    PORT = 26257  # Default port number
    SSL_ROOT_CERT = "CA Certificate absolute file path"
    SSL_KEY = "SSL Key absolute file path"
    SSL_CERT = "SSL Cert absolute file path"

    # Spark jars
    JDBC_JAR = "Absolute path postgres jdbc jar"
    """

    filename = ".env.example"

    with open(filename, "+w") as f:
        f.write(inspect.cleandoc(file_content))


SELECT_FROM: List[Callable] = [unpack_source_data, create_env_file]


def current_selection(key_action: int, curr: int):
    max_len = len(SELECT_FROM)
    if key_action == 258 or key_action == curses.KEY_DOWN:
        calc_val = curr - 1
        return max_len - 1 if calc_val < 0 else calc_val
    elif key_action == 259 or key_action == curses.KEY_UP:
        calc_val = curr + 1
        return 0 if calc_val == max_len else calc_val
    return curr


def main(screen: curses.window):
    curr = 0
    key_entered = -1
    while key_entered != curses.KEY_ENTER and key_entered != 10 and key_entered != 13:
        curr = current_selection(key_entered, curr)
        screen.clear()
        screen.refresh()
        screen.addstr("Select Action: \n\n")
        for idx, func in enumerate(SELECT_FROM):
            if idx != curr:
                screen.addstr(f"{func.__name__}\n")
            else:
                screen.addstr(f">> {func.__name__}\n", curses.A_BOLD)
        key_entered = screen.getch()
    # execute selection
    SELECT_FROM[curr]()


wrapper(main)
