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
# tag::ch07-code-final-ingestion[]
from pyspark.sql.utils import AnalysisException
from dateutil import rrule
from datetime import datetime
from functools import reduce
import os
import pprint
import pyspark.sql.types as T
import pyspark.sql.functions as F
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

spark = (SparkSession.builder
                 .appName("Chapter 7 example")
                 .config('spark.driver.memory', '8g')
                 .config('spark.executor.memory', '8g')
                 .master('local[8]')
                 .getOrCreate())

# We get 365 warnings like
# CSV file: file:///home/willem/git/DataAnalysisWithPythonAndPySpark/data/Ch07/2019-12-28.csv
# 23/02/08 21:59:12 WARN CSVHeaderChecker: Number of column in CSV header is not equal to number of fields in the schema:
#  Header length: 131, schema size: 5
# But only after using merged_df.createOrReplaceTempView("backblaze_stats_2019") on the merged dataframe
spark.sparkContext.setLogLevel("ERROR")

data_dir = "../../data/Ch07/"

start_date = '2019-01-01'
end_date = '2019-12-31'
# loading the whole year gives stack overflow
# end_date = '2019-12-31'


# list comprehension based on
# https://stackoverflow.com/questions/11317378/how-to-get-all-dates-month-day-and-year-between-two-dates-in-python
# to get a list of strings representing all file names, one for each day of the year 2019
all_files = [f"{dt.strftime('%Y-%m-%d')}.csv" for dt in rrule.rrule(rrule.DAILY,
                                                                    dtstart=datetime.strptime(start_date, '%Y-%m-%d'),
                                                                    until=datetime.strptime(end_date, '%Y-%m-%d'))]

# pprint.pprint(all_files)

# alternative approach do not infer schema, but impose our own with only the fields we will investigate and are
# present in all the files, this will enhance performance and hopefully prevent out of memory errors
# all other columns will be discarded.
schema = T.StructType(
    [
        T.StructField("date", T.DateType(), nullable=False),
        T.StructField("serial_number", T.StringType(), nullable=False),  # DateType default format is yyyy-MM-dd
        T.StructField("model", T.StringType(), nullable=False),
        T.StructField("capacity_bytes", T.LongType(), nullable=False),
        T.StructField("failure", T.IntegerType(), nullable=False),

    ]
)

# a list of dataframes
data = [
    spark.read.csv(os.path.join(data_dir, file), header=True, schema=schema, mode='PERMISSIVE')
    for file in all_files
]
# the last file, 2019-12-31.csv, represents the 365th day of the year, which has a 0-based index of 364.
# data[364].printSchema()
# data[364].show(5, truncate=False)
# spark.read.csv(os.path.join(data_dir, '2019-12-31.csv'), header=True, inferSchema=True).printSchema()
# pprint.pprint(data)

# merging all 365 dataframes in the list data with functools reduce and DataFrame.unionAll, provided all dataframes
# share the same schema and have the columns in the same order
# source: https://walkenho.github.io/merging-multiple-dataframes-in-pyspark/
merged_df = reduce(DataFrame.unionAll, data).dropna()

# The actual listing 7.8 combined with listing 7.9
# The SQL way takes pretty long
merged_df.createOrReplaceTempView("backblaze_stats_2019")

spark.sql(
    """
    CREATE OR REPLACE TEMP VIEW drive_days AS
    SELECT model, count(*) AS drive_days
    FROM backblaze_stats_2019
    GROUP BY model
    """
)

# # alternatively we could have used a normal SQL select query and assigned it to a data frame variable
# drive_days = spark.sql(
#     """
#     SELECT model, count(*) AS drive_days
#     FROM backblaze_stats_2019
#     GROUP BY model
#     """
# )
#
# # or use PySpark's DataFrame methods to do the same
# drive_days = merged_df.groupby(F.col("model")).agg(
#     F.count(F.col("*")).alias("drive_days")
# )

spark.sql(
    """
    CREATE OR REPLACE TEMP VIEW failures AS
    SELECT model, count(*) AS failures
    FROM backblaze_stats_2019
    WHERE failure = 1
    GROUP BY model
    """
)

