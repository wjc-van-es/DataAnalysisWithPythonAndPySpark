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

# The exercise 6.6 wants us to compare the tenure of the three shows by getting the difference of the airdate of their
# respective last and first episode.
# Our solution is a bit round about exploratory, but gets the job done and produces the same answers as the book's
# more succinct solution copied underneath.
df_episode_dates = df_three_shows.select(F.col('id'), F.col('name'),
                                         F.explode(F.col('_embedded.episodes.airdate')).alias('airdate'))
df_episode_dates.printSchema()
df_episode_dates.show(truncate=False)

df_min_max = (df_episode_dates.groupby(F.col('id'), F.col('name'))
              .agg(F.min(F.col('airdate')).alias('first'),
                   F.max(F.col('airdate')).alias('last'))
              .withColumn('duration in days', F.datediff(F.col('last'), F.col('first')))
              .orderBy('duration in days', ascending=False))
df_min_max.printSchema()
df_min_max.show(truncate=False)

df_min_max.printSchema()
df_min_max.show(truncate=False)

# More succinct solution from the book yields the same result:
# In descending order of tenure:
# The Golden Girls (2429 days), Breaking Bad (2079 days) and Silicon Valley (2072 days)
sol6_6 = df_three_shows.select(
    "name",
    F.array_min("_embedded.episodes.airdate").cast("date").alias("first"),
    F.array_max("_embedded.episodes.airdate").cast("date").alias("last"),
).select("name", (F.col("last") - F.col("first")).alias("tenure")).orderBy('tenure', ascending=False)
sol6_6.show(truncate=50)


