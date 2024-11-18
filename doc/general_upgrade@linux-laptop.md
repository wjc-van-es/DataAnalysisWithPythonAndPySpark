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

# General update / upgrade of all components

## Context
See also [https://github.com/wjc-van-es/da-pyspark-examples/blob/master/readme.md](https://github.com/wjc-van-es/da-pyspark-examples/blob/master/readme.md)

For this project to work we have a working configuration of the following components
- Java 11 from SDKMan (Spark is written in Scala, which runs on the Java Virtual Machine, or JVM).
- Spark from SDKMan.
- Python 3 and IPython from Anaconda.
- An Anaconda virtual environment named dasci (short for Data Science)
- On this dasci environment, the following main packages (with a lot of transient dependencies)
  - PySpark
  - Jupyter
  - matplotlib 

## Java 11 update to latest version
```bash
(dasci) $ sdk current java

Using java version 11.0.20-tem
$ sdk list java | grep tem
 Temurin       |     | 21           | tem     |            | 21-tem              
               |     | 20.0.2       | tem     | installed  | 20.0.2-tem          
               |     | 20.0.1       | tem     |            | 20.0.1-tem          
               |     | 17.0.8       | tem     | installed  | 17.0.8-tem          
               |     | 17.0.8.1     | tem     |            | 17.0.8.1-tem        
               |     | 17.0.7       | tem     |            | 17.0.7-tem          
               | >>> | 11.0.20      | tem     | installed  | 11.0.20-tem         
               |     | 11.0.20.1    | tem     |            | 11.0.20.1-tem       
               |     | 11.0.19      | tem     |            | 11.0.19-tem         
               |     | 8.0.382      | tem     | installed  | 8.0.382-tem         
               |     | 8.0.372      | tem     |            | 8.0.372-tem         
Omit Identifier to install default version 21-tem:
    $ sdk install java 21-tem
(dasci) $ sdk install java 11.0.20.1-tem
Do you want java 11.0.20.1-tem to be set as default? (Y/n): 

Setting java 11.0.20.1-tem as default.
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts

```

## Update Spark to latest version

```bash
(dasci) $ sdk current spark

Using spark version 3.3.1
(dasci) $ sdk list spark > sdk_pyspark_versions.txt ## we can update to 3.4.0 no need to specify this latest version
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk install spark

Downloading: spark 3.4.0
...
Do you want spark 3.4.0 to be set as default? (Y/n): 

Setting spark 3.4.0 as default.
(dasci) $ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts


```