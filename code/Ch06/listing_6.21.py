import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pprint

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

data_dir = "../../data/shows"

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
df_sil_val = spark.read.json(os.path.join(data_dir, 'shows-silicon-valley.json'), multiLine=True)

# you have one record, where each column is a field on the highest level under the document root
# hence these columns can have simple values when the corresponding field is a simple scalar type or
# a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
# objects or arrays)
print(f"total number of records in df_sil_val data frame is  {df_sil_val.count()}")

df_sil_val.printSchema()

df_sil_val.show()

df_episodes = exploded_episodes = (df_sil_val.select(
                        F.col("_embedded.episodes")
                    ).alias('episodes')
)

pprint.pprint(df_episodes.schema.jsonValue())
pprint.pprint(df_episodes.schema.json())

pprint.pprint(df_episodes.select(F.col('episodes.summary')).alias('summary').schema.jsonValue())
pprint.pprint(df_episodes.select(F.col('episodes.summary')).alias('summary').schema.json())
