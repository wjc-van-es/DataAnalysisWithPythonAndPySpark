from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os

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
