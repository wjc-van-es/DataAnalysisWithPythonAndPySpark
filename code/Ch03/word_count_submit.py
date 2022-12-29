from pyspark.sql import SparkSession
import pyspark.sql.functions as F


spark = SparkSession.builder.appName(
    "Counting word occurrences from a book."
).getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# If you need to read multiple text files, replace `1342-0` by `*`.
results = (
    # if you execute within PyCharm run than the location is relative from
    # /home/willem/git/DataAnalysisWithPythonAndPySpark/code/Ch03
    # if you want to use spark-submit from the command line then make sure you are in the same dir
    # and use: $ spark-submit ./word_count_submit.py
    spark.read.text("../../data/gutenberg_books/1342-0.txt")
    .select(F.split(F.col("value"), " ").alias("line"))
    .select(F.explode(F.col("line")).alias("word"))
    .select(F.lower(F.col("word")).alias("word"))
    .select(F.regexp_extract(F.col("word"), "[a-z']*", 0).alias("word"))
    .where(F.col("word") != "")
    .groupby(F.col("word"))
    .count()

)

results.orderBy("count", ascending=False).show(10)
results.coalesce(1).write.mode('overwrite').csv("./results_single_partition.csv")
