import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import project_utils.config_info as ci


ci.print_environment()
ci.check_path()

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
df_sil_val = spark.read.json(os.path.join(data_dir, 'shows-silicon-valley.json'), multiLine=True)

# you have one record, where each column is a field on the highest level under the document root
# hence these columns can have simple values when the corresponding field is a simple scalar type or
# a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
# objects or arrays)
print(f"total number of records in df_sil_val data frame is  {df_sil_val.count()}")

df_sil_val.printSchema()

df_sil_val.show()

# We build a map from two arrays, the first would provide the keys and the second the values

df_episode_ids_names = df_sil_val.select(
    F.map_from_arrays(F.col("_embedded.episodes.id"),
                      F.col("_embedded.episodes.name")).alias("col_episode_id_name")
    )

df_episode_ids_names.printSchema()
df_episode_ids_names.show(truncate=False)

df_expl_episode_ids_names = df_episode_ids_names.select(
    F.posexplode("col_episode_id_name").alias("position", "id", "name")
)

df_expl_episode_ids_names.printSchema()
df_expl_episode_ids_names.show(truncate=False)
