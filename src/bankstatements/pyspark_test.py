#!/usr/bin/env python
import os
import sys
from pyspark.sql import SparkSession
# import project_utils.config_info as ci # works as well
from project_utils import config_info as ci

"""
This script is to check whether pyspark is available.
We should be able to launch it when the conda ds311 or ds312 environment is activated
Also $MY_IBAN and $BANK_ROOT_DIR should be set as environment variables
This can be done in ~/.bashrc with
~$ gedit .bashrc
~$ source .bashrc
If you run this from the commandline set PYTHONPATH to the src/ dir to be able to find the module
project_utils.config_info that you can find direct under the src/ dir
(ds311) willem@willem-Latitude-5590:~/git/DataAnalysisWithPythonAndPySpark/src/bankstatements$ PYTHONPATH=../ python pyspark_test.py 2023

"""


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
    path = os.path.join(root_dir, file_name)
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
    ci.print_environment()
    ci.check_path()
    check_pyspark(year)


if __name__ == '__main__':
    print(f"__name__=={__name__}")
    print(f"sys.argv={sys.argv}")
    main(sys.argv[1:])
