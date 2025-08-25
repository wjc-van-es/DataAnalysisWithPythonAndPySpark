from pyspark.sql import SparkSession
import pyspark.sql.types as T
import pyspark.sql.functions as F
from pprint import pprint
import project_utils.config_info as ci

# code that should be called before any PySpark dependencies
ci.load_env_file_when_present('project.env')

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df_exo6_8 = spark.createDataFrame([[1, 2], [2, 4], [3, 9]], ["one", "square"])

df_exo6_8.printSchema()
df_exo6_8.show(truncate=False)

map_exo6_8 = (df_exo6_8
            .select(F.struct(F.col('one'), F.col('square')).alias('struct'))
            .agg(F.collect_list(F.col('struct')).alias('as_list'))
            .select(F.map_from_entries(F.col('as_list')).alias('squares_map'))
              )
map_exo6_8.printSchema()
map_exo6_8.show(truncate=False)
pprint(map_exo6_8)

if __name__ == "__main__":
    pass
