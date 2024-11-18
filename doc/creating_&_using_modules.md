<style>
body {
  font-family: "Gentium Basic", Cardo, "Linux Libertine o", "Palatino Linotype", Cambria, serif;
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

# Creating and using Python modules

## Configuration
- Within this project root we have a src directory located at `~/git/DataAnalysisWithPythonAndPySpark/src`
- Within that we have a separate directories with python scripts we can run all named `Chxx` where th xx varies for each
  chapter number. e.g. `~/git/DataAnalysisWithPythonAndPySpark/src/Ch06`
- We have a module directory `~/git/DataAnalysisWithPythonAndPySpark/src/project_utils` that contains
  - an empty `__init__.py` file to mark it as a module directory
  - a file named `config_info.py` that contains two function definitions `print_environment` and `check_path`
- To be able to run everything inside PyCharm `~/git/DataAnalysisWithPythonAndPySpark/src` is marked as _Sources Root_

## Importing the `project_utils.config_info` module in another python script file
- add at the top of the python script file either 
  - `import project_utils.config_info as ci` or 
  - `from project_utils import config_info as ci`
- Now you can both its available functions with
  - `ci.print_environment()` and
  - `ci.check_path()` respectively
- e.g.
  - [../src/Ch06/listing_6.24_6.26.py](../src/Ch06/listing_6.24_6.26.py)
  - [../src/Ch06/listing_6.25.py](../src/Ch06/listing_6.25.py)
  - [../src/bankstatements/df_prep.py](../src/bankstatements/df_prep.py)
  - [../src/bankstatements/pyspark_test.py](../src/bankstatements/pyspark_test.py)

## Running a script with the imported module

### In PySpark
Running a script that has imported the module using the PySpark Run / Debug Configurations doesn't need any further
configuration as long both the dir with the script as the dir with the imported module are both subdirectories of 
a directory marked as _Sources Root_, which is `~/git/DataAnalysisWithPythonAndPySpark/src` in our example.

### On the commandline
If we try to run it in a commandline terminal we also need to set the PYTHONPATH environment variable
to the directory we marked as the _Sources Root_ `~/git/DataAnalysisWithPythonAndPySpark/src`. This may be done
as relative path, e.g.
```bash
(ds311) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/src/Ch06$ PYTHONPATH=../ python listing_6.24_6.26.py
(ds311) willem@willem-Latitude-5590:~/git/DataAnalysisWithPythonAndPySpark/src/Ch07$ PYTHONPATH=../ ./more_periodic_table.py
```
or as absolute path, e.g.
```bash
(ds311) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/src/Ch06$ PYTHONPATH=~/git/DataAnalysisWithPythonAndPySpark/src/ python listing_6.24_6.26.py
```

### In a jupyter notebook
```python
import sys
sys.path.append("/home/willem/git/DataAnalysisWithPythonAndPySpark/src/")
from project_utils import config_info as ci

ci.print_environment()
ci.check_path()
```
- For environment variables created in `~/.bashrc` to be visible within the jupyter notebook the declarations
  `export ENV_NAME="value"` should be made after the conda initialize statements for them to be visible within
  a jupyter notebook.
- For a python script executed from the commandline (the previous section) this exact location of the placement wasn't
  necessary
- [https://stackoverflow.com/questions/68572852/import-local-modules-in-jupyter-notebook](https://stackoverflow.com/questions/68572852/import-local-modules-in-jupyter-notebook)

## References
- [https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files](https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files)
- [https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script](https://stackoverflow.com/questions/28705029/pycharm-error-no-module-when-trying-to-import-own-module-python-script)
- [https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run](https://stackoverflow.com/questions/4580101/python-add-pythonpath-during-command-line-module-run)
- [https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)
- [https://docs.python.org/3/using/cmdline.html](https://docs.python.org/3/using/cmdline.html)
- [https://docs.python.org/3/tutorial/modules.html](https://docs.python.org/3/tutorial/modules.html)