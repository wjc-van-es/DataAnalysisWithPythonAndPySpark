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

