import pyspark.sql.types as T
import pyspark.sql.functions as F
import os
from pyspark.sql import SparkSession

# Setting up a schema definition for shows data
# where we build up from discrete StructType elements assigned to variables.
# This should improve readability over a single schema variable with deep nested complex types

episode_schema = T.StructType(
    [
        T.StructField("season", T.LongType()),
        T.StructField("number", T.LongType()),
        T.StructField("name", T.StringType()),
        T.StructField("airdate", T.DateType()),
        T.StructField("summary", T.StringType()),

    ]
)

embedded_schema = T.StructType(
    [
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

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

data_dir = "../../data/shows"

# The original json document was a single line and this is the PySpark default rule of:
# "One JSON document, one line, one (df) record",
# where multiple JSON docs / df records can fit in one file
# each on a new line. This is set by the optional parameter multiLine, which has a default of False
#
# We already went exploring and ordered the PyCharm IDE to reformat the src, so we get an indented multiline
# JSON document, which is much easier to read.
# When we print the schema we now get
# root
#  |-- _corrupt_record: string (nullable = true)
# However, if we set the optional multiline parameter to True it will be able to load the multiline document, which now
# follow the adapted PySpark rule of
# "one JSON document, one file, one (df) record"
df_sil_val = spark.read.json(os.path.join(data_dir, 'shows-silicon-valley.json'), multiLine=True,
                             schema=embedded_schema, mode='FAILFAST')

# you have one record, where each column is a field on the highest level under the document root
# hence these columns can have simple values when the corresponding field is a simple scalar type or
# a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
# objects or arrays)
print(f"total number of records in df_sil_val data frame is  {df_sil_val.count()}")

df_sil_val.printSchema()
df_sil_val.show()

# essentially the same modifications as done in
# DataAnalysisWithPythonAndPySpark/src/Ch06/listing_6.14_6.15_create_tabular_episodes.py
# but slightly more compressed and on a relevant subset of the data selected with our own schema
# assigned to the embedded_schema variable, only capturing the relevant embedded data for the series' every episode.
exploded_episodes = (df_sil_val.withColumn(
                        "episodes", F.col("_embedded.episodes")
                    )
                    .drop("_embedded")
                    .select(F.explode(F.col('episodes')).alias('episodes'))
)
print(f"total number of records in tabular_episodes data frame is  {exploded_episodes.count()}")
exploded_episodes.printSchema()

tabular_episodes = (exploded_episodes
                    .withColumn('season', F.col('episodes.season'))
                    .withColumn('number', F.col('episodes.number'))
                    .withColumn('name', F.col('episodes.name'))
                    .withColumn('airdate', F.col('episodes.airdate'))
                    .withColumn('summary', F.col('episodes.summary'))
                    .drop('episodes')
)

tabular_episodes.printSchema()
print(f"total number of records in tabular_episodes data frame is  {tabular_episodes.count()}")
tabular_episodes.show(truncate=False)
tabular_episodes.coalesce(1).write.mode('overwrite').csv("./episodes.csv", sep='|', quote=None)

