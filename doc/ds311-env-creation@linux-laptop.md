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

# Recreation of the conda ds311 environment on linux-laptop

## Context
We installed Anaconda on willem-Latitude-5590 and created an environment that would be an upgrade from the old dasci
- python 3.11
- pyspark 3.4 to be compatible with the SDKman Apache Spark 3.4.0 installation
- latest jupyter notebook
- latest matplotlib

We had some difficulties on linux-laptop in the past with finding all the environment variables and SDKman installed
and managed Apache Spark in particular. We solved this by forcefully setting the SPARK_HOME and PATH in `~/.bashrc`
and again `PATH` in conda's `dasci` environment. This has made the configuration brittle and unresponsive to management
by SDKMan.

Maybe we could have solved this by a timely `source ~/.bashrc` after an installation changed it or a timely
`conda activate dasci` after something changed in its package configuration. 

Whatever the case, we now see on willem-Latitude-5590 that the JAVA_HOME, SPARK_HOME and PATH work fine within the 
`ds311` conda environment and that SDKMan management of Java and Spark installed versions also works fine and guarantees
for per session runtime flexibility.

The difference between the willem-Latitude-5590 and linux-laptop `~/.bshrc` is that the latter has 3 additional 
statements:

```bash
# export $(go env GOPATH)/bin to be added to the PATH environment variable
export PATH="$PATH:$HOME/go/bin"

export SPARK_HOME="$HOME/.sdkman/candidates/spark/3.3.1"
export PATH="$PATH:$HOME/.sdkman/candidates/spark/3.3.1/bin"

```
we should remove the last two statements and trust that the SDKMan's flexible `$HOME/.sdkman/candidates/spark/current`
configuration for SPARK_HOME should be used in every situation.

## Steps
- removing `SPARK_HOME` and `PATH` export statements from `~/.bashrc`
- `source ~/.bashrc` didn´t work with current terminal even after `conda deactivate` in a new terminal, however, all 
  environment variables pointed to the right paths.
- `conda create -n ds311`
- `conda activate ds311`
- The environment is completely devoid of packages it hasn't even got a python version installed (derived from base)
  ```bash
  (ds311) willem@linux-laptop:~$ conda list -n ds311
    # packages in environment at /home/willem/anaconda3/envs/ds311:
    #
    # Name                    Version                   Build  Channel
    (ds311) willem@linux-laptop:~$ python --version
    Command 'python' not found, did you mean:
    command 'python3' from deb python3
    command 'python' from deb python-is-python3
  ```
- Installing python 3.11 with `conda install -n ds311 python=3.11`
- Now the python command was available:
  ```bash
  (ds311) willem@linux-laptop:~$ python --version
  Python 3.11.5                                                                                                                                         
  (ds311) willem@linux-laptop:~$ which python
  /home/willem/anaconda3/envs/ds311/bin/python
  ```
- Installing PySpark with `conda install -n ds311 pyspark`
- pyspark 3.4.1 was installed together with some thirty transitive dependencies among which pandas 2.0.3 & numpy 1.26.0
- we refreshed the environment with `conda activate ds311`
- Installing jupyter notebook with
  - `conda install -n ds311 notebook`
  - `conda activate ds311`
  - `conda install -n ds311 -c conda-forge nb_conda_kernels`
  - `conda activate ds311`
- Installing matplotlib with `conda install -n ds311 matplotlib`
- we refreshed the environment with `conda activate ds311`
- conda env export --no-builds > ds311_env_linux-laptop_no-builds.yml
- See if any updates are possible already with `conda update -n ds311 all`, most important change:
  ```bash
  The following packages will be SUPERSEDED by a higher-priority channel:

  nb_conda_kernels   conda-forge::nb_conda_kernels-2.3.1-p~ --> pkgs/main::nb_conda_kernels-2.3.1-py311h06a4308_0
  ```
- `conda activate ds311`
- `conda env export --no-builds > ds311_env_linux-laptop_no-builds_after-update_--all.yml`
- `conda update -n ds311 --all --no-pin` yielded no possible new updates
- `conda update -n base --all --no-pin` yielded 4 new packages, 2 updates and 2 downgrades

## references
- The whole session is saved to 
  [ds311-conda-env-creation-+-conda-update-session.txt](../../../Documents/sysAdmin-linux-laptop/Python/ds311-conda-env-creation-+-conda-update-session.txt)
- [https://github.com/wjc-van-es/da-pyspark-examples/blob/master/readme.md](https://github.com/wjc-van-es/da-pyspark-examples/blob/master/readme.md)
- [https://towardsdatascience.com/how-to-set-up-anaconda-and-jupyter-notebook-the-right-way-de3b7623ea4a](https://towardsdatascience.com/how-to-set-up-anaconda-and-jupyter-notebook-the-right-way-de3b7623ea4a)
- [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)