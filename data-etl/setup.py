"""
Used to set up the data needed for this section of the project
File has no dependency on pipenv environment and can be used outside the environment
"""


def unpack_source_data():
    import tarfile
    import os
    import zipfile

    base_path = "spark_bulk_data/resources/source_data"

    print("STARTED  UNPACKING THE TAR FILE...\n")
    tarred = tarfile.open("source.data.tar")
    os.makedirs(f"{base_path}/zipped")
    tarred.extractall(f"{base_path}/zipped")
    print("FINISHED UNPACKING THE TAR FILE...\n")
    tarred.close()

    zipped_files = os.listdir(f"{base_path}/zipped")
    print("STARTED  Unzipping...\n")
    for zf in zipped_files:
        src = f"{base_path}/zipped/{zf}"
        with zipfile.ZipFile(src, "r") as zipped:
            folder = zf.split(".")[0]
            unzip_path = f"{base_path}/unzipped/{folder}"
            os.makedirs(unzip_path)
            zipped.extractall(unzip_path)

    print("FINISHED Unzipping...\n")
    # for folder in data_folders:
    #     folder_path = f"{base_path}/{folder}"
    #     tarred.add(folder_path, arcname=folder)


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


def setup():
    create_env_file()


if __name__ == "__main__":
    unpack_source_data()