# # alternatively we could have used a normal SQL select query and assigned it to a data frame variable
# failures = spark.sql(
#     """
#     SELECT model, count(*) AS failures
#     FROM backblaze_stats_2019
#     WHERE failure = 1
#     GROUP BY model
#     """
# )
#
# # or use PySpark's DataFrame methods to do the same
# failures = (
#     merged_df.where(F.col("failure") == 1)
#     .groupby(F.col("model"))
#     .agg(F.count(F.col("*")).alias("failures"))
# )

print("""
      List tables in catalog after executing a SQL statements:
      'CREATE OR REPLACE TEMP VIEW drive_days ...' &
      'CREATE OR REPLACE TEMP VIEW failures ...'
       We expect both drive_days and failures to be in the list besides the backblaze_stats_2019 that was
       created with the DataFrame's createOrReplaceTempView() method.
      """)
pprint.pprint(spark.catalog.listTables('default'))

joined = spark.sql(
    """
    select
        drive_days.model,
        drive_days,
        failures
    from drive_days
    left join failures
    on drive_days.model = failures.model
    """
)

joined.show(5, truncate=False)
# alternative using the methods from PySpark's DataFrame object
# drive_days.join(failures, on="model", how="left").show(5)

# merged_df.groupby(F.col("model")).agg(
#     F.min(F.col("capacity_bytes") / F.pow(F.lit(1024), 3)).alias("min_GB"),
#     F.max(F.col("capacity_bytes") / F.pow(F.lit(1024), 3)).alias("max_GB"),
# ).where(F.col("min_GB") != F.col("max_GB")).orderBy(F.col("max_GB"), ascending=False).show(5)
# merged_df.show(truncate=False)

# common_columns = list(
#     reduce(lambda x, y: x.intersection(y), [set(df.columns) for df in data])
# )
#
# assert set(["model", "capacity_bytes", "date", "failure"]).issubset(
#     set(common_columns)
# )
#
# full_data = reduce(
#     lambda x, y: x.select(common_columns).union(y.select(common_columns)), data
# )
# # end::ch07-code-final-ingestion[]
#
# # tag::ch07-code-final-processing[]
# full_data = full_data.selectExpr(
#     "model", "capacity_bytes / pow(1024, 3) capacity_GB", "date", "failure"
# )
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
#
# drive_days = full_data.groupby("model", "capacity_GB").agg(
#     F.count("*").alias("drive_days")
# )
#
# failures = (
#     full_data.where("failure = 1")
#     .groupby("model", "capacity_GB")
#     .agg(F.count("*").alias("failures"))
# )
#
# failures.printSchema()
# failures.show()
#
# summarized_data = (
#     drive_days.join(failures, on=["model", "capacity_GB"], how="left")
#     .fillna(0.0, ["failures"])
#     .selectExpr("model", "capacity_GB", "failures / drive_days failure_rate")
#     .cache()
# )
#
# summarized_data.printSchema()
# summarized_data.show()
# # end::ch07-code-final-processing[]
#
#
# # tag::ch07-code-final-function[]
#
#
# def most_reliable_drive_for_capacity(data, capacity_GB=2048, precision=0.25, top_n=3):
#     """Returns the top 3 drives for a given approximate capacity.
#
#     Given a capacity in GB and a precision as a decimal number, we keep the N
#     drives where:
#
#     - the capacity is between (capacity * 1/(1+precision)), capacity * (1+precision)
#     - the failure rate is the lowest
#
#     """
#     capacity_min = capacity_GB / (1 + precision)
#     capacity_max = capacity_GB * (1 + precision)
#
#     answer = (
#         data.where(f"capacity_GB between {capacity_min} and {capacity_max}")  # <1>
#         .orderBy("failure_rate", "capacity_GB", ascending=[True, False])
#         .limit(top_n)  # <2>
#     )
#
#     return answer
# end::ch07-code-final-function[]
# most_reliable_drive_for_capacity(full_data)

if __name__ == "__main__":
    pass
