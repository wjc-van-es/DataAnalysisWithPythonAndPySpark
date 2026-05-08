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

# Anaconda maintenance strategy

## Context
Every once in a while we would like to upgrade or system to keep everything up to date in this way discern three layers:
1. The version of conda itself, to keep the management of all environments reliable and stable
2. The version of python itself, which it at the core of all code execution and where all other packages relate to
3. The specific packages our project code depends on.

## Principles
- We keep (Ana)conda iteself up to date on a regular basis, this only is concerned with the default base environment.
- We keep the base environment as bare as possible as its main purpose is to do the management of all other environments:
  - Only updates of conda itself are done on the base environment.
  - No specific extra packages are installed in base.
  - No python updates will be necessary in the base environment, conda will continue to manage fine with older versions
    of python.
- For each (group of related) project(s) we define a new environment on which we install all the packages we need
- For every project environment we can do regular package updates.
- If we want to increase the python version for a specific project environment it is usually best to create a 
  new environment with the desired python version and then reinstall all required packages.
  - We usually have part of the environment name reflecting the python version, 
    - e.g. `ds311` & `ds312`
      - here `ds` stands for _data science_ and the set of packages required to run related projects
      - `311` and `312` stands for _python 3.11_ and _python 3.12_ respectively.
- If all projects have migrated from a previous environment you can remove the old one.

## Useful commands per use case

### Updating anaconda
1. `conda activate base`
2. `conda update -n base -c defaults conda --repodata-fn=repodata.json`
   1. Uses the full repodata for better dependency resolution
   2. Will warn if newer conda version is available, e.g.:
      ```bash
      ==> WARNING: A newer version of conda exists. <==
          current version: 25.7.0
          latest version: 26.3.2

      Please update conda by running

          $ conda update -n base -c defaults conda
      ```
3. `conda update -n base --all`
   1. Using `--all` to update all base packages and resolve conflicts that otherwise may prevent conda from updating
4. `conda --version` to check it succeeded in updating its version (e.g. to `conda 26.3.2`)

## Resources
- [https://www.perplexity.ai/search/i-want-to-update-my-conda-envi-w5ntvRByRRa31PO9eimjCA](https://www.perplexity.ai/search/i-want-to-update-my-conda-envi-w5ntvRByRRa31PO9eimjCA)
- [https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-conda.html](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-conda.html)
- [https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)