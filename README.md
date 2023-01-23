# Data Analysis with Python and PySpark

This is the companion repository for the _Data Analysis with Python and PySpark_
book (Manning, 2022). It contains the source
code and data download scripts, when pertinent.

## Get the data

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

e.g. in [code/Ch04/checkpoint.py](code/Ch04/checkpoint.py)
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
~/git/DataAnalysisWithPythonAndPySpark$ cd code/Ch04
~/git/DataAnalysisWithPythonAndPySpark/code/Ch04$ spark-submit ./checkpoint.py
```

---
