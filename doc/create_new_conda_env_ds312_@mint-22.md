<style>
body {
  font-family: "Gentium Basic", Cardo , "Linux Libertine o", "Palatino Linotype", Cambria, serif;
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

# Creating a new conda environment `ds312` on `@mint-22`

## Context
- We need a new conda data science oriented environment on `@mint-22` based on `ds311`. 
- As it will be based on Python 3.12, we will name it `ds312`

## Workflow
1. We installed Anaconda as described at [Anaconda_installation@mint-22.md](Anaconda_installation@mint-22.md)
2. We now will create a conda environment named `ds312` based on `ds311`, but with Python 3.12 as basis
   1. We use [ds311-env-creation@linux-laptop.md#steps](ds311-env-creation@linux-laptop.md#steps) as reference

## Steps

