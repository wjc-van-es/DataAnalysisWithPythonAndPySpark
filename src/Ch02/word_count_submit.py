from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName(
    "Counting word occurrences from a book."
).getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# If you need to read multiple text files, replace `1342-0` by `*`.
# ingestion of the text file
# followed by modifying the string fields into list of separate word strings fields by using split,
# where the column is renamed to "line"
#

# We discovered some more constructions that should be cleaned up:
# words ending with 's, ' or 'll should be delivered without these suffixes
# words starting with ' as the start of a quote this prefix should be removed as well
# other words with ' can be considered unique words like don't, shan't and ma'am

windowSpec = Window.orderBy(F.col("count").desc(), F.col("word"))
results = (
    spark.read.text("../../data/gutenberg_books/*.txt")
    .select(F.split(F.col("value"), " ").alias("line"))
    .select(F.explode(F.col("line")).alias("word"))
    .select(F.lower(F.col("word")).alias("word"))
    .select(F.regexp_extract(F.col("word"), "[a-z']*", 0).alias("word"))
    .select(F.regexp_replace(F.col("word"), "^'|'$|'s$|'ll", "").alias("word"))
    .where(F.col("word") != "")
    .groupby(F.col("word"))
    .count()
    #    .orderBy("count", ascending=False)
    .withColumn("index", F.row_number().over(windowSpec))
)

results.coalesce(1) \
    .write \
    .option('header', True) \
    .mode('overwrite') \
    .csv("./results_single_partition.csv")
