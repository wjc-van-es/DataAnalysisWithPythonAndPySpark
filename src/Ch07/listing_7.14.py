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
from dateutil import rrule
from datetime import datetime
from functools import reduce
import os
import pprint
import pyspark.sql.types as T
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
import project_utils.config_info as ci

ci.print_environment()
ci.check_path()

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

table_name = 'backblaze_stats_2019'

# list comprehension based on
# https://stackoverflow.com/questions/11317378/how-to-get-all-dates-month-day-and-year-between-two-dates-in-python
# to get a list of strings representing all file names, one for each day of the year 2019
all_files = [f"{dt.strftime('%Y-%m-%d')}.csv" for dt in rrule.rrule(rrule.DAILY,
                                                                    dtstart=datetime.strptime(start_date, '%Y-%m-%d'),
                                                                    until=datetime.strptime(end_date, '%Y-%m-%d'))]

print(f"The number of files should be 365 for each day of the year 2019: {len(all_files)}")
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

print(f"we now have a list of 365 separate data frames {len(data)}, type(data[0]) = {type(data[0])}")
# the last file, 2019-12-31.csv, represents the 365th day of the year, which has a 0-based index of 364.
# data[364].printSchema()
# data[364].show(5, truncate=False)
# spark.read.csv(os.path.join(data_dir, '2019-12-31.csv'), header=True, inferSchema=True).printSchema()
# pprint.pprint(data)

# merging all 365 dataframes in the list data with functools reduce and DataFrame.unionAll, provided all dataframes
# share the same schema and have the columns in the same order
# source: https://walkenho.github.io/merging-multiple-dataframes-in-pyspark/
merged_df = reduce(DataFrame.unionAll, data).dropna()

print(f"We now have a merged data frame with this number of rows: {merged_df.count()}")
merged_df.show(5, truncate=False)

# The actual listing 7.8 combined with listing 7.9
# The SQL way takes pretty long
merged_df.createOrReplaceTempView(table_name)


print("""
      List tables in catalog after executing a SQL statements:
       We expect now only expect backblaze_stats_2019 that was
       created with the DataFrame's createOrReplaceTempView() method.
      """)
pprint.pprint(spark.catalog.listTables('default'))

# Example of two common table expressions or CTE using the WITH keyword to define temporary tables, whose aliases can be
# targeted in the following query and that will be dropped after query execution has finished.
joined = spark.sql(
   f"""
    WITH drive_days AS (
        SELECT 
            model, 
            count(*) AS drive_days
        FROM backblaze_stats_2019
        GROUP BY model),
    failures AS (
        SELECT 
            model, 
            count(*) AS failures
        FROM {table_name}
        WHERE failure = 1
        GROUP BY model)
    
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

spark.catalog.dropTempView(table_name)
spark.stop()

if __name__ == "__main__":
    pass
