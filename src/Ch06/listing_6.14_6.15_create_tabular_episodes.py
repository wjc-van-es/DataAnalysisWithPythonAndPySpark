import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

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
# df_shows = spark.read.json(os.path.join(data_dir, 'shows-silicon-valley.json'), multiLine=True)
df_shows = spark.read.json(os.path.join(data_dir, '493-ds9.json'), multiLine=True)

# you have one record, where each column is a field on the highest level under the document root
# hence these columns can have simple values when the corresponding field is a simple scalar type or
# a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
# objects or arrays)
print(f"total number of records in df_shows data frame is  {df_shows.count()}")
df_shows.printSchema()
df_shows.show()

shows_clean = df_shows.withColumn(
    "episodes", F.col("_embedded.episodes")
).drop("_embedded")

shows_clean.printSchema()

# the episodes column of the shows_clean data frame is of type array[struct] an array that contains struct items, all
# contained in single cell
# when we explode the shows_clean.'episodes' column into a new column of a new data episodes.'episodes' then this
# will result in a data frame episodes with a single column episodes of type struct where all items in the
# array are now separate rows of the new data frame
episodes = shows_clean.select(F.explode(F.col('episodes')).alias('episodes'))
episodes.printSchema()

print(f"total number of records in episodes data frame is  {episodes.count()}")

# Now take all attributes of interest from the episodes column struct and put them in separate columns, then drop the
# episodes column
tabular_episodes = (episodes
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
tabular_episodes.coalesce(1).write.mode('overwrite').csv("./493-ds9-episodes.csv", sep='|', quote=None)
