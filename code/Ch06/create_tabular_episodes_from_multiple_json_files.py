import glob
import os
from pprint import pprint

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

data_dir = "../../data/shows"


def create_df(file_path):
    # The original json document was a single line and this is the PySpark default rule of:
    # "One JSON document, one line, one (df) record",
    # where multiple JSON docs / df records can fit in one file
    # each on a new line. This is set by the optional parameter multiLine, which has a default of False
    #
    # We already went exploring and ordered the PyCharm IDE to reformat the code, so we get an indented multiline
    # JSON document, which is much easier to read.
    # When we print the schema we now get
    # root
    #  |-- _corrupt_record: string (nullable = true)
    # However, if we set the optional multiline parameter to True it will be able to load the multiline document, which now
    # follow the adapted PySpark rule of
    # "one JSON document, one file, one (df) record"
    df_show = spark.read.json(file_path, multiLine=True)

    # you have one record, where each column is a field on the highest level under the document root
    # hence these columns can have simple values when the corresponding field is a simple scalar type or
    # a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
    # objects or arrays)
    print(f"total number of records in df_shows data frame is  {df_show.count()}")
    # df_show.printSchema()
    # df_show.show()
    return df_show


def create_files_list(dir_path, file_name_pattern):
    return glob.glob(os.path.join(dir_path, file_name_pattern))


def create_tabular_from_shows(df_shows):
    shows_clean = df_shows.withColumn(
        "episodes", F.col("_embedded.episodes")
    ).drop("_embedded")

    shows_clean.printSchema()

    name = shows_clean.select('name').collect()[0][0]
    print(f"df name = {name}")
    # show_name = shows_clean.
    # explode the episodes column, which contains struct items
    episodes = (shows_clean.select(F.explode(F.col('episodes')).alias('episodes'))
                .withColumn('show', F.lit(name)))
    episodes.printSchema()

    print(f"total number of records in episodes data frame is  {episodes.count()}")

    # Now take all attributes of interest from the episodes column struct and put them in separate columns, then drop
    # the episodes column
    tabular_episodes = (episodes
                        .withColumn('show', F.col('show'))
                        .withColumn('season', F.col('episodes.season'))
                        .withColumn('number', F.col('episodes.number'))
                        .withColumn('name', F.col('episodes.name'))
                        .withColumn('airdate', F.col('episodes.airdate'))
                        .withColumn('summary', F.col('episodes.summary'))
                        .drop('episodes')
                        )
    tabular_episodes.printSchema()

    return tabular_episodes


data_files_list = create_files_list(data_dir, "*.json")


for file in data_files_list:
    cleaned_up_df = create_tabular_from_shows(create_df(file))
    show_name = cleaned_up_df.select('show').collect()[0][0].replace(" ", "_").replace(":", "-")
    pprint(show_name)
    cleaned_up_df.coalesce(1).write.mode('overwrite').csv(f"./{show_name}.csv", sep='|', quote=None)

if __name__ == "__main__":
    pass
