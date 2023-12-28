from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# The RDD functions and methods are under the
# SparkContext object, accessible as an attribute of
# our SparkSession. I alias it to sc for convenience.
sc = spark.sparkContext

collection = [1, "two", 3.0, ("four", 4), {"five": 5}]

collection_rdd = sc.parallelize(collection)

print(f"type(collection_rdd)={type(collection_rdd)}")

if __name__ == "__main__":
    pass
