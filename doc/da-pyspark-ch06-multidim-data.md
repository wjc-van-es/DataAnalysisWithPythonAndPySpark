<style>
body {
  font-family: "Gentium Basic", Cardo, "Linux Libertine o", "Palatino Linotype", Cambria, serif;
  font-size: 130% !important;
}
code {
	padding: 0 .25em;
	
	white-space: pre;
	font-family: "Tlwg mono", Consolas, "Liberation Mono", Menlo, Courier, monospace;
	
	background-color: #ECFFFA;
	//border: 1px solid #ccc;
	//border-radius: 3px;
}

kbd {
	display: inline-block;
	padding: 3px 5px;
	font-family: "Tlwg mono", Consolas, "Liberation Mono", Menlo, Courier, monospace;
	line-height: 10px;
	color: #555;
	vertical-align: middle;
	background-color: #ECFFFA;
	border: solid 1px #ccc;
	border-bottom-color: #bbb;
	border-radius: 3px;
	box-shadow: inset 0 -1px 0 #bbb;
}

h1,h2,h3,h4,h5 {
  color: #269B7D; 
  font-family: "fira sans", "Latin Modern Sans", Calibri, "Trebuchet MS", sans-serif;
}
</style>
### JONATHAN RIOUX, ©2022 by Manning Publications Co. All rights reserved.
## Data Analysis with Python & PySpark
# Chapter 6: Multidimensional data frames: Using PySpark with JSON data
## Two-dimensional tabular data
Ingesting a csv file or a relational database view or table and representing it in a data frame is easy as they have the
same two-dimensional structure of rows or records with their attributes divided into separate columns. The column's
datatypes are usually simple scalars, like an integer, float, calendar date, text or boolean

## How to store complex hierarchical datastructures into a data frame?
- JSON (JavaScript Object Notation) can, in principle, contain layer upon layer of nested hierarchical data
  - e.g. a variable pointing to a list of objects containing a map of objects, containing (among many other attributes)
    a list of dates
- The key of transforming this complex hierarchy of data into a (PySpark) data frame is creating complex types for its
  columns.
- PySpark is already very helpful with this
  - It has three container structures available:
    - array
    - map
    - struct
  - When ingesting JSON file with a complex data structure the schema reader functionality works very well in 
    representing that data in a schema that uses the container structures mentioned above to translate to a dataframe
    with complex hierarchical column types
  - Then we are able to transform this into a dataframe that only contains the data we are interested in.
    - In this we could go as far as to flatten the data structure to a data frame with simple scalar column types
    - but often we do not have to go so far to end up with a usable data frame to analyse or represent a query result
   
## 6.1 Reading JSON data: Getting ready for the schemapocalypse

### 6.1.1 Analysing JSON and comparing it (and its parts) to Python data types
- each JSON file contains one object called the root object delimited with a starting `{` and closing `}` curly brace.
- its attributes, separated by a comma, have a name or key that must be of type string and a value, which gives it a 
  structure not unlike a python dictionary (or map)
  - the value of a JSON object can represent a view types
    - a simple scalar type,
      - Strings, which use double-quotes
      - Numbers
      - Booleans, true or false (not capitalized like in Python)
      - null, a null pointer object, akin to Python's None
    - another object delimited with a starting `{` and closing `}` curly brace, this way objects can be nested
    - an array delimited with a starting `[` and closing `]` square bracket, like a python's list
      - the array's elements can be of any type including objects and other arrays
- If you read a JSON file with the `json` package from the Python standard library and assigned to a variable its type
  would be dictionary, which makes sense.
  ```python
  import json
  sample_json = """{
     "id": 493,
     "name": "Star Trek: Deep Space Nine",
     "type": "Scripted",
     "language": "English",
     "genres": [
        "Action",
        "Adventure",
        "Science-Fiction"
     ],
     "network": {
        "id": 72,
        "name": "Syndication",
        "country": {
           "name": "United States",
           "code": "US",
           "timezone": "America/New_York"
        },
     "status": "Ended",
     "runtime": 60,
     "averageRuntime": 60,
     "premiered": "1993-01-03",
    "ended": "1999-06-02",
  }"""
  
  document = json.loads(sample_json)
  assert(type(document) is dict)
  ```

