#!/usr/bin/env python
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col
from pyspark.sql.functions import when
from pyspark.sql.functions import round as ps_round


def produce_df_for_year(year):
    """

    :param year:
    :return:
    """
    path = create_path_from_year(year)
    app_name = f"Analyzing bank statements {path}"
    spark = SparkSession \
        .builder \
        .appName(app_name) \
        .getOrCreate()
    raw_df = spark.read \
        .format("csv") \
        .option("header", "true") \
        .load(path)

    return create_bedrag_column(raw_df)


def create_path_from_year(year):
    """
    creates the path to the csv file based on the year and two environment variables that should be set
    MY_IBAN and BANK_ROOT_DIR
    :param year:
    :return:
    """
    env_iban_key = "MY_IBAN"
    env_root_dir_key = "BANK_ROOT_DIR"
    iban = os.getenv(env_iban_key)  # set in the conda dasci env can only be read when run in terminal not in pyspark
    root_dir = os.getenv(
        env_root_dir_key)  # set in the conda dasci env can only be read when run in terminal not in pyspark
    if iban is None:
        raise ValueError(f"Value of environment variable '{env_iban_key}' could not be obtained. Please check.")
    if root_dir is None:
        raise ValueError(f"Value of environment variable '{env_root_dir_key}' could not be obtained. Please check.")
    file_name = f"{iban}_01-01-{year}_31-12-{year}.csv"
    path = f"{root_dir}{file_name}"
    return path


def create_bedrag_column(in_def):
    """
    cleans up the pyspark dataframe by adding a 'Bedrag' column of type double with a negative value
    when the column 'Af Bij' contains the value 'Af'.
    The columns 'Af Bij' and the column Bedrag (EUR) are then dropped
    :param in_def: the dataframe that needs the clean up
    :return: the restructured pyspark dataframe
    """

    # replace comma with period as decimal division symbol and change type to double
    df_1 = in_def.withColumn('Bedrag (EUR)', regexp_replace('Bedrag (EUR)', ',', '.')) \
        .withColumn("Bedrag (EUR)", col("Bedrag (EUR)").cast("double"))

    df_2 = df_1.withColumn('Bedrag', when(col('Af Bij') == 'Af', -1 * col('Bedrag (EUR)')) \
        .otherwise(col('Bedrag (EUR)'))) \
        .drop(col('Af Bij')) \
        .drop(col('Bedrag (EUR)'))

    return df_2


def sum_per_tegenrekening(in_df):
    """
    creates a dataframe where all amounts from 'Bedrag' are summed grouped by the columns 'Tegenrekening' and
     'Naam / Omschrijving'

    :param in_df: the prepared dataframe from the bank_statements csv
    :return: dataframe with aggregated data
    """
    return in_df.groupBy('Tegenrekening', 'Naam / Omschrijving') \
        .agg({'Bedrag': 'sum'}) \
        .withColumn("Totaal", ps_round(col("sum(Bedrag)"), 2)) \
        .drop(col("sum(Bedrag)")) \
        .orderBy("Totaal")

def main(args):
    year = 2020
    if len(args) > 0:
        print(f"args = {args}")
        year = args[0]
    print(create_path_from_year(year))


if __name__ == '__main__':
    print(f"__name__=={__name__}")
    main(sys.argv[1:])