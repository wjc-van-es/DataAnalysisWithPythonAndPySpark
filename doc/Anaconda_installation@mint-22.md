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

# Fresh Anaconda installation @mint-22

## PyCharm installation & git clone
- First we installed PyCharm with JetBrains Toolbox
- Then we used File > project from Version Control... and filled out 
  `git@github.com:wjc-van-es/DataAnalysisWithPythonAndPySpark.git`

## Anaconda

### primary install
- source: [https://docs.anaconda.com/anaconda/install/](https://docs.anaconda.com/anaconda/install/)
- `~/resources/SoftwareInstall/anaconda$ wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh`
- check hash with info from [https://repo.anaconda.com/archive/](https://repo.anaconda.com/archive/)
  ```bash
  willem@mint-22:~/resources/SoftwareInstall/anaconda$ sha256sum Anaconda3-2024.10-1-Linux-x86_64.sh 
  3ba0a298155c32fbfd80cbc238298560bf69a2df511783054adfc151b76d80d8  Anaconda3-2024.10-1-Linux-x86_64.sh
  3ba0a298155c32fbfd80cbc238298560bf69a2df511783054adfc151b76d80d8
  willem@mint-22:~/resources/SoftwareInstall/anaconda$ 

  ```
- Give the shell script execution rights with
  `~/resources/SoftwareInstall/anaconda$ chmod +x Anaconda3-2024.10-1-Linux-x86_64.sh`
- Install with `~/resources/SoftwareInstall/anaconda$ bash ./Anaconda3-2024.10-1-Linux-x86_64.sh`
- Scroll through the license agreement with the enter key
- Agree with `yes` enter
- `conda config --set auto_activate_base false` is the default it means we have to manually activate a conda environment
  with `conda init <environment_name>` in each terminal where we would like to use it, otherwise the standard OS 
  Python installation is used.
- We agreed on the suggested installation location of conda being `~/anaconda3`
- run `~/resources/SoftwareInstall/anaconda$ eval "$(/home/willem/anaconda3/bin/conda shell.bash hook)"`
- `(base) ~/resources/SoftwareInstall/anaconda$ conda init`
  - This reports `modified      /home/willem/.bashrc` (and `no change` for all other listed script files, all under 
    `~/anaconda3` or one of its subdirectories)
- `(base) ~/resources/SoftwareInstall/anaconda$ source ~/.bashrc` to effectuate the changes in the current terminal.

### Test in same terminal
```bash
(base) willem@mint-22:~/resources/SoftwareInstall/anaconda$ which python
/home/willem/anaconda3/bin/python
(base) willem@mint-22:~/resources/SoftwareInstall/anaconda$ python --version
Python 3.12.7
(base) willem@mint-22:~/resources/SoftwareInstall/anaconda$ printenv PATH
/home/willem/anaconda3/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/quarkus/current/bin:/home/willem/.sdkman/candidates/maven/current/bin:/home/willem/.sdkman/candidates/java/current/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(base) willem@mint-22:~/resources/SoftwareInstall/anaconda$ conda config --json
{
  "get": {},
  "rc_path": "/home/willem/.condarc",
  "success": true,
  "warnings": []
}
```

- For more info `conda config --show --json`

## Further actions
