#!/usr/bin/env python
import os
import sys
from pyspark.sql import SparkSession

"""
This script is to check whether pyspark is available.
We should be able to launch it when the conda dasci environment is activated
"""


def print_environment():
    # We made an iterable stream of environment variables filtered by filtertuple
    # Only vars with a key that contain any of the fragments in filtertuple are included
    filtertuple = ("CONDA", "SPARK", "PYTHON", "JAVA", "PATH", "IBAN", "ROOT_DIR")
    stream = (item for item in os.environ.items() if any(fragment in item[0] for fragment in filtertuple))
    # print(stream)
    # print(stream[0])
    for k, v in iter(stream):
        print(f'{k}={v}')


def check_path():
    try:
        conda_prefix = os.environ['CONDA_PREFIX']
        user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    except KeyError:
        user_paths = []

    print(f"CONDA_PREFIX: {conda_prefix}")
    print("PYTHONPATH: ", user_paths)
    print("sys.path: ")
    for path in sys.path:
        print(path)


def create_path_from_year(year):
    """
    creates the path to the csv file based on the year and two environment variables
    :param year:
    :return:
    """
    iban = str(os.getenv("MY_IBAN")).strip() # set in the conda dasci env can only be read when run in terminal not in pyspark
    print(iban)
    root_dir = os.getenv(
        "BANK_ROOT_DIR").strip()  # set in the conda dasci env can only be read when run in terminal not in pyspark
    file_name = f"{iban}_01-01-{year}_31-12-{year}.csv"
    path = f"{root_dir}{file_name}"
    print(path)
    return path


def check_pyspark(year):
    path = create_path_from_year(year)
    if "NL79" in path:
        spark = SparkSession \
            .builder \
            .appName(f"Analyzing bank statements of {path}") \
            .getOrCreate()
        data = spark.read \
            .format("csv") \
            .option("header", "true") \
            .load(path)
        data.printSchema()
        data.count()
        data.show(5)
    else:
        print(f"something wrong with the path: {path}")


def main(args):
    year = 2021
    if len(args) > 0:
        print(f"args = {args}")
        year = args[0]
    print_environment()
    check_path()
    check_pyspark(year)


if __name__ == '__main__':
    print(f"__name__=={__name__}")
    main(sys.argv[1:])
