from pyspark.sql import SparkSession
import project_utils.config_info as ci

# code that should be called before any PySpark dependencies
ci.load_env_file_when_present('project.env')

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
