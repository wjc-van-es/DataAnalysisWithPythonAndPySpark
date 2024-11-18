<style>
body {
  font-family: "Gentium Basic", Cardo , "Linux Libertine o", "Palatino Linotype", Cambria, serif;
  font-size: 100% !important;
  padding-right: 12%;
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

# Q & A
- **Q**: Do I need to clean up a Spark Session after it has done all necessary jobs?
- **A**: The session will be closed if the spark object gets destroyed or if the script exits. So you shouldn't need to 
  worry about "dangling connections" or anything like that.
  (That's why all the code samples don't bother with closing the session by calling `spark.stop()`, because the script 
  has ended anyway)

  However, if you have a bunch of non-spark work that you want to do at the end of the script, it may still be a good
  idea to stop the session early to avoid holding that connection open.

  Note that you can use the SparkSession object as a context manager using the `with` keyword to automatically stop it 
  at the end of a scope:

  ```python
  from pyspark.sql import SparkSession
  
  with SparkSession.builder.appName("NewSpark").getOrCreate() as spark:
      # do stuff
      # ...
  
  # spark.stop() gets called automatically here
  ```
  - [https://stackoverflow.com/questions/69773515/do-i-need-to-stop-spark-after-creating-sparksession-using-pyspark](https://stackoverflow.com/questions/69773515/do-i-need-to-stop-spark-after-creating-sparksession-using-pyspark)
- 