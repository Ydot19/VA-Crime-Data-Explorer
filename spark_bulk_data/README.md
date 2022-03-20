# VA Crime Data with Pyspark --> CockroachDB

Objectives:
- Interaction between Pyspark and SQL DB using jdbc
- Aggregate CSV files and input to CockRoach database
    - Small and bulk uploads
- Dockerize the setup process for ease of setup
- Python Behave Testing of the Data-job Process
- Unit-testing (Goal: Coverage > 80%)


## Commit Standards

Uses pre-commit to set up 

- dev: in-progress feature
- feat: (new feature for the user, not a new feature for build script)
- fix: (bug fix for the user, not a fix to a build script)
- docs: (changes to the documentation)
- style: (formatting, missing semi colons, etc; no production code change)
- refactor: (refactoring production code, eg. renaming a variable)
- test: (adding missing tests, refactoring tests; no production code change)
- chore: (updating grunt tasks etc; no production code change)


## Setup

### Docker Setup Notes

- Requires setting up 3 environment variables
  - CRDB_CERTS
    - Location of SSL certs (node and client certs) on your local computer
      - When running the `crdb-copy-certs.sh` script, this copies the files to the `./temp/certs` directory
  - COCKROACH_USER
  - COCKROACH_PASSWORD
  - COCKROACH_DB

Run the following command
```terminal
$ docker-compose up 
```
from the root project directory

NOTE: 
- more notes coming on how to automate the importing of env variables and automatically setting the admin USER and project DB

### Non Docker Setup Notes
Notes:

- Non-dockerized setup and code development done via WSL2 - Ubuntu Linux 20.04

### Pre-req

- postgresql-42.3.3.jar JDBC Jar for Apache Spark
- Python 3.10.x
- Apache Spark 3.2.1
- CockroachDB v21.2.x

#### Start Cockroach DB (linux Ubuntu/WSL2)

Note: 
- Single node, local setup
- <certs_dir> refers to the location of your SSL certs for cockroachdb relative to where you are executing the command
  OR an absolute path to that directory

Before starting your cockroachdb database, please create your ssl certificates
Follow this link for instructions: [Create SSL Certs with Cockroach CLI](https://www.cockroachlabs.com/docs/v21.1/cockroach-cert)


```zsh
$ cockroach start \
--certs-dir=<certs_dir> \
--store=node1 \
--listen-addr=localhost:26257 \
--join=localhost:26257,localhost:26258,localhost:26259 \
--background \
--cluster-name CDB-VACrime
```

#### Cockroachdb SQL via terminal

```zsh
$ cockroach sql --certs-dir=<certs_dir> --host=localhost:26257
```

once you are in the CockroachDB SQL shell

create your database

```sql
CREATE DATABASE va_crime;
```

Next all subsequent interactions with the CockroachDB SQL shell can be done with the following command

```zsh
$ cockroach sql --certs-dir=<certs_dir> --host=localhost:26257 --database va_crime
```

## Development Notes

### Running Single Python File

When doing sanity checks on a python file to debug, do the following. This project was developed with PyCharm IDE

```python
# functions and classes above
if __name__ == '__main__':
    # Other imports
    # Doing this is particularly important if debugging use pycharm
    # on Windows with your code in WSL, like myself
    import os
        
    os.environ['JAVA_HOME'] = '/path/to/java/11'
    os.environ['SPARK_HOME'] = '/path/to/apache/spark'
    os.environ['PYSPARK_PYTHON'] = '/path/to/virtualenv/python'
```

Alternatively: if you do not use a full-fledged IDE, simply place breakpoints at your points of interest

simply place 
```python
# some script above
breakpoint()
# some script below
```
And execute your entry script from the terminal. This way you can debug using the native pdb module

```zsh
$ python some_entry_script.py
```

## Acknowledgements

### Datasource

- All data used for this project belongs to NIBRS