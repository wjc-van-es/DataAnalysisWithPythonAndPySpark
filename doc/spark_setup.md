<style>
body {
  font-family: "Spectral", "Gentium Basic", Cardo , "Linux Libertine o", "Palatino Linotype", Cambria, serif;
  font-size: 100% !important;
  padding-right: 12%;
}
code {
  padding: 0.25em;
	
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

# How to get Python code to work with Spark

## Context
- For the python code to work it should have access to
- 

## Add a `project.env` file to the project root
- In it declare `JAVA_HOME=/absolute/path/to/root/of/java/installation`
- add any other environment variable you may need in your code

## Adding the `config_info` module
- located at [../src/project_utils/config_info.py](../src/project_utils/config_info.py)
- its function `load_env_file_when_present(file_name)` tries to find the `.env` file with the `file_name` argument
  starting in the same directory as the source file and moving up from there to subsequent parent dirs
- so when you set `'project.env'` as `file_name` argument it will find it and read its environment variables
- Add the following code as first initialization, to ensure the presence of a valid value for `JAVA_HOME` before any
  PySpark libraries are used in your code
  ```python
  import project_utils.config_info as ci

  # code that should be called before any PySpark dependencies
  ci.load_env_file_when_present('project.env')
  ```


