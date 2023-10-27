import os
from pyspark.sql import SparkSession
import pyspark.sql.types as T
import pyspark.sql.functions as F

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

# now we read all 3 json files into one dataframe
# besides the shows-silicon-valley.json with multiline indented reformatting treatment we have 2 others that remain
# single line, but by setting multiLine=True we also interpret each new file as separated complete JSON document, which
# will be represented as a separate record in the dataframe following the
# "One JSON document, one file, one (df) record" rule.
# Beware, this will only work as long as all JSON document follow the same schema (as they are being retrieved from
# the same REST API, with a GET request query of the same format
df_three_shows = spark.read.json(os.path.join(data_dir, '*.json'), multiLine=True, schema=summary_schema,
                                 mode='FAILFAST')

print(f"total number of records in df_three_shows data frame is  {df_three_shows.count()}")
df_three_shows.printSchema()
df_three_shows.show(truncate=False)

# The exercise 6.7 wants us to extract the air date and name of each episode in two array columns.
# We also include the id and the name of the show
df_sol_6_7 = df_three_shows.select(F.col('id'),
                      F.col('name'),
                      F.col('_embedded.episodes.name').alias('episode name'),
                      F.col('_embedded.episodes.airdate').alias('episode airdate'),)

df_sol_6_7.printSchema()
df_sol_6_7.show(truncate=False)