<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I want to update my conda environments

I start out with
conda update -n base -c defaults conda
but when I check with
conda --version
but still the old version is returned

Your conda base environment likely isn't updating due to dependency conflicts or solver issues preventing the upgrade, even though the command runs without errors.[^1_1][^1_2]

## Quick Fixes

Try these commands in sequence from your base environment (activate with `conda activate base` if needed):

- Use the full repodata for better dependency resolution:
`conda update -n base -c defaults conda --repodata-fn=repodata.json`[^1_2]
- Update all base packages to resolve conflicts:
`conda update -n base --all`[^1_3][^1_2]
- Force classic solver if using libmamba (faster but sometimes problematic):
`conda update -n base -c defaults conda --solver=classic`[^1_4]

After any command, verify with `conda --version`. If it still fails, check for pinned packages (`conda list --show-channel-urls`) or conflicts (`conda info`).[^1_2]

## Advanced Troubleshooting

List environments and inspect base: `conda env list` and `conda list -n base | grep conda`. [^1_5]
If base is cluttered (e.g., extra packages like scipy), remove non-essentials: `conda remove -n base <package>`. A clean Miniconda reinstall is a last resort—export envs first with `conda env export > env.yml`.[^1_2]
<span style="display:none">[^1_10][^1_11][^1_12][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://stackoverflow.com/questions/77944252/why-cant-i-update-conda

[^1_2]: https://github.com/conda/conda/issues/9469

[^1_3]: https://stackoverflow.com/questions/57518050/conda-install-and-update-do-not-work-also-solving-environment-get-errors

[^1_4]: https://newreleases.io/project/github/conda/conda/release/23.10.0

[^1_5]: https://docs.conda.io/projects/conda/en/stable/commands/update.html

[^1_6]: https://forum.anaconda.com/t/do-i-need-to-update-conda/54664

[^1_7]: https://community.anaconda.cloud/t/do-i-need-to-update-conda/54664

[^1_8]: https://forum.anaconda.com/t/conda-update-is-not-updating-just-repeats-the-update-command/69404

[^1_9]: https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-conda.html

[^1_10]: https://github.com/conda/conda/issues/8269

[^1_11]: https://github.com/conda/conda/issues/12519

[^1_12]: https://stackoverflow.com/questions/73974735/conda-update-conda-does-not-update-conda/76084719

[^1_13]: https://stackoverflow.com/questions/57701571/what-is-the-right-way-to-update-anaconda-and-conda-base-environments

[^1_14]: https://github.com/conda/conda-libmamba-solver/issues/616

[^1_15]: https://github.com/conda/conda/issues/13549

[^1_16]: https://stackoverflow.com/questions/78437278/problems-encountered-when-installing-new-solver

[^1_17]: https://stackoverflow.com/questions/70365296/how-to-use-conda-update-n-base-conda-properly/76098124

[^1_18]: https://forum.anaconda.com/t/problem-updating-conda-anaconda/62050

[^1_19]: https://docs.conda.io/projects/conda/en/23.9.x/commands/update.html

[^1_20]: https://github.com/conda/conda/issues/14626

[^1_21]: https://docs.conda.io/projects/conda/en/23.10.x/release-notes.html

[^1_22]: https://github.com/conda/conda/issues/11663

[^1_23]: https://conda.github.io/conda-libmamba-solver/user-guide/

[^1_24]: https://github.com/conda/conda/issues/1797

[^1_25]: https://stackoverflow.com/questions/77617946/solve-conda-libmamba-solver-libarchive-so-19-error-after-updating-conda-to-23


---

# The combination of

conda update -n base -c defaults conda
conda update -n base --all
worked.
However my python version on base is still 3.12.11 and I would like to upgrade to the latest stable 3.14 version. Do you recommend updating python in the base environment or would it be better / saver to create a new environment and install python 3.14 (and all the other packages I need for my project) in that new environment?

Creating a new environment for Python 3.14 is safer and aligns with Conda best practices, as updating the base risks dependency conflicts or breaking core tools. Python 3.14 is available via conda-forge, the latest stable major release supported by Conda.[^2_1][^2_2]

## Recommendation

Keep base minimal (Python 3.12 is fine there) and create project-specific environments to isolate dependencies—this prevents version clashes across projects.[^2_3][^2_4][^2_1]

## Create New Environment

Run these commands:

```
conda create -n py314 python=3.14 -c conda-forge
conda activate py314
```

Install your project packages next (e.g., `conda install numpy pandas` or from a `environment.yml`). Export for reproducibility: `conda env export > environment.yml`.[^2_2][^2_1]

## If Updating Base (Not Recommended)

```
conda install -n base python=3.14 -c conda-forge
```

Review changes carefully—solver may downgrade other packages. Backup first: `conda env export -n base > base_backup.yml`.[^2_5][^2_6]
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-python.html

[^2_2]: https://conda-forge.org/blog/2025/10/09/python-314/

[^2_3]: https://github.com/conda/conda/issues/12456

[^2_4]: https://stackoverflow.com/questions/70820752/how-to-update-python-in-anaconda-base-environment/75211780

[^2_5]: https://coderivers.org/blog/conda-upgrade-python/

[^2_6]: https://stackoverflow.com/questions/52035673/how-can-i-update-to-the-latest-python-version-using-conda

[^2_7]: https://www.youtube.com/watch?v=yoCFbZNF81M

[^2_8]: https://stackoverflow.com/questions/57701571/what-is-the-right-way-to-update-anaconda-and-conda-base-environments

[^2_9]: https://rse.shef.ac.uk/conda-environments-for-effective-and-reproducible-research/02-working-with-environments/index.html

[^2_10]: https://forum.anaconda.com/t/i-want-advice-on-managing-python-environments-in-anaconda/92986

[^2_11]: https://edcarp.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html

[^2_12]: https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html

[^2_13]: https://blog.csdn.net/qq_34640315/article/details/152780173

[^2_14]: https://github.com/conda/conda/issues/10634

[^2_15]: https://blog.csdn.net/qq_34640315/article/details/152780305

[^2_16]: https://conda-forge.org/blog/2026/01/15/100-days-python314/

[^2_17]: https://www.technetexperts.com/fix-jupyter-python-314-conda/amp/

[^2_18]: https://docs.conda.io/projects/conda/en/23.1.x/user-guide/tasks/manage-python.html

[^2_19]: https://discuss.python.org/t/conda-version-of-python-3-14/104253


---

# I will follow the instruction, keep base minimal and separate dependencies for each project in a separate environment. As a matter of fact when I need to do a major upgrade for a dedicated project environment I created a new one.

However, for future reference, is there any scenario where updating the python version in the base environment would be necessary? Like with a major new python release like python 4? Or would you need to reinstall conda from scratch at that point?

No, there are no scenarios where updating Python in the base environment is necessary—even for major releases like a hypothetical Python 4. Conda is designed to install any Python version (e.g., 3.14 or future 4.x) into new environments independently of base, which should stay minimal.[^3_1][^3_2][^3_3]

## Why Avoid Base Updates

Base serves as a bootstrap for creating envs; changing its Python can break conda itself or introduce solver conflicts, as base packages are tightly coupled. Official docs and community consensus recommend against it, favoring new envs for all projects.[^3_4][^3_5][^3_6]

## Handling Major Releases

For Python 4 (or any major upgrade):

- Continue creating new envs: `conda create -n project-py4 python=4.0 -c conda-forge`.
- No reinstall needed—Conda handles multi-version support natively. Clean up old envs with `conda env remove -n oldenv` if space is an issue.[^3_2][^3_3]

If base becomes problematic (rare), export envs and reinstall Miniconda/Anaconda, but this isn't tied to Python versions.[^3_7]
<span style="display:none">[^3_10][^3_11][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://stackoverflow.com/questions/72575136/do-i-need-to-update-upgrade-python-version-at-conda-base-environment

[^3_2]: https://stackoverflow.com/questions/52035673/how-can-i-update-to-the-latest-python-version-using-conda

[^3_3]: https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-python.html

[^3_4]: https://coderivers.org/blog/conda-upgrade-python/

[^3_5]: https://stackoverflow.com/questions/70820752/how-to-update-python-in-anaconda-base-environment/75211780

[^3_6]: https://github.com/conda/conda/issues/12456

[^3_7]: https://stackoverflow.com/questions/57701571/what-is-the-right-way-to-update-anaconda-and-conda-base-environments

[^3_8]: https://agirlamonggeeks.com/update-python-version-in-conda-environment/

[^3_9]: https://hpc.njit.edu/assets/slides/conda_training_11-05-2025.pdf

[^3_10]: https://www.pythontutorials.net/blog/how-to-use-conda-update-n-base-conda-properly/

[^3_11]: https://forum.anaconda.com/t/i-want-advice-on-managing-python-environments-in-anaconda/92986


---

# I have created a conda environment with pyspark=4.1.1 and python=3.14.4.
```
JAVA_HOME is pointing to java 21.
When I execute within PyCharm everything works fine, but from the commandline I get an error on
spark = (SparkSession
.builder
.appName(app_name)
.getOrCreate())
with this output:
File "/home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/pyspark/sql/session.py", line 560, in getOrCreate
session = SparkSession(sc, options=self._options)
File "/home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/pyspark/sql/session.py", line 636, in __init__
jSparkSessionClass.getDefaultSession().isDefined()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^

TypeError: 'JavaPackage' object is not callable

This error usually means PySpark can start the Python side, but the JVM side is not being initialized with the same runtime/classpath setup that PyCharm is using. Given that it works in PyCharm but fails in the shell, the most likely issue is environment mismatch: different `JAVA_HOME`, different `SPARK_HOME`/`PYSPARK_*` variables, or a different `spark-submit`/Java being picked up on the command line. Spark 4.1.1 supports Java 17/21 and Python 3.10+, so your versions are broadly compatible.[^4_1][^4_2][^4_3]
```

## What the error usually means

`TypeError: 'JavaPackage' object is not callable` often appears when PySpark is trying to access a JVM class that is missing, misloaded, or coming from the wrong Spark installation. In practice, that is commonly caused by classpath or launcher configuration problems rather than a pure Python issue.[^4_4][^4_5][^4_6]

## Why PyCharm works

PyCharm often runs with a different interpreter startup environment than your interactive shell, so it may inherit variables or path settings that your terminal session does not. A very common pattern is that the IDE is using the conda env correctly while the shell is using a different `java`, `spark-submit`, or `PYTHONPATH`.[^4_7][^4_2]

## Things to check

Run these in the same terminal where it fails:

- `which python`
- `which java`
- `echo $JAVA_HOME`
- `which spark-submit`
- `python -c "import pyspark; print(pyspark.__version__)"`

If `spark-submit` is not coming from your conda env or `JAVA_HOME` is not the Java 21 installation you expect, fix that first.[^4_2][^4_3][^4_1]

## Likely fix

Make sure the shell uses the conda environment’s runtime explicitly before starting Spark:

```bash
conda activate ds314
export JAVA_HOME=/path/to/java-21
export PATH="$JAVA_HOME/bin:$PATH"
unset PYSPARK_SUBMIT_ARGS
unset SPARK_HOME
python your_script.py
```

If you have a separate Spark installation, ensure it matches the PySpark version you installed in conda, or let the conda-provided `pyspark` manage the launch path consistently.[^4_8][^4_1][^4_7]

## Best next step

If the shell still fails, the fastest way to narrow it down is to compare the working PyCharm environment against the failing terminal environment, especially `JAVA_HOME`, `PATH`, `SPARK_HOME`, and `PYSPARK_*` variables. In most cases, aligning those makes the error disappear without changing your code.[^4_3][^4_7][^4_2]

Would you like me to give you a short diagnostic script that prints the exact Spark/Java paths from both PyCharm and the terminal so you can compare them directly?
<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_17][^4_18][^4_19][^4_20][^4_21][^4_22][^4_23][^4_24][^4_25][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://spark.apache.org/docs/latest/

[^4_2]: https://stackoverflow.com/questions/79010499/able-to-execute-pyspark-script-in-pycharm-terminal-using-virtual-env-but-execut

[^4_3]: https://stackoverflow.com/questions/71900906/java-not-found-and-java-home-environment-variable-is-not-set

[^4_4]: https://stackoverflow.com/questions/65713299/javapackage-object-is-not-callable-error-executing-explain-in-pyspark-3-0

[^4_5]: https://stackoverflow.com/questions/58608226/typeerror-javapackage-object-is-not-callable-spark-jvm

[^4_6]: https://github.com/JohnSnowLabs/spark-nlp/discussions/12576

[^4_7]: https://intellij-support.jetbrains.com/hc/en-us/community/posts/12672469165586-How-to-setup-pycharm-for-working-to-run-spark

[^4_8]: https://pypi.org/project/pyspark/

[^4_9]: https://www.youtube.com/watch?v=44A0xRsYFY8

[^4_10]: https://discuss.hail.is/t/typeerror-javapackage-object-is-not-callable-when-using-pyspark/2548

[^4_11]: https://stackoverflow.com/questions/55425348/pyspark-not-able-to-create-sparksession-java-gateway-error

[^4_12]: https://www.youtube.com/watch?v=HYGeBYuJ8is

[^4_13]: https://community.fabric.microsoft.com/t5/Data-Engineering/Pydeequ-JavaPackage-is-not-callable/m-p/4031271

[^4_14]: https://github.com/JohnSnowLabs/spark-nlp/issues/6563

[^4_15]: https://github.com/JohnSnowLabs/spark-nlp/issues/575

[^4_16]: https://github.com/JohnSnowLabs/spark-nlp/issues/13962

[^4_17]: https://github.com/aws/sagemaker-feature-store-spark/issues/20

[^4_18]: https://github.com/JohnSnowLabs/spark-nlp/issues/868

[^4_19]: https://www.4each.com.br/threads/python-typeerror-javapackage-object-is-not-callable-in-pyspark.137535/

[^4_20]: https://codingtechroom.com/question/resolving-typeerror-javapackage-object-is-not-callable-in-pyspark

[^4_21]: https://www.youtube.com/watch?v=IueOeLKk6YQ

[^4_22]: https://www.youtube.com/watch?v=FUelbDkJ1_Y

[^4_23]: https://stackoverflow.com/questions/77712968/what-are-compatible-versions-of-pyspark-and-py4j-packages-in-python

[^4_24]: https://www.youtube.com/watch?v=bRWQmhlyIuQ

[^4_25]: https://services.cs.rutgers.edu/spark.html


---

# There are certainly differences

CLI:
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark\$ printenv PATH
/home/willem/.nvm/versions/node/v22.20.0/bin:/home/willem/anaconda3/envs/ds314/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/spark/current/bin:/home/willem/.sdkman/candidates/quarkus/current/bin:/home/willem/.sdkman/candidates/maven/current/bin:/home/willem/.sdkman/candidates/java/current/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
There is an installation of Spark visible:
SPARK_HOME=/home/willem/.sdkman/candidates/spark/4.0.0-preview2
JAVA_HOME=/home/willem/.sdkman/candidates/java/current (pointing to default), but this is
java 21:
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark\$ sdk current java
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark\$ java -version
openjdk version "21.0.11" 2026-04-21 LTS
OpenJDK Runtime Environment Temurin-21.0.11+10 (build 21.0.11+10-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.11+10 (build 21.0.11+10-LTS, mixed mode, sharing)
Using java version 21.0.11-tem

In PyCharm less clutter is visible on PATH:
PATH=/home/willem/anaconda3/envs/ds314/bin:/home/willem/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts:/home/willem/.local/share/JetBrains/Toolbox/scripts
JAVA_HOME=/home/willem/.sdkman/candidates/java/current (will also evaluate to java 21.0.11-tem
Main difference:
SPARK_HOME is absent

**The issue is your SDKMAN Spark installation interfering.** The CLI has `SPARK_HOME=/home/willem/.sdkman/candidates/spark/4.0.0-preview2` pointing to Spark 4.0.0-preview2, while your conda env has PySpark 4.1.1. This version mismatch causes the `'JavaPackage' object is not callable` error—PySpark 4.1.1 can't communicate with Spark 4.0.0 JVM classes. PyCharm works because `SPARK_HOME` is absent, letting conda PySpark 4.1.1 manage everything correctly.[^5_1]

## Quick Fix (for CLI)

**Before running your script, unset the conflicting SPARK_HOME:**

```bash
conda activate ds314
unset SPARK_HOME
unset PYSPARK_SUBMIT_ARGS  # if set
python your_script.py
```

This lets PySpark 4.1.1 from conda use its bundled Spark JARs and launcher, matching PyCharm's clean setup.

## Permanent Fix Options

### Option 1: Update SDKMAN Spark (Recommended)

```bash
sdk install spark 4.1.1
sdk use spark 4.1.1
```

Then your `SPARK_HOME` will match PySpark 4.1.1.

### Option 2: Remove SDKMAN Spark from PATH

Edit `~/.bashrc` or `~/.zshrc` to comment out SDKMAN Spark paths:

```bash
# export PATH="$HOME/.sdkman/candidates/spark/current/bin:$PATH"
```


### Option 3: Conda-only approach (cleanest)

Add to your `~/.bashrc` **after** conda activation:

```bash
conda activate ds314
unset SPARK_HOME PYSPARK_SUBMIT_ARGS
export PATH="/home/willem/anaconda3/envs/ds314/bin:$PATH"
```


## Verify Fix

After unsetting `SPARK_HOME`, test:

```bash
python -c "from pyspark.sql import SparkSession; spark = SparkSession.builder.appName('test').getOrCreate(); print('Success:', spark.version)"
```

**PySpark works best when there's no external `SPARK_HOME` interference**—the conda package includes everything needed. Your Java 21 is perfect for Spark 4.1.1, so once Spark versions align, everything will work consistently across CLI and PyCharm.

<div align="center">⁂</div>

[^5_1]: https://stackoverflow.com/questions/58608226/typeerror-javapackage-object-is-not-callable-spark-jvm


---

# The quick fix (unsetting the environment variables for spark, SPARK_HOME and PYSPARK_SUBMIT_ARGS) worked.

The problem remains sdkman won't deliver spark 4.1.1 any time soon.
Can I do without a local Spark installation when I just run tests on localhost?
I also use Spark in Java code:
there the pom file contains the dependencies:
org.apache.spark:spark-core_2.13:4.1.1
org.apache.spark:spark-sql_2.13:4.1.1
Here the code doesn't seem to be bothered by the SPARK_HOME=/home/willem/.sdkman/candidates/spark/4.0.0-preview2
At least when I run inside IntelliJ SPARK_HOME and JAVA_HOME appear not to be set and with the system properties:
java.home = /home/willem/.sdkman/candidates/java/21.0.11-tem
sun.boot.library.path = /home/willem/.sdkman/candidates/java/21.0.11-tem/lib
and java.class.path only points to jars in my local maven repo

**Yes, you can absolutely run PySpark 4.1.1 tests on localhost without any local Spark installation.** The conda `pyspark=4.1.1` package includes all necessary Spark JARs and launches everything in `local[*]` mode automatically. Unsetting `SPARK_HOME` (as you did) is the correct approach—PySpark handles the JVM bootstrap itself.

## Why Java Spark Works Differently

Your Java/Scala Spark code succeeds because:

1. **Maven provides JARs**: `spark-core_2.13:4.1.1` + `spark-sql_2.13:4.1.1` download the correct 4.1.1 JARs to `~/.m2/repository`
2. **IntelliJ runs fat JARs**: No `SPARK_HOME` needed—`java -cp ...` executes Spark classes directly from Maven deps
3. **No launcher interference**: Java skips PySpark's Python-to-JVM gateway entirely

PySpark failed because it was trying to connect to your SDKMAN Spark 4.0.0 JVM through the Python gateway, causing the version mismatch.

## Recommended Workflow (No Spark Install Needed)

**For PySpark (CLI/PyCharm):**

```bash
conda activate ds314
unset SPARK_HOME PYSPARK_SUBMIT_ARGS
python script.py  # Uses conda pyspark 4.1.1 JARs automatically
```

**For Java/Spark (IntelliJ/Maven):**

```
mvn compile exec:java -Dexec.mainClass="YourMain"
```

No changes needed—your `pom.xml` handles everything.

## Version Matrix Summary

| Tool | Version Source | Needs SPARK_HOME? |
| :-- | :-- | :-- |
| PySpark (conda) | 4.1.1 JARs bundled | **No** (unset it!) |
| Java/Spark (Maven) | 4.1.1 from `~/.m2` | No |
| SDKMAN Spark | 4.0.0-preview2 | Ignore/Remove |

## Clean PATH for Future

Add this to `~/.bashrc` **after** conda activation:

```bash
# For ds314 PySpark - disable SDKMAN Spark interference
if [[ "$CONDA_DEFAULT_ENV" == "ds314" ]]; then
    unset SPARK_HOME PYSPARK_SUBMIT_ARGS
fi
```

**Bottom line**: Keep SDKMAN Spark for other projects if needed, but always unset `SPARK_HOME` in your `ds314` env. Both Python and Java Spark 4.1.1 will work perfectly for local testing without any system-wide Spark installation.
<span style="display:none">[^6_1][^6_10][^6_2][^6_3][^6_4][^6_5][^6_6][^6_7][^6_8][^6_9]</span>

<div align="center">⁂</div>

[^6_1]: https://copyprogramming.com/howto/can-pyspark-work-without-spark

[^6_2]: https://pypi.org/project/mock-spark/3.6.1/

[^6_3]: https://stackoverflow.com/questions/74786953/can-i-run-pyspark-locally-without-installing-spark-on-windows-10

[^6_4]: https://kokes.github.io/blog/2020/10/19/running-apache-spark-pyspark-locally.html

[^6_5]: https://kordinglab.com/2016/03/18/spark-script.html

[^6_6]: https://libraries.io/pypi/sparkless

[^6_7]: https://stackoverflow.com/questions/46286436/running-pyspark-after-pip-install-pyspark

[^6_8]: https://stackoverflow.com/questions/57256428/do-pyspark-need-a-local-spark-installation

[^6_9]: https://bytes.grubhub.com/learn-pyspark-locally-without-an-aws-cluster-988e2a86f59c?gi=8ca58c168102

[^6_10]: https://pypi.org/project/mock-spark/

