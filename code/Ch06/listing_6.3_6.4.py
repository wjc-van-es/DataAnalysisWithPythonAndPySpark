import os
from pyspark.sql import SparkSession

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

# now we read all 3 json files into one dataframe
# besides the shows-silicon-valley.json with multiline indented reformatting treatment we have 2 others that remain
# single line, but by setting multiLine=True we also interpret each new file as separated complete JSON document, which
# will be represented as a separate record in the dataframe following the
# "One JSON document, one file, one (df) record" rule.
# Beware, this will only work as long as all JSON document follow the same schema (as they are being retrieved from
# the same REST API, with a GET request query of the same format
df_three_shows = spark.read.json(os.path.join(data_dir, '*.json'), multiLine=True)

print(f"total number of records in df_three_shows data frame is  {df_three_shows.count()}")
df_three_shows.printSchema()
df_three_shows.show()