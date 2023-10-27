from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os

# relative to ~/git/DataAnalysisWithPythonAndPySpark/src/Ch04 as we will execute from this location when running
# directly in PyCharm IDE.
# Hence, when using spark-submit from CLI terminal
# we should be in ~/git/DataAnalysisWithPythonAndPySpark/src/Ch04 as well
data_root_dir = "../../data/broadcast_logs"
broadcasts_file = "BroadcastLogs_2018_Q3_M8_sample.CSV"

spark = SparkSession.builder.appName("Canadian Broadcasting Shizzle").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

logs_df = spark.read.csv(
    os.path.join(data_root_dir, broadcasts_file),
    sep='|',
    header=True,
    inferSchema=True,
    timestampFormat='yyyy-MM-dd',
)
logs_df.printSchema()

# works with just as well with a tuple comprehension as with a list comprehension
# as the select column name arguments are unpacked anyway
logs_no_id = logs_df.select(*(col for col in logs_df.columns if not col.endswith('ID') ))

logs_no_id.printSchema()
