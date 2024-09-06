# most_reliable_drives.py #####################################################
#
# This program computes the most reliable drives for a given set of capacities.
#
# We are looking at (± 10% by default)
#
#  - 500GB
#  - 1TB
#  - 2TB
#  - 4TB
#
###############################################################################
# tag::ch07-src-final-ingestion[]
from pyspark.sql.utils import AnalysisException
from dateutil import rrule
from datetime import datetime
from functools import reduce
import os
import pprint
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()

data_dir = "../../data/Ch07/"


start_date = '2019-01-01'
end_date = '2019-01-31'
# loading the whole year gives stack overflow
# end_date = '2019-12-31'


# list comprehension based on
# https://stackoverflow.com/questions/11317378/how-to-get-all-dates-month-day-and-year-between-two-dates-in-python
# to get a list of strings representing all file names, one for each day of the year 2019
all_files = [f"{dt.strftime('%Y-%m-%d')}.csv" for dt in rrule.rrule(rrule.DAILY,
                                                                    dtstart=datetime.strptime(start_date, '%Y-%m-%d'),
                                                                    until=datetime.strptime(end_date, '%Y-%m-%d'))]

pprint.pprint(all_files)

# DATA_FILES = [
#     "drive_stats_2019_Q1",
#     "data_Q2_2019",
#     "data_Q3_2019",
#     "data_Q4_2019",
# ]
#

data = [
    spark.read.csv(os.path.join(data_dir, file), header=True, inferSchema=True)
    for file in all_files
]

common_columns = list(
    reduce(lambda x, y: x.intersection(y), [set(df.columns) for df in data])
)

assert set(["model", "capacity_bytes", "date", "failure"]).issubset(
    set(common_columns)
)

full_data = reduce(
    lambda x, y: x.select(common_columns).union(y.select(common_columns)), data
)
# end::ch07-src-final-ingestion[]

# tag::ch07-src-final-processing[]
full_data = full_data.selectExpr(
    "model", "capacity_bytes / pow(1024, 3) capacity_GB", "date", "failure"
)
# full_data.printSchema()
# full_data.createOrReplaceTempView("full_data")
# try:
#     spark.sql(
#         '''
#         select model
#         from full_data
#         where failure = 1
#         '''
#     ).show(5)
# except AnalysisException as e:
#     print(e)

drive_days = full_data.groupby("model", "capacity_GB").agg(
    F.count("*").alias("drive_days")
)

failures = (
    full_data.where("failure = 1")
    .groupby("model", "capacity_GB")
    .agg(F.count("*").alias("failures"))
)

failures.printSchema()
failures.show()

summarized_data = (
    drive_days.join(failures, on=["model", "capacity_GB"], how="left")
    .fillna(0.0, ["failures"])
    .selectExpr("model", "capacity_GB", "failures / drive_days failure_rate")
    .cache()
)

summarized_data.printSchema()
summarized_data.show()
# end::ch07-src-final-processing[]


# tag::ch07-src-final-function[]


def most_reliable_drive_for_capacity(data, capacity_GB=2048, precision=0.25, top_n=3):
    """Returns the top 3 drives for a given approximate capacity.

    Given a capacity in GB and a precision as a decimal number, we keep the N
    drives where:

    - the capacity is between (capacity * 1/(1+precision)), capacity * (1+precision)
    - the failure rate is the lowest

    """
    capacity_min = capacity_GB / (1 + precision)
    capacity_max = capacity_GB * (1 + precision)

    answer = (
        data.where(f"capacity_GB between {capacity_min} and {capacity_max}")  # <1>
        .orderBy("failure_rate", "capacity_GB", ascending=[True, False])
        .limit(top_n)  # <2>
    )

    return answer


# end::ch07-src-final-function[]
# most_reliable_drive_for_capacity(full_data)
results = most_reliable_drive_for_capacity(summarized_data, capacity_GB=11176.0, top_n=25)
results.show(truncate=False)


if __name__ == "__main__":
    pass
