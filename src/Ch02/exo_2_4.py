from pyspark.sql import SparkSession
from pyspark.sql.functions import col, greatest
from pyspark.sql.utils import AnalysisException
import numbers

spark = SparkSession.builder.appName("exercise 2.4").getOrCreate()
exo2_4_df = spark.createDataFrame(
    [["key", 10_000, 20_000]], ["key", "value1", "value2"]
)
exo2_4_df.printSchema()
# root
# |-- key: string (containsNull = true)
# |-- value1: long (containsNull = true)
# |-- value2: long (containsNull = true)
# `greatest` will return the greatest value of the list of column names,
# skipping null value
# The following statement will return an error


try:
    exo2_4_mod = exo2_4_df.select(
        col("key"),  # adding the key column will fix it
        greatest(col("value1"), col("value2")).alias("maximum_value")
    ) #.select("key", "maximum_value") # unnecessary even
    exo2_4_mod.show(truncate=False)
except AnalysisException as err:
    print(err)

# alternative for the strict select is just create an extra column without selecting implicitly including
# all columns that are not actively removed.
df_with_max = exo2_4_df.withColumn("max_value", greatest(col("value1"), col("value2")))
df_with_max.printSchema()
df_with_max.show(truncate=False)