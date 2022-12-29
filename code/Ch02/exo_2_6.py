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
#
windowSpec = Window.orderBy(F.col("count").desc())
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

results.show(65, truncate=False)

# With the extra index column we see
# the records with word "the" has the index 1
# the records with word "not" has the index 13
# the records with word "is" has the index 23
# the records with word "is" has the index 62

# Now when we filter the words is "is", "not", "the", "if"
# we get a data frame with only these four records
df_filter_words = results.filter(F.col("word").isin(["is", "not", "the", "if"]))

# we see that there are only four records containing the four words with their respective index values.
df_filter_words.show(65, truncate=False)

# With the ~ operator we can negate the outcome of the isin() function
df_filter_out_words = results.filter(~ F.col("word").isin(["is", "not", "the", "if"]))

# we see the 1rst, 13th, 23th and 62th record are skipped.
df_filter_out_words.show(65, truncate=False)

