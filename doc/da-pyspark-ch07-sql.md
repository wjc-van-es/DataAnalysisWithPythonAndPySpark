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

Therefore, we need to register a data frame, before it can be queried via SQL. The data frame method 
`createOrReplaceTempView('view_name')` will create a view named `'view_name'` that will be a reference to the data of
the data frame that can be used as reference in any SQL's `from view_name` clause. This `'view_name'` can be the same as
the data frame Python variable name, but this isn't required.
```python
# elements is a data frame created by reading a csv file containing all elements from the periodic table 
elements.createOrReplaceTempView('elements')
```
See [../src/Ch07/listing_7.3_7.4.py](../src/Ch07/listing_7.3_7.4.py)
