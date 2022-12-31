from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import numpy as np
import os

# relative to ~/git/DataAnalysisWithPythonAndPySpark/code/Ch04 as we will execute from this location when running
# directly in PyCharm IDE.
# Hence, when using spark-submit from CLI terminal
# we should be in ~/git/DataAnalysisWithPythonAndPySpark/code/Ch04 as well
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

# a numpy array of lists containing 3 column names
column_split = np.array_split(np.array(logs_df.columns), len(logs_df.columns) // 3)
print(type(column_split))

for columns in column_split:
    logs_df.select(*columns).show(5, truncate=False)

# For our purposes programClassID and Duration seem interesting
