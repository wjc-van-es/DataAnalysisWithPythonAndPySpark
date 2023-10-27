import os
import json
from pyspark.sql import SparkSession
import pyspark.sql.types as T
import pprint


spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# we load a json data file and derive a json formatted multidimensional schema string from it that we write into
# a file.
# Then we demonstrate how to reuse the json formatted schema string or file to derive a StructType schema object from it
# which then can be used as explicit schema in reloading the data from file into a new data frame object.
# See also https://gist.github.com/mrchristine/027d43cdbecdb363f0f36b0115cf9f1e
#
# Furthermore, a json formatted multidimensional spark schema IS NOT THE SAME as a json schema that we derived from
# the src/Ch06/json_show_samples/data_samples/sv_episodes.json file with
# https://www.liquid-technologies.com/online-json-to-schema-converter
# and wrote into src/Ch06/json_show_samples/json_schemas/tvmaze_episodes_schema.json
# The content of src/Ch06/json_show_samples/data_samples/sv_episodes.json could be validated with the content of
# src/Ch06/json_show_samples/json_schemas/tvmaze_episodes_schema.json with
# https://www.jsonschemavalidator.net/

data_dir = "json_show_samples/data_samples"
schemas_dir = "json_show_samples/spark_schemas_as_json"

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
df_sv_episodes = spark.read.json(os.path.join(data_dir, 'sv_episodes.json'), multiLine=True)

# you have one record, where each column is a field on the highest level under the document root
# hence these columns can have simple values when the corresponding field is a simple scalar type or
# a hierarchy of nested dataframes when the corresponding field is an object or array (which may in turn contain
# objects or arrays)
print(f"total number of records in df_sv_episodes data frame is  {df_sv_episodes.count()}")

df_sv_episodes.printSchema()

df_sv_episodes.show(truncate=False)

# a string variable with a json representation of the derived multidimensional schema of the
# df_sv_episodes
episodes_schema_json = df_sv_episodes.schema.json()

# Writing the json representation of the derived multidimensional schema into a file
with open(os.path.join(schemas_dir, 'episodes_spark_schema.json'), 'w') as file:
    file.write(episodes_schema_json)

# creating a schema structType object from the string json format representation of the schema
episodes_schema = T.StructType.fromJson(json.loads(episodes_schema_json))

# alternatively, the json formatted schema could have been read from the file
# with open(os.path.join(schemas_dir, 'episodes_spark_schema.json'), 'r') as content_file:
#     reloaded_schema_json = content_file.read()
#
# episodes_schema = T.StructType.fromJson(json.loads(reloaded_schema_json))

# read the data again into a data frame with the explicit multidimensional schema structType object, which was
# derived from the json formatted schema string
# The mode='FAILFAST' will immediately expose any mismatch of the data with the schema
df_sv_episodes_validated = spark.read.json(os.path.join(data_dir, 'sv_episodes.json'), multiLine=True,
                                           schema=episodes_schema, mode='FAILFAST')

df_sv_episodes_validated.printSchema()

# superfluous assertion that the data frame's internal schema equals to the imposed schema
assert df_sv_episodes_validated.schema == episodes_schema

# Rereading the original sv_episodes.json into a dataframe checking with our derived schema
pprint.pprint(episodes_schema_json)


