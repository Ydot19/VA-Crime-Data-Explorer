# PySpark Data Transformations

Objectives:
- Aggregate CSV files and input to CockRoach database
- Document Data source


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


## Development Notes

### Running Single Python File

When doing sanity checks on a python file to debug, do the following

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

