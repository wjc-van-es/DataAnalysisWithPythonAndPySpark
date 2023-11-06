<style>
body {
  font-family: "Gentium Basic", Cardo , "Linux Libertine o", "Palatino Linotype", Cambria, serif;
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
# Chapter 7 - Bilingual PySpark: Blending Python and SQL code

To explicitly tell the SparkSession to run locally call `.master("local")` on the `SparkSession.builder`
You can also specify how many cores you want to use: e.g. `.master("local[2]")` to use two cores.
```python
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("Chapter 7 example")
         .master("local")
         .config('spark.sql.debug.maxToStringFields', '50')
         .getOrCreate())
```
[https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.builder.master.html#pyspark.sql.SparkSession.builder.master](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.builder.master.html#pyspark.sql.SparkSession.builder.master)

## 7.2 Preparing a data frame for SQL
In [../src/Ch07/listing_7.1_7.2.py](../src/Ch07/listing_7.1_7.2.py) we see what happens when you try to execute an SQL
query on a data frame named elements and expect that there is a view or table available with the same name.
However, Spark SQL does not have visibility over the variables Python assigns, and you get `AnalysisException` thrown in
this first attempt.

Therefore, we need to register a data frame, before it can be queried via SQL. 
- The data frame method `createOrReplaceTempView('view_name')` will create a view named `'view_name'` that will be a 
  reference to the data of the data frame that can be used as reference in any SQL's `from` clause. 
  This `'view_name'` can be the same as the data frame Python variable name, but this isn't required.
- Now we can perform a SQL query with the `sql()` method of `pyspark.sql.SparkSession` where we refer to the registered
  `view_name`
- we can also check metadata from the `pyspark.sql.Catalog` typed `catalog` field of our current 
  `pyspark.sql.SparkSession` like
  - `spark.catalog.currentDatabase()`
  - `spark.catalog.listTables('default')` where `'default'` is the name returned by the previous call.

#### Summary code
```python
# elements is a data frame created by reading a csv file containing all elements from the periodic table 
elements.createOrReplaceTempView('elements')
print(f"After calling elements.createOrReplaceTempView('elements'):\n"
      f"spark.catalog.currentDatabase() returns {spark.catalog.currentDatabase()}\n"
      f"With the current database name being 'default' we want a list of its (temporary) tables with:\n"
      f"spark.catalog.listTables('default') returns:\n{spark.catalog.listTables('default')}")
spark.sql(
    '''
    select period, count(*) 
    from elements 
    where phase="liq" 
    group by period
    '''
).show(5)
```
See for the full code example: [../src/Ch07/listing_7.3_7.4.py](../src/Ch07/listing_7.3_7.4.py)

## 7.3 SQL and PySpark

## 7.4 Using SQL-like syntax within data frame methods

### 7.4.2 Grouping similar records together: group by and order by
- A `group by some_column` is quite simply aggregating all rows that have the exact same value for `some_column`.
- This means that _for all other columns you select you need_ an **aggregate function** for all the values of these 
  columns that will be aggregated into one row based on the same value of that other `some_column`.
- All these aggregate functions are part of the `pyspark.sql.functions` package, which needs to be imported
  when you use the PySpark Python code, but is implicitly available in a SQL query string.pyspark.sql.functions 
- A complete list of the aggregate functions can be found at
  [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#aggregate-functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html#aggregate-functions)
  some well known examples are:
  - `min()` minimum value of all the aggregated values of the column passed in as argument
  - `max()` maximum value of all the aggregated values of the column passed in as argument
  - `sum()` sum value of all the aggregated values of the column passed in as argument
  - `mean()` mean value of all the aggregated values of the column passed in as argument
  - `median()` mean value of all the aggregated values of the column passed in as argument
  - `count()` count of all the aggregated column values (this would be all aggregated rows)

### 7.4.3 Filtering after grouping using having
#### Using `having` in SQL and `where()` in PySpark
- **In SQL**, the `GROUP BY` clause should always come after the `WHERE` clause, therefore to add filtering conditions
  that need to be **applied to aggregate fields** cannot be added to the `WHERE` clause, but to a separate `HAVING` 
  clause that comes after the `GROUP BY` clause. Thus, `HAVING` can be thought of as a `WHERE` clause especially for 
  aggregate columns.
- **In PySpark**, there is _**no** need for a separate `having()` data frame method_, as each method simple returns a
  new data frame. Therefore, in Python code, simply use the `where()` data frame method whenever you should have used
  `HAVING` in SQL.

See the following code fragments for comparison
```python
import pyspark.sql.functions as F
...
spark.sql(
    """ SELECT
          model,
          min(capacity_bytes / pow(1024, 3)) min_GB,
          max(capacity_bytes/ pow(1024, 3)) max_GB
        FROM backblaze_stats_2019
        GROUP BY model
    HAVING min_GB != max_GB                     -- filtering on aggregate fields
    ORDER BY max_GB DESC"""
    ).show(5)
    
df_backblaze_2019.groupby(F.col("model")).agg(
    F.min(F.col("capacity_bytes") / F.pow(F.lit(1024), 3)).alias("min_GB"),
    F.max(F.col("capacity_bytes") / F.pow(F.lit(1024), 3)).alias("max_GB"),
).where(F.col("min_GB") != F.col("max_GB")      # for the same filtering the where() method can be used
).orderBy(
    F.col("max_GB"), ascending=False
).show(5)
```

### 7.4.4 Creating new tables/views using the CREATE keyword
- In SQL, we can create tables and views this can be used in Spark as well.
- Resulting views will be visible in `spark.catalog.listTables('default')` and usable in the `from` clause of SQL 
  queries.
- tabular result sets of SQL queries can be assigned to a variable in Python code of type `pyspark.sql.DataFrame`
- a scalar result type of SQL queries with a single aggregated result value can also be assigned to a variable of
  corresponding type
- see [../src/Ch07/listing_7.10.py](../src/Ch07/listing_7.10.py) and the code fragment underneath
```python
backblaze_2019.createOrReplaceTempView("drive_stats")
spark.sql(
  """
  CREATE OR REPLACE TEMP VIEW drive_days AS
  SELECT model, count(*) AS drive_days
  FROM drive_stats
  GROUP BY model"""
)
spark.sql(
  """CREATE OR REPLACE TEMP VIEW failures AS
  SELECT model, count(*) AS failures
  FROM drive_stats
  WHERE failure = 1
  GROUP BY model"""
)
print(
  f"""
  List tables in catalog after executing a SQL statements:\n
    'CREATE OR REPLACE TEMP VIEW drive_days ...' &\n
    'CREATE OR REPLACE TEMP VIEW failures ...'\n
    We expect both drive_days and failures to be in the list besides the drive_stats that was
    created with the DataFrame's createOrReplaceTempView() method. \n
    spark.catalog.listTables('default'):\n
    {spark.catalog.listTables('default')}
    """
)

# assigning a query result to a data frame.
drive_days_over_180_000 = spark.sql(
    '''
    select * 
    from drive_days
    where drive_days > 180000
    order by drive_days desc
    '''
)
drive_days_over_180_000.show(truncate=False)
print(f"There are {drive_days_over_180_000.count()} models with over 180_000 drive days.")
```

### 7.4.5 Adding data to our table using UNION and JOIN
We deviate from the path chosen in the book by reading all the csv files, which each represent 1 day of the year into
a data frame and so creating a list of 365 data frames. Then we need a way to combine these into a single data frame
containing all the data of a complete year.
[https://walkenho.github.io/merging-multiple-dataframes-in-pyspark/](https://walkenho.github.io/merging-multiple-dataframes-in-pyspark/)
explains how this can be done by  
- combining `pyspark.sql.Dataframe.unionAll()` 
- with `functools.reduce()`

#### Notes about `pyspark.sql.Dataframe.unionAll()` and `pyspark.sql.Dataframe.union()`
- `pyspark.sql.Dataframe.unionAll()` is typically used as `this_df.unionAll(other_df)`, which will return a new 
   data frame containing the union of rows in the this_df and other_df DataFrame objects.
- `pyspark.sql.Dataframe.union()` is an alias doing the exact same thing, which is confusing when you compare it to
  the respective SQL commands of the same name, which differ slightly in their behavior
  - the SQL command `UNION` automatically removes duplicate records, whilst `UNION ALL` does _NOT_
  - therefore `pyspark.sql.Dataframe.unionAll()` is more accurately descriptive as it behaves like SQL command 
    `UNION ALL` in keeping any duplicate records.
  - combine `unionAll()` with `distinct()` if you do want to remove duplicate records
- `pyspark.sql.Dataframe.unionAll()` does not re-sort columns, so when you apply the procedure described above, so make 
  sure that your dataframes have the same order of columns. We did this by applying our own schema as argument on the
  spark.read.csv() function call
- `pyspark.sql.Dataframe.unionAll()` can only union 2 data frames, that's where `functools.reduce()` comes in
- [https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unionAll.html#pyspark.sql.DataFrame.unionAll](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.unionAll.html#pyspark.sql.DataFrame.unionAll)

#### Notes about `functools.reduce()`
This function takes two arguments
- the first is a function
- the second is an iterable on whose elements the function can be performed

Or described with a bit more precision these steps are applied:
1. Apply a function (or callable) to the first two items in an iterable and generate a partial result.
1. Use that partial result, together with the third item in the iterable, to generate another partial result.
1. Repeat the process until the iterable is exhausted and then return a single cumulative value.

For a simple example of how this can be used:
[../src/Ch07/simple_reduce_example.py](../src/Ch07/simple_reduce_example.py)

See also [https://realpython.com/python-reduce-function/](https://realpython.com/python-reduce-function/)

#### Combining both `functools.reduce()` with `pyspark.sql.Dataframe.unionAll()` 
We see this at work in most of our listings of chapter 7 that involve the memory drives reliability investigation, e.g.
[../src/Ch07/listing_7.10.py](../src/Ch07/listing_7.10.py)

A code fragment with the most relevant bit:
```python
from functools import reduce
from pyspark.sql import DataFrame
...
# a list of 365 dataframes
# all_files is a list containing all file names
# schema is a predefined schema to force compliance of all data frames to have the same columns of the same type 
# in the same order
# the schema is also a subset of only the columns we're interested in to optimize the process
data = [
    spark.read.csv(os.path.join(data_dir, file), header=True, schema=schema, mode='PERMISSIVE')
    for file in all_files
]

merged_df = reduce(DataFrame.unionAll, data).dropna()
```
#### Joins
See also section 5.1 for all theory of joining tabular structures with the PySpark methods in 7.4.5 we see a short
example of joins in SQL syntax.

### 7.4.6 Organizing your SQL code better through subqueries and common table expressions

