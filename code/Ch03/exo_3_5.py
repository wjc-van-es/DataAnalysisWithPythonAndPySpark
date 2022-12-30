from pyspark.sql import SparkSession
import pyspark.sql.functions as F


spark = SparkSession.builder.appName(
    "Counting word occurrences from a book."
).getOrCreate()

spark.sparkContext.setLogLevel("WARN")

first_letter_header = 'First Letter'
total_header = 'total'
vowels = ['a','e','i','o','u']

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
    .filter(F.col("word") != "")
    .select(F.substring(F.col("word"), 0, 1).alias(first_letter_header))
    .groupby(F.col(first_letter_header))
    .count()
    .orderBy("count", ascending=False)
)
# the distinct words are the total number of rows in the data frame:
print(f"The number of distinct words is the total number of rows in the data frame: {results.count()}")
results.show(26)
results.show(5)
# results.coalesce(1).write.mode('overwrite').csv("./results_single_partition.csv")
words_starting_vowel = (results
                        .filter(F.col(first_letter_header).isin(vowels))
                        .select(F.sum(F.col('count')).alias(total_header)))
print(words_starting_vowel.show())
print(f"Number of words starting with a vowel: {words_starting_vowel.first()[total_header]}")

words_starting_consonant = (results
                        .filter(~ F.col(first_letter_header).isin(vowels))
                        .select(F.sum(F.col('count')).alias(total_header)))
print(words_starting_consonant.show())
print(f"Number of words starting with a consonant: {words_starting_consonant.first()[total_header]}")