### 6.1.2 Going bigger: Reading JSON data in PySpark

- To read a json file into a dataframe you use the `pyspark.sql.DataFrameReader.json` function.
  - The only mandatory argument will be a str, list of RDD representing the path, list of paths or RDD of strings storing
    JSON content.
  - The default rule is *one JSON document, one line, one record*
    - a JSON file may contain only one record, stored in a single line.
  - When we want to read JSON files with a more easy to read multiline representation of a single record (which implies
    the JSON file will only hold a single record) we can use the `multiLine=True` argument.
    - This will change the rule to *one JSON document, one file, one record*
    - With the `multiLine=True` argument you can also use the glob pattern (using a * to refer to multiple files), 
      give the path to a directory and specify multiple JSON files in the path with `*.json` to ingest them as
      separate records into a singe data frame. Take care, however, that these multiple JSON files adhere to the same
      structure (the same schema can be inferred)
- See [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html#pyspark.sql.DataFrameReader.json](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html#pyspark.sql.DataFrameReader.json)
- For all optional parameters see
  [https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option)
- For an example see [../code/Ch06/listing_6.3_6.4.py](../code/Ch06/listing_6.3_6.4.py)

## 6.2 Breaking the second dimension with complex data types

- The hierarchical structure of a JSON document can be squeezed into the two-dimensional, tabular structure of a Spark
  data frame by letting the cells contain more than a single, scalar value.
- Instead, a cell may have a complex type that may contain a lot of other types.
  - these types are not complex in the Python sense of holding images, video or audio footage,
  - rather in Spark complex type is a synonym for container or compound type.
- The Spark complex types are
  - array
  - map
  - struct
- We will learn how to relate JSON object and array structures to the Spark complex types
- All the top level attributes become columns in the data frame with their key or name given to the column name

### 6.2.1 When you have more than one value: The array
- The PySpark array container type loosely compares to a Python list
  - as they both are _sequences_, they contain their elements in a deliberate order
- The main difference is that in PySpark arrays are always containers of values _of the same type_
  - although it is good practice to keep Python lists homogeneous as well (and use tuples to store heterogeneous elements)
    Python does not enforce this homogeneousness
  - PySpark will not raise an error if you try to read an array-type column with multiple types. Instead, it will 
    simply default to the lowest common denominator, usually the string. This way, you don’t lose any data, but you
    will get a surprise later if your code expects an array of another type.

#### Extracting elements from an array
- The data frame `df` has a column named `'genres'` of type array, and we wish to select only its first element
  assume this import statement: `import pyspark.sql.functions as F`
  
  | name           | code of `df.select()` parameters |
  |----------------|----------------------------------|
  | dot and index  | `df.genres[0]`                   |
  | col and index  | `F.col("genres")[0]`             |
  | dot and method | `df.genres.getItem(0)`           |
  | col and method | `F.col("genres").getItem(0)`     |
- In PySpark arrays you cannot use slicing with the brackets like with a Python list, so this:  ~~`df.genres[0:9]`~~ 
  cannot be done.
- PySpark is a thin layer of veneer over Spark (Java / Scala), which provides a consistent API across languages. This
  makes it less integrated with core Python capabilities.

### 6.2.2 The map type: Keys and values within a column
- a PySpark `map` is like a Python `dictionary`, but
  - all keys must be of the same type and cannot be `null`
  - all values must be of the same type and can be `null`
- Maps are less common as column type than `array`; reading a JSON document won't yield columns of type `map`, because
  JSON objects are not enforced to comply to the same type keys and same type values rule.
- with the `map_from_arrays()` function you can create a `map` typed column from two `array` type columns

## 6.3 The struct: Nesting columns within columns
- Like a JSON object
  - the key or name of each pair is a string,
  - the value of each pair can be of a different type.
- The number of fields and their names are fixed (i.e. known ahead of {run}time),
  - unlike arrays and maps, which have a free, variable size of elements (albeit of the same type)
- Conceptually it is convenient to think of a struct column type as a column that contains a data frame within each of
  its cells.
- Structs can contain fields that are of different type including `array` and `struct` type. Also, arrays can contain
  elements of type `struct`. 
  - Hence, nesting `struct` type fields and array elements we can create a deep hierarchy of data

### 6.3.1 Navigating structs as if they were nested columns
- we can refer to fields within a struct, the same way we can refer to columns of a data frame with dot notation
- so promoting the episodes `array[struct]` field within the `_embedded` `struct` column as new separate column whilst
  discarding the `_embedded` column goes as follows:
  ```python
  import pyspark.sql.functions as F
  ...
  shows_clean = shows.withColumn(
     "episodes", F.col("_embedded.episodes")
  ).drop("_embedded")
  ```
- We can select a single string field from a `array[struct]` type column (an array of struct type elements) to create a
  column from this that will be of type `array[string]`.
- In our example we have a column named 'episodes' of type `array[struct]` and one string typed field is named 'name'
  ```python
  episodes_name = shows_clean.select(F.col("episodes.name"))
  episodes_name.printSchema()
  
  # root
  # |-- name: array (nullable = true)
  # |    | -- element: string (containsNull = true)
  ```
- we could go on exploding this resulting column to go from a data frame with a single record holding an `array[string]`
  type column to a multi-record data frame with `string` type column, which has a record for each element in the
  previous array, in a single nested statement this would become:
  ```python
  episode_names = shows_clean.select(F.explode(F.col('episodes.name')).alias('name'))
  ```
- see for a more involved example 
  [../code/Ch06/listing_6.14_6.15_create_tabular_episodes.py](../code/Ch06/listing_6.14_6.15_create_tabular_episodes.py)

## 6.4 Building and using the data frame schema
Up until this point we have used the schema that Spark infers for us from the data it has ingested into a data frame.
It is also possible, however, to define a schema that our ingested data should adhere to. 
One advantage over Spark inferred schemas is performance: as Spark needs to read the data twice to infer its schema
- once to infer the schema and
- once more to read the data itself

As we can think of a struct column as a data frame nested inside that column, we can think of any data frame as a
single struct entity with its columns as top-level fields of the implicit struct called 'root'.

There are two syntaxes to create a schema in Spark:
- an explicit, programmatic one (reviewed in the next section)
- a DDL-style schema covered in chapter 7.

You often would provide a **reduced schema**, which means you only define a subset of all the available fields. 
PySpark will only read the fields you have defines, which means
- a further reduction of processing time
- usually a much simpler subset of the entire datastructure, making the resulting data frame easier to manipulate.

### 6.4.1 Using Spark types as the base blocks of a schema
- all types derive from the `pyspark.sql.types` module, which can be imported as `import pyspark.sql.types as T` where
  the capital `T` is commonly used by convention
- The module contains a lot of types:
  - Simple value types that usually have a constructor without any arguments
    - `T.DateType()`
    - `T.StringType()`
    - `T.LongType()`
    - `T.DecimalType(precision, scale)`
  - Complex types
    - The `ArrayType`, where you also have to specify the type of its elements as constructor parameter, e.g. 
      - `T.ArrayType(T.StringType())` or 
      - `T.ArrayType(T.DateType())`
    - The `MapType`, where you specify the types of its keys and values as cosntructor parameters. e.g.
      - `T.MapType(T.StringType(), T.LongType())`
    - The `T.StructType()`, to define the data frame root and any nested structs
      - This constructor takes a list of `T.StructFields()`, whose constructor in turn takes
        - a name and type argument
        - an optional nullable key parameter, which defaults to `True`
        - an optional `metadata` key parameter of type `dict`

#### A summary example of the definition of a reduced schema
To see all this in a code example of the definition of a reduced schema of show data ingested from the _TVMaze REST API_
e.g. [https://api.tvmaze.com/singlesearch/shows?q=%22Star%20Trek:%20Deep%20Space%20Nine%22&embed=episodes](https://api.tvmaze.com/singlesearch/shows?q=%22Star%20Trek:%20Deep%20Space%20Nine%22&embed=episodes)
```python
import pyspark.sql.types as T

# a reduced schema of the episode struct, containing only the fields of interest
# applied later as the element-type of a nested array (see the reduced_show_schema variable below)
episode_schema = T.StructType(
    [
        T.StructField("airdate", T.DateType()),
        T.StructField("id", T.StringType()),
        T.StructField("name", T.StringType()),
        T.StructField("number", T.LongType()),
        T.StructField("season", T.LongType()),
    ]
)

# a reduced schema definition applied to the ingested data,
# corresponding to the top-level (root) of the resulting data frame,
# only containing the fields (columns) we are interested in
reduced_show_schema = T.StructType(
    [
        T.StructField("id", T.StringType()),
        T.StructField("name", T.StringType()),
        T.StructField(
            "_embedded",
            T.StructType(
                [
                    T.StructField(
                        # here we apply the StructType defined earlier and assigned to episode_schema variable to become
                        # the type of the elements of the array
                        "episodes", T.ArrayType(episode_schema) 
                    )
                ]
            )
        )
    ]
)

```
### 6.4.2 Reading a JSON document with a strict schema in place
- With the `pyspark.sql.DataFrameReader.json` function available from the `DataFrameReader` attribute in 
  `pyspark.sql.SparkSession.read` we can read a json document
- See [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html#pyspark.sql.DataFrameReader.json](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.json.html#pyspark.sql.DataFrameReader.json)
  - With the optional keyword parameter `schema` we can specify the schema we defined ourselves
  - With the keyword parameter `mode='FAILFAST'` set the `SateFrameReader` will throw an Exception as soon as it 
    encounters a part of the document that is incompatible with the schema we declared.
  - We also set the optional keyword parameter `multiline=True`
- For all optional parameters see
  [https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option)
```python
import os
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Chapter 6 example").getOrCreate()
spark.sparkContext.setLogLevel("WARN")
data_dir = "../../data/shows"
df_sil_val = spark.read.json(os.path.join(data_dir, 'shows-silicon-valley.json'), multiLine=True,
                             schema=reduced_show_schema, mode='FAILFAST')
```
See for a complete example [../code/Ch06/listing_6.17_6.18_6.19.py](../code/Ch06/listing_6.17_6.18_6.19.py)
here we have defined a whole schema to use for the show data, and we use `pyspark.sql.types.DateType` and
`pyspark.sql.types.TimestampType` assuming the fields comply to the ISO-8601 standard.
If the formatting deviates from this standard you need to pass the right format as pattern to `dateFormat` or 
`timestampFormat` [https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)

When you try to parse a JSON document with fields missing you will still be good when these fields are optional, as
they are by default. If you substitute a `LongType` for a field that is suposed to be a `StringType`, like the 'summary'
field, there is a type mismatch, and you will get an Exception:
`org.apache.spark.SparkException: [MALFORMED_RECORD_IN_PARSING] Malformed records are detected in record parsing: [null].`
If you scroll down the long stacktrace you will find more descriptive information
`Caused by: org.apache.spark.SparkRuntimeException: [CANNOT_PARSE_JSON_FIELD] Cannot parse the field name 'summary' and 
the value <p>Attending an elaborate launch party, Richard and his computer programmer friends - Big Head, Dinesh and 
Gilfoyle - dream of making it big. Instead, they're living in the communal Hacker Hostel owned by former programmer 
Erlich, who gets to claim ten percent of anything they invent there. When it becomes clear that Richard has developed a 
powerful compression algorithm for his website, Pied Piper, he finds himself courted by Gavin Belson, his egomaniacal 
corporate boss, who offers a $10 million buyout by his firm, Hooli. But Richard holds back when well-known investor 
Peter Gregory makes a counteroffer.</p> of the JSON token type VALUE_STRING to target Spark data type "BIGINT".`

[../code/Ch06/exo_6.7.py](../code/Ch06/exo_6.7.py)

### 6.4.3 Going full circle: Specifying your schemas in JSON

## 6.5 Putting it all together: Reducing duplicate data with complex data types
