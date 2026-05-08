<style>
body {
  font-family: "Spectral", "Gentium Basic", Cardo , "Linux Libertine o", "Palatino Linotype", Cambria, serif;
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


# Data Analysis with Python and PySpark

This is the companion repository for the _Data Analysis with Python and PySpark_
book (Manning, 2022). It contains the source
code and data download scripts, when pertinent.

## NEW (June 2025): Databricks Free

With Databricks offering [free access](https://www.databricks.com/blog/introducing-databricks-free-edition) of most important functionalities, you can now avoid installing (and paying) for your own version. I've created [a notebook/file](DownloadsDatabricksFree.py) you can use to get all the data in tables and volumes. Five minutes and you're ready to work through the code examples, no fuss!

Just clone the repository in databricks and open the data download notebook.

## Get the data (old version, still works)

The complete data set for the book hovers at around ~1GB. Because of this, [I
moved the data sources to another repository](
https://github.com/jonesberg/DataAnalysisWithPythonAndPySpark-Data) to
avoid cloning a gigantic repository just to get the code. The book assumes the data is under
`./data`.

## Mistakes or omissions

If you encounter mistakes in the book manuscript (including the printed source
code), please use the Manning platform to provide feedback.

---
### Note on relative paths and program execution
When I execute a `*.py` file in my PyCharm IDE it has the directory containing that file as the root of the execution.

Therefore, the root of execution would be `~/git/DataAnalysisWithPythonAndPySpark/code/Chxx` in my configuration.
The book, however, assumes the root of the project `~/git/DataAnalysisWithPythonAndPySpark` to be the root of the
execution.

Hence, we change the relative path to a data resource from
`./data/$specific_data_dir` to `../../data/$specific_data_dir`.

e.g. in [src/Ch04/checkpoint.py](src/Ch04/checkpoint.py)
```python
DIRECTORY = "../../data/broadcast_logs"
```
instead of
```python
DIRECTORY = "./data/broadcast_logs"
```

and whenever we want to execute a `*.py` file from the bash terminal, we go into the directory, which contains the
python file, e.g.:
```bash
~/git/DataAnalysisWithPythonAndPySpark$ cd src/Ch04
~/git/DataAnalysisWithPythonAndPySpark/src/Ch04$ spark-submit ./checkpoint.py
```

---
