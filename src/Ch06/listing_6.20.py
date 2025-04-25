import os

from py4j.protocol import Py4JJavaError
from pyspark.sql import SparkSession
import pyspark.sql.types as T
import project_utils.config_info as ci

ci.load_env_file_when_present('project.env')

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

data_dir = "../../data/shows"

episode_schema = T.StructType(
    [
        T.StructField("airdate", T.DateType()),
        T.StructField("id", T.StringType()),
        T.StructField("name", T.StringType()),
        T.StructField("number", T.LongType()),
        T.StructField("season", T.LongType()),
        T.StructField("summary", T.LongType()), # deliberate mistype to check the exception you get
        T.StructField("url", T.LongType()), # deliberate mistype to check the exception you get
    ]
)

summary_schema = T.StructType(
    [
        T.StructField("id", T.StringType()),
        T.StructField("name", T.StringType()),
        T.StructField(
            "_embedded",
            T.StructType(
                [
                    T.StructField(
                        "episodes", T.ArrayType(episode_schema)
                    )
                ]
            )
        )
    ]
)

# the summary schema has a wrong assumption for two summary fields
df_with_wrong_schema = spark.read.json(os.path.join(data_dir, '*.json'),
                                       multiLine=True,
                                       schema=summary_schema,
                                       mode='FAILFAST')

df_with_wrong_schema.printSchema()
try:
    df_with_wrong_schema.show(truncate=False)
except Py4JJavaError:
    pass


if __name__ == "__main__":
    pass