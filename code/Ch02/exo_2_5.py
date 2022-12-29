from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName(
    "Counting word occurences from a book."
).getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# If you need to read multiple text files, replace `1342-0` by `*`.
# ingestion of the text file
# followed by modifying the string fields into list of separate word strings fields by using split,
# where the column is renamed to "line"

# ordering first to count and then to word (alphabetical order whenever the count has the same value)
windowSpec = Window.orderBy(F.col("count").desc(), F.col("word"))
results = (
    spark.read.text("../../data/gutenberg_books/1342-0.txt")
    .select(F.split(F.col("value"), " ").alias("line"))
    .select(F.explode(F.col("line")).alias("word"))
    .select(F.lower(F.col("word")).alias("word"))
    .select(F.regexp_extract(F.col("word"), "[a-z']*", 0).alias("word"))
    .where(F.col("word") != "")
    .groupby(F.col("word"))
    .count()
 #   .orderBy("count", ascending=False)
    .withColumn("index", F.row_number().over(windowSpec))
)

results.show(30, truncate=False)

# With the extra index column we see is at index 23

# Now when we filter out the word is
df_without_is = results.filter(F.col("word") != "is")

# we see that the record containing the word "is" at index 23 is skipped
df_without_is.show(30, truncate=False)

# Skipping all words shorter than 4 characters
df_over_3_char = df_without_is.filter(F.length(F.col("word")) > 3)

# we see that the records with index 1 to 10 are skipped because the words are shorter than 4 character
# thus record with index 11 and word "that" is the first entry and
# record with index 20 and word "with" is the second entry.
df_over_3_char.show(30, truncate=False)

# ordered_results = results.orderBy("count", ascending=False)
# results.coalesce(1) \
#     .write \
#     .option('header', True) \
#     .mode('overwrite') \
#     .csv("./results_single_partition.csv")
