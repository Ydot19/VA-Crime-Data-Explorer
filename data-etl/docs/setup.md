# Setup

Objective:
- Outline prerequisites for data transformation and data load

Note:
- Development for this project completed on WSL2 Ubuntu-20.04
    - Project should work similarly on regular Linux Ubuntu-20.04
- Guide will differ based on if you are running on macOS and/or Windows

## NIBRS Data

Steps:
- Visit https://crime-data-explorer.fr.cloud.gov/downloads-and-docs
- Download data based on state (VA in this case) and year
- Collected zip files in a single directory

Example:
```
  data (parent directory)
    |_VA-2000.zip
    |_VA-2001.zip
    |_VA-2002.zip
    ...
```

This directory and its respective csv files will be used by PySpark to upload data to the Couchdb database

## Couchdb

[TO DO]

## Pyspark Data-job

- Make sure you have a virtual environment that starts at the directory of the Pipfile
- If you are having PYTHONPATH issues, please write the follow to a `.env` file

```dotenv
PYTHONPATH=${PYTHONPATH}:${PWD}
```

This will let the python interpreter to detect a path from the current executing directory


### Getting Started

Need to install the following
- [Pipenv](https://pypi.org/project/pipenv/)
- [Pyenv](https://github.com/pyenv/pyenv-installer)
  - Install version `3.9.0` of python (This was used to develop this job flow)
- [Apache Spark 3.x](https://phoenixnap.com/kb/install-spark-on-ubuntu)
  - With scala, and java installations consider using [sdkman](https://github.com/sdkman/sdkman-cli)
  
