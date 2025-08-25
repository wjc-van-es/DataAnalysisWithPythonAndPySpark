from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os
import project_utils.config_info as ci

# code that should be called before any PySpark dependencies
ci.load_env_file_when_present('project.env')

data_root_dir = "../../data/sample_csv"
broadcasts_file = "sample.csv"

spark = SparkSession.builder.appName("Sample with $ as quotes Shizzle").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

logs_df = spark.read.csv(
    os.path.join(data_root_dir, broadcasts_file),
    sep=',',
    quote='$',
    header=True,
    inferSchema=True,
).withColumn('Subtotal', F.col('Quantity') * F.col('Price'))

logs_df.printSchema()
logs_df.show(5, truncate=False)

total_df = logs_df.agg(F.sum('Subtotal').alias('Total'))
total_df.printSchema()
total_df.show()

if __name__ == "__main__":
    pass
