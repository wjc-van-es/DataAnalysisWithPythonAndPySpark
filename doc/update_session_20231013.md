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

# Update Session Friday 20231013

## Java 11
```bash
WARNING: overwriting environment variables set in the machine
overwriting variable {'PATH'}
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk current java

Using java version 11.0.20-tem
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk list java | grep tem
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
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk install java 11.0.20.1-tem

Downloading: java 11.0.20.1-tem

In progress...

################################################################################################################################################################################################################################# 100,0%

Repackaging Java 11.0.20.1-tem...

Done repackaging...

Installing: java 11.0.20.1-tem
Done installing!

Do you want java 11.0.20.1-tem to be set as default? (Y/n): 

Setting java 11.0.20.1-tem as default.

```

## Spark 3.3.1 -> 3.4.0

```bash
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk current spark

Using spark version 3.3.1
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk list spark
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk list spark > cat
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk list spark > sdk_pyspark_versions.txt
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ sdk install spark

Downloading: spark 3.4.0

In progress...

################################################################################################################################################################################################################################# 100,0%

Repackaging Spark 3.4.0...

Done repackaging...

Installing: spark 3.4.0
Done installing!

Do you want spark 3.4.0 to be set as default? (Y/n): 

Setting spark 3.4.0 as default.
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts

(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/code/Ch07$ printenv SPARK_HOME
/home/willem/.sdkman/candidates/spark/3.3.1
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/code/Ch07$ printenv JAVA_HOME
/home/willem/.sdkman/candidates/java/current
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/code/Ch07$ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark/code/Ch07$ cd ~/.sdkman/candidates/spark/
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ ls -la
total 16
drwxrwxr-x  4 willem willem 4096 okt 13 21:02 .
drwxrwxr-x  5 willem willem 4096 apr  9  2023 ..
drwxr-xr-x 13 willem willem 4096 okt 15  2022 3.3.1
drwxr-xr-x 13 willem willem 4096 apr  7  2023 3.4.0
lrwxrwxrwx  1 willem willem    5 okt 13 21:02 current -> 3.4.0
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ sdk current spark 

Using spark version 3.3.1
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ conda env config vars set SPARK_HOME=/home/willem/.sdkman/candidates/spark/current
To make your changes take effect please reactivate your environment
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ conda activate dasci
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ printenv SPARK_HOME
/home/willem/.sdkman/candidates/spark/current
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ printenv PATH
/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ conda env config vars set PATH=/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:$JAVA_HOME/bin:$SPARK_HOME/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
To make your changes take effect please reactivate your environment
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ conda activate dasci
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ printenv PATH
/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/.sdkman/candidates/spark/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ sdk current spark

Using spark version 3.4.0
(dasci) willem@linux-laptop:~/.sdkman/candidates/spark$ 

```
We saw that the PATH environment variable was hardcoded to stick to `/home/willem/.sdkman/candidates/spark/3.3.1/bin`
instead to the `$SPARK_HOME/bin`, which we edited to point to `$SDKMAN_CANDIDATES_DIR/spark/current` (resolving to
`/home/willem/.sdkman/candidates/spark/current`) Now we forced using Spark 3.4.0.

## Updating conda and python in both the base and dasci environment
- In the base environment we updated conda with `conda update conda`
- In the base environment we updated python from 3.9.13 to 3.9.18 with `conda update python`
- In the dasci environment we update python from 3.10.9 to 3.10.13 with `conda update python`

Changing an environment to a major python update (e.g. 3.10.x -> 3.11.x) can be done but will be very time-consuming
to calculate the necessary updates of the other installed packages and there is a chance of failure.

It is therefore recommended to create a whole new environment for drastic upgrades. That is the whole point of working 
with separated, well-defined environments.

```bash
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda deactivate
willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda activate base
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda info --envs
# conda environments:
#
base                  *  /home/willem/anaconda3
dasci                    /home/willem/anaconda3/envs/dasci

(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.9.13
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    aiofiles-22.1.0            |   py39h06a4308_0          24 KB
    aiosqlite-0.18.0           |   py39h06a4308_0          34 KB
    anaconda-anon-usage-0.4.3  | py39hfc0e8ea_100          24 KB
    anaconda-client-1.12.1     |   py39h06a4308_0         152 KB
    aom-3.6.0                  |       h6a678d5_0         2.8 MB
    arrow-1.2.3                |   py39h06a4308_1         154 KB
    arrow-cpp-11.0.0           |       h374c478_2        10.2 MB
    astroid-2.14.2             |   py39h06a4308_0         393 KB
    attrs-23.1.0               |   py39h06a4308_0         140 KB
    aws-c-common-0.6.8         |       h5eee18b_1         177 KB
    aws-c-event-stream-0.1.6   |       h6a678d5_6          25 KB
    aws-checksums-0.1.11       |       h5eee18b_2          48 KB
    aws-sdk-cpp-1.8.185        |       h721c034_1         2.2 MB
    beautifulsoup4-4.12.2      |   py39h06a4308_0         209 KB
    black-23.3.0               |   py39h06a4308_0         258 KB
    bokeh-3.2.1                |   py39h2f386ee_0         6.1 MB
    boltons-23.0.0             |   py39h06a4308_0         426 KB
    boost-cpp-1.73.0           |      h7f8727e_12          16 KB
    boto3-1.26.76              |   py39h06a4308_0         120 KB
    botocore-1.29.76           |   py39h06a4308_0         6.3 MB
    c-ares-1.19.1              |       h5eee18b_0         118 KB
    c-blosc2-2.8.0             |       h6a678d5_0         309 KB
    ca-certificates-2023.08.22 |       h06a4308_0         123 KB
    certifi-2023.7.22          |   py39h06a4308_0         153 KB
    cffi-1.15.1                |   py39h5eee18b_3         242 KB
    cfitsio-3.470              |       h5893167_7         833 KB
    cloudpickle-2.2.1          |   py39h06a4308_0          41 KB
    conda-23.9.0               |   py39h06a4308_0         972 KB
    conda-build-3.27.0         |   py39h06a4308_0         603 KB
    conda-content-trust-0.2.0  |   py39h06a4308_0          51 KB
    conda-index-0.3.0          |   py39h06a4308_0         202 KB
    conda-package-handling-2.2.0|   py39h06a4308_0         267 KB
    conda-package-streaming-0.9.0|   py39h06a4308_0          27 KB
    conda-repo-cli-1.0.75      |   py39h06a4308_0         134 KB
    cryptography-41.0.3        |   py39hdda0065_0         2.0 MB
    curl-8.4.0                 |       hdbd6064_0          85 KB
    cyrus-sasl-2.1.28          |       h52b45da_1         237 KB
    cython-3.0.0               |   py39h5eee18b_0         3.2 MB
    daal4py-2023.1.1           |   py39h79cecc1_0        11.4 MB
    dal-2023.1.1               |   hdb19cb5_48679        36.9 MB
    dask-2023.6.0              |   py39h06a4308_0           6 KB
    dask-core-2023.6.0         |   py39h06a4308_0         2.1 MB
    datashader-0.15.2          |   py39h06a4308_0        16.8 MB
    dav1d-1.2.1                |       h5eee18b_0         823 KB
    debugpy-1.6.7              |   py39h6a678d5_0         2.0 MB
    dill-0.3.7                 |   py39h06a4308_0         170 KB
    distributed-2023.6.0       |   py39h06a4308_0         1.3 MB
    docstring-to-markdown-0.11 |   py39h06a4308_0          31 KB
    exceptiongroup-1.0.4       |   py39h06a4308_0          28 KB
    expat-2.5.0                |       h6a678d5_0         172 KB
    flake8-6.0.0               |   py39h06a4308_0         155 KB
    flask-2.2.2                |   py39h06a4308_0         147 KB
    fontconfig-2.14.1          |       h4c34cd2_2         281 KB
    fsspec-2023.9.2            |   py39h06a4308_0         260 KB
    future-0.18.3              |   py39h06a4308_0         671 KB
    giflib-5.2.1               |       h5eee18b_3          80 KB
    grpc-cpp-1.48.2            |       he1ff14a_1         4.8 MB
    gst-plugins-base-1.14.1    |       h6a678d5_1         2.2 MB
    gstreamer-1.14.1           |       h5eee18b_1         1.7 MB
    h5py-3.9.0                 |   py39he06866b_0         1.2 MB
    hdf5-1.12.1                |       h2b7332f_3         5.4 MB
    holoviews-1.17.1           |   py39h06a4308_0         4.4 MB
    hvplot-0.8.4               |   py39h06a4308_0         3.1 MB
    imagecodecs-2023.1.23      |   py39hc4b7b5f_0         9.4 MB
    imageio-2.31.4             |   py39h06a4308_0         469 KB
    importlib-metadata-6.0.0   |   py39h06a4308_0          38 KB
    importlib_metadata-6.0.0   |       hd3eb1b0_0           8 KB
    importlib_resources-5.2.0  |     pyhd3eb1b0_1          21 KB
    intake-0.6.8               |   py39h06a4308_0         208 KB
    intel-openmp-2023.1.0      |   hdb19cb5_46305        17.1 MB
    ipykernel-6.25.0           |   py39h2f386ee_0         228 KB
    ipython-8.15.0             |   py39h06a4308_0         1.1 MB
    ipywidgets-8.0.4           |   py39h06a4308_0         195 KB
    jaraco.classes-3.2.1       |     pyhd3eb1b0_0           9 KB
    jellyfish-1.0.1            |   py39hb02cf49_0        1013 KB
    jinja2-3.1.2               |   py39h06a4308_0         211 KB
    joblib-1.2.0               |   py39h06a4308_0         396 KB
    jpeg-9e                    |       h5eee18b_1         262 KB
    jsonpatch-1.32             |     pyhd3eb1b0_0          15 KB
    jsonpointer-2.1            |     pyhd3eb1b0_0           9 KB
    jsonschema-4.17.3          |   py39h06a4308_0         140 KB
    jupyter_client-8.1.0       |   py39h06a4308_0         178 KB
    jupyter_console-6.6.3      |   py39h06a4308_0          44 KB
    jupyter_core-5.3.0         |   py39h06a4308_0          89 KB
    jupyter_events-0.6.3       |   py39h06a4308_0          37 KB
    jupyter_server-2.5.0       |   py39h06a4308_0         462 KB
    jupyter_server_fileid-0.9.0|   py39h06a4308_0          29 KB
    jupyter_server_terminals-0.4.4|   py39h06a4308_1          24 KB
    jupyter_server_ydoc-0.8.0  |   py39h06a4308_1          21 KB
    jupyter_ydoc-0.2.4         |   py39h06a4308_0          15 KB
    jupyterlab-3.6.3           |   py39h06a4308_0         4.1 MB
    jupyterlab_server-2.22.0   |   py39h06a4308_0          82 KB
    jupyterlab_widgets-3.0.5   |   py39h06a4308_0         178 KB
    keyring-23.13.1            |   py39h06a4308_0          64 KB
    krb5-1.20.1                |       h143b758_1         1.3 MB
    libarchive-3.6.2           |       h6ac8c49_2         900 KB
    libavif-0.11.1             |       h5eee18b_0         111 KB
    libclang-14.0.6            |default_hc6dbbc7_1         137 KB
    libclang13-14.0.6          |default_he11475f_1         9.8 MB
    libcups-2.4.2              |       h2d74bed_1         4.5 MB
    libcurl-8.4.0              |       h251f7ec_0         411 KB
    libdeflate-1.17            |       h5eee18b_1          64 KB
    libevent-2.1.12            |       hdbd6064_1         453 KB
    libffi-3.4.4               |       h6a678d5_0         142 KB
    libgfortran-ng-11.2.0      |       h00389a5_1          20 KB
    libgfortran5-11.2.0        |       h1234567_1         2.0 MB
    libidn2-2.3.4              |       h5eee18b_0         146 KB
    libllvm14-14.0.6           |       hdb19cb5_3        33.4 MB
    libnghttp2-1.57.0          |       h2d74bed_0         674 KB
    libpng-1.6.39              |       h5eee18b_0         304 KB
    libpq-12.15                |       hdbd6064_1         2.4 MB
    libssh2-1.10.0             |       hdbd6064_2         292 KB
    libthrift-0.15.0           |       h1795dd8_2         4.0 MB
    libtiff-4.5.1              |       h6a678d5_0         533 KB
    libwebp-1.3.2              |       h11a3e52_0          87 KB
    libwebp-base-1.3.2         |       h5eee18b_0         387 KB
    libxkbcommon-1.0.1         |       h5eee18b_1         590 KB
    libxml2-2.10.4             |       hcbfbd50_0         755 KB
    libxslt-1.1.37             |       h2085143_0         266 KB
    linkify-it-py-2.0.0        |   py39h06a4308_0          34 KB
    llvmlite-0.41.0            |   py39he621ea3_0         3.5 MB
    lxml-4.9.3                 |   py39hdbbb534_0         1.5 MB
    lz4-4.3.2                  |   py39h5eee18b_0          35 KB
    markdown-it-py-2.2.0       |   py39h06a4308_1         113 KB
    markupsafe-2.1.1           |   py39h7f8727e_0          21 KB
    matplotlib-3.7.2           |   py39h06a4308_0           8 KB
    matplotlib-base-3.7.2      |   py39h1128e8f_0         6.7 MB
    mdit-py-plugins-0.3.0      |   py39h06a4308_0          52 KB
    mdurl-0.1.0                |   py39h06a4308_0          18 KB
    mkl-2023.1.0               |   h213fc3f_46343       171.6 MB
    mkl-service-2.4.0          |   py39h5eee18b_1          54 KB
    mkl_fft-1.3.8              |   py39h5eee18b_0         216 KB
    mkl_random-1.2.4           |   py39hdb19cb5_0         313 KB
    more-itertools-8.12.0      |     pyhd3eb1b0_0          49 KB
    mpich-4.1.1                |       hbae89fd_0        20.4 MB
    mpmath-1.3.0               |   py39h06a4308_0         829 KB
    mypy_extensions-1.0.0      |   py39h06a4308_0          11 KB
    mysql-5.7.24               |       h721c034_2        60.0 MB
    nbclassic-0.5.5            |   py39h06a4308_0         6.1 MB
    nbconvert-6.5.4            |   py39h06a4308_0         513 KB
    nbformat-5.9.2             |   py39h06a4308_0         136 KB
    networkx-3.1               |   py39h06a4308_0         2.7 MB
    nltk-3.8.1                 |   py39h06a4308_0         2.2 MB
    nspr-4.35                  |       h6a678d5_0         244 KB
    nss-3.89.1                 |       h6a678d5_0         2.1 MB
    numba-0.58.0               |   py39h1128e8f_0         4.3 MB
    numexpr-2.8.7              |   py39h85018f9_0         140 KB
    numpy-1.24.3               |   py39hf6e8229_1          10 KB
    numpy-base-1.24.3          |   py39h060ed82_1         6.2 MB
    openssl-3.0.11             |       h7f8727e_2         5.2 MB
    orc-1.7.4                  |       hb3bc3d3_1         972 KB
    packaging-23.1             |   py39h06a4308_0          77 KB
    pandas-2.0.3               |   py39h1128e8f_0        12.3 MB
    panel-1.2.3                |   py39h06a4308_0        14.3 MB
    param-1.13.0               |   py39h06a4308_0         145 KB
    partd-1.4.0                |   py39h06a4308_0          36 KB
    pillow-10.0.1              |   py39ha6cbd5a_0         745 KB
    pip-23.2.1                 |   py39h06a4308_0         2.6 MB
    pkginfo-1.9.6              |   py39h06a4308_0          50 KB
    platformdirs-3.10.0        |   py39h06a4308_0          33 KB
    py-cpuinfo-8.0.0           |     pyhd3eb1b0_1          23 KB
    pyarrow-11.0.0             |   py39h468efa6_1         4.3 MB
    pycodestyle-2.10.0         |   py39h06a4308_0          68 KB
    pycosat-0.6.6              |   py39h5eee18b_0          94 KB
    pycurl-7.45.2              |   py39hdbd6064_1          84 KB
    pyflakes-3.0.1             |   py39h06a4308_0         119 KB
    pygments-2.15.1            |   py39h06a4308_1         1.7 MB
    pylint-2.16.2              |   py39h06a4308_0         727 KB
    pylint-venv-2.3.0          |   py39h06a4308_0          11 KB
    pyodbc-4.0.39              |   py39h6a678d5_0          77 KB
    pyopenssl-23.2.0           |   py39h06a4308_0          96 KB
    pytables-3.8.0             |   py39hb8ae3fc_3         2.0 MB
    pytest-7.4.0               |   py39h06a4308_0         522 KB
    python-3.9.18              |       h955ad1f_0        25.1 MB
    python-json-logger-2.0.7   |   py39h06a4308_0          16 KB
    python-lmdb-1.4.1          |   py39h6a678d5_0         141 KB
    python-lsp-server-1.7.2    |   py39h06a4308_0         108 KB
    python-tzdata-2023.3       |     pyhd3eb1b0_0         140 KB
    pytoolconfig-1.2.5         |   py39h06a4308_1          31 KB
    pytz-2023.3.post1          |   py39h06a4308_0         210 KB
    pyviz_comms-2.3.0          |   py39h06a4308_0          36 KB
    pyzmq-25.1.0               |   py39h6a678d5_0         459 KB
    qt-main-5.15.2             |       h7358343_9        53.7 MB
    qt-webengine-5.15.9        |       h9ab4d14_7        53.8 MB
    qtconsole-5.4.2            |   py39h06a4308_0         191 KB
    qtwebkit-5.212             |       h3fafdc1_5        16.2 MB
    queuelib-1.6.2             |   py39h06a4308_0          27 KB
    regex-2023.10.3            |   py39h5eee18b_0         365 KB
    requests-2.31.0            |   py39h06a4308_0          96 KB
    requests-toolbelt-1.0.0    |   py39h06a4308_0          72 KB
    rfc3339-validator-0.1.4    |   py39h06a4308_0           9 KB
    rfc3986-validator-0.1.1    |   py39h06a4308_0           9 KB
    rope-1.7.0                 |   py39h06a4308_0         441 KB
    scikit-learn-1.3.0         |   py39h1128e8f_0         8.4 MB
    scikit-learn-intelex-2023.1.1|   py39h06a4308_0         111 KB
    scipy-1.11.3               |   py39h5f9d8c6_0        20.3 MB
    scrapy-2.8.0               |   py39h06a4308_0         404 KB
    secretstorage-3.3.1        |   py39h06a4308_1          26 KB
    setuptools-68.0.0          |   py39h06a4308_0         928 KB
    soupsieve-2.5              |   py39h06a4308_0          69 KB
    spyder-5.4.3               |   py39h06a4308_1        10.5 MB
    spyder-kernels-2.4.4       |   py39h06a4308_0         154 KB
    sqlalchemy-2.0.21          |   py39h5eee18b_0         3.1 MB
    sqlite-3.41.2              |       h5eee18b_0         1.2 MB
    statsmodels-0.14.0         |   py39ha9d4c09_0        10.5 MB
    tbb-2021.8.0               |       hdb19cb5_0         1.6 MB
    tbb4py-2021.8.0            |   py39hdb19cb5_0         233 KB
    tenacity-8.2.2             |   py39h06a4308_0          37 KB
    tifffile-2023.4.12         |   py39h06a4308_0         386 KB
    tornado-6.3.3              |   py39h5eee18b_0         635 KB
    tqdm-4.65.0                |   py39hb070fc8_0         131 KB
    twisted-22.10.0            |   py39h5eee18b_0         5.3 MB
    typing-extensions-4.7.1    |   py39h06a4308_0           9 KB
    typing_extensions-4.7.1    |   py39h06a4308_0          55 KB
    tzdata-2023c               |       h04d1e81_0         116 KB
    uc-micro-py-1.0.1          |   py39h06a4308_0          10 KB
    urllib3-1.26.16            |   py39h06a4308_0         201 KB
    werkzeug-2.2.3             |   py39h06a4308_0         341 KB
    wget-1.21.4                |       h251f7ec_1         805 KB
    wheel-0.41.2               |   py39h06a4308_0         108 KB
    widgetsnbextension-4.0.5   |   py39h06a4308_0         875 KB
    xarray-2023.6.0            |   py39h06a4308_0         1.7 MB
    xlrd-2.0.1                 |     pyhd3eb1b0_1          97 KB
    xlsxwriter-3.1.1           |   py39h06a4308_0         247 KB
    xyzservices-2022.9.0       |   py39h06a4308_1          43 KB
    xz-5.4.2                   |       h5eee18b_0         642 KB
    y-py-0.5.9                 |   py39h52d8a92_0         1.3 MB
    ypy-websocket-0.8.2        |   py39h06a4308_0          26 KB
    zfp-1.0.0                  |       h6a678d5_0         289 KB
    zict-3.0.0                 |   py39h06a4308_0          92 KB
    zlib-ng-2.0.7              |       h5eee18b_0         100 KB
    zstandard-0.19.0           |   py39h5eee18b_0         474 KB
    zstd-1.5.5                 |       hc292b87_0         647 KB
    ------------------------------------------------------------
                                           Total:       793.9 MB

The following NEW packages will be INSTALLED:

  abseil-cpp         pkgs/main/linux-64::abseil-cpp-20211102.0-hd4dd3e8_0 
  aiofiles           pkgs/main/linux-64::aiofiles-22.1.0-py39h06a4308_0 
  aiosqlite          pkgs/main/linux-64::aiosqlite-0.18.0-py39h06a4308_0 
  anaconda-anon-usa~ pkgs/main/linux-64::anaconda-anon-usage-0.4.3-py39hfc0e8ea_100 
  aom                pkgs/main/linux-64::aom-3.6.0-h6a678d5_0 
  arrow-cpp          pkgs/main/linux-64::arrow-cpp-11.0.0-h374c478_2 
  asttokens          pkgs/main/noarch::asttokens-2.0.5-pyhd3eb1b0_0 
  aws-c-common       pkgs/main/linux-64::aws-c-common-0.6.8-h5eee18b_1 
  aws-c-event-stream pkgs/main/linux-64::aws-c-event-stream-0.1.6-h6a678d5_6 
  aws-checksums      pkgs/main/linux-64::aws-checksums-0.1.11-h5eee18b_2 
  aws-sdk-cpp        pkgs/main/linux-64::aws-sdk-cpp-1.8.185-h721c034_1 
  boltons            pkgs/main/linux-64::boltons-23.0.0-py39h06a4308_0 
  boost-cpp          pkgs/main/linux-64::boost-cpp-1.73.0-h7f8727e_12 
  c-blosc2           pkgs/main/linux-64::c-blosc2-2.8.0-h6a678d5_0 
  conda-index        pkgs/main/linux-64::conda-index-0.3.0-py39h06a4308_0 
  cyrus-sasl         pkgs/main/linux-64::cyrus-sasl-2.1.28-h52b45da_1 
  dav1d              pkgs/main/linux-64::dav1d-1.2.1-h5eee18b_0 
  docstring-to-mark~ pkgs/main/linux-64::docstring-to-markdown-0.11-py39h06a4308_0 
  exceptiongroup     pkgs/main/linux-64::exceptiongroup-1.0.4-py39h06a4308_0 
  executing          pkgs/main/noarch::executing-0.8.3-pyhd3eb1b0_0 
  gflags             pkgs/main/linux-64::gflags-2.2.2-he6710b0_0 
  glog               pkgs/main/linux-64::glog-0.5.0-h2531618_0 
  grpc-cpp           pkgs/main/linux-64::grpc-cpp-1.48.2-he1ff14a_1 
  importlib_resourc~ pkgs/main/noarch::importlib_resources-5.2.0-pyhd3eb1b0_1 
  jaraco.classes     pkgs/main/noarch::jaraco.classes-3.2.1-pyhd3eb1b0_0 
  jsonpatch          pkgs/main/noarch::jsonpatch-1.32-pyhd3eb1b0_0 
  jsonpointer        pkgs/main/noarch::jsonpointer-2.1-pyhd3eb1b0_0 
  jupyter_events     pkgs/main/linux-64::jupyter_events-0.6.3-py39h06a4308_0 
  jupyter_server_fi~ pkgs/main/linux-64::jupyter_server_fileid-0.9.0-py39h06a4308_0 
  jupyter_server_te~ pkgs/main/linux-64::jupyter_server_terminals-0.4.4-py39h06a4308_1 
  jupyter_server_yd~ pkgs/main/linux-64::jupyter_server_ydoc-0.8.0-py39h06a4308_1 
  jupyter_ydoc       pkgs/main/linux-64::jupyter_ydoc-0.2.4-py39h06a4308_0 
  libavif            pkgs/main/linux-64::libavif-0.11.1-h5eee18b_0 
  libboost           pkgs/main/linux-64::libboost-1.73.0-h28710b8_12 
  libclang13         pkgs/main/linux-64::libclang13-14.0.6-default_he11475f_1 
  libcups            pkgs/main/linux-64::libcups-2.4.2-h2d74bed_1 
  libgfortran5       pkgs/main/linux-64::libgfortran5-11.2.0-h1234567_1 
  libllvm14          pkgs/main/linux-64::libllvm14-14.0.6-hdb19cb5_3 
  libprotobuf        pkgs/main/linux-64::libprotobuf-3.20.3-he621ea3_0 
  libthrift          pkgs/main/linux-64::libthrift-0.15.0-h1795dd8_2 
  linkify-it-py      pkgs/main/linux-64::linkify-it-py-2.0.0-py39h06a4308_0 
  lz4                pkgs/main/linux-64::lz4-4.3.2-py39h5eee18b_0 
  markdown-it-py     pkgs/main/linux-64::markdown-it-py-2.2.0-py39h06a4308_1 
  mdit-py-plugins    pkgs/main/linux-64::mdit-py-plugins-0.3.0-py39h06a4308_0 
  mdurl              pkgs/main/linux-64::mdurl-0.1.0-py39h06a4308_0 
  more-itertools     pkgs/main/noarch::more-itertools-8.12.0-pyhd3eb1b0_0 
  mysql              pkgs/main/linux-64::mysql-5.7.24-h721c034_2 
  orc                pkgs/main/linux-64::orc-1.7.4-hb3bc3d3_1 
  pure_eval          pkgs/main/noarch::pure_eval-0.2.2-pyhd3eb1b0_0 
  py-cpuinfo         pkgs/main/noarch::py-cpuinfo-8.0.0-pyhd3eb1b0_1 
  pyarrow            pkgs/main/linux-64::pyarrow-11.0.0-py39h468efa6_1 
  pylint-venv        pkgs/main/linux-64::pylint-venv-2.3.0-py39h06a4308_0 
  python-json-logger pkgs/main/linux-64::python-json-logger-2.0.7-py39h06a4308_0 
  python-lmdb        pkgs/main/linux-64::python-lmdb-1.4.1-py39h6a678d5_0 
  python-tzdata      pkgs/main/noarch::python-tzdata-2023.3-pyhd3eb1b0_0 
  pytoolconfig       pkgs/main/linux-64::pytoolconfig-1.2.5-py39h06a4308_1 
  re2                pkgs/main/linux-64::re2-2022.04.01-h295c915_0 
  requests-toolbelt  pkgs/main/linux-64::requests-toolbelt-1.0.0-py39h06a4308_0 
  rfc3339-validator  pkgs/main/linux-64::rfc3339-validator-0.1.4-py39h06a4308_0 
  rfc3986-validator  pkgs/main/linux-64::rfc3986-validator-0.1.1-py39h06a4308_0 
  stack_data         pkgs/main/noarch::stack_data-0.2.0-pyhd3eb1b0_0 
  uc-micro-py        pkgs/main/linux-64::uc-micro-py-1.0.1-py39h06a4308_0 
  utf8proc           pkgs/main/linux-64::utf8proc-2.6.1-h27cfd23_0 
  xyzservices        pkgs/main/linux-64::xyzservices-2022.9.0-py39h06a4308_1 
  y-py               pkgs/main/linux-64::y-py-0.5.9-py39h52d8a92_0 
  ypy-websocket      pkgs/main/linux-64::ypy-websocket-0.8.2-py39h06a4308_0 
  zlib-ng            pkgs/main/linux-64::zlib-ng-2.0.7-h5eee18b_0 

The following packages will be REMOVED:

  dataclasses-0.8-pyh6d0b6a4_7
  flit-core-3.6.0-pyhd3eb1b0_0
  glob2-0.7-pyhd3eb1b0_0
  libgfortran4-7.5.0-ha8ba4b0_17
  libllvm10-10.0.1-hbcb73fb_5
  libllvm11-11.1.0-h9e868ea_6
  mock-4.0.3-pyhd3eb1b0_0
  pyhamcrest-2.0.2-pyhd3eb1b0_2
  ripgrep-13.0.0-hbdeaff8_0

The following packages will be UPDATED:

  anaconda-client                     1.11.0-py39h06a4308_0 --> 1.12.1-py39h06a4308_0 
  arrow                                1.2.3-py39h06a4308_0 --> 1.2.3-py39h06a4308_1 
  astroid                             2.11.7-py39h06a4308_0 --> 2.14.2-py39h06a4308_0 
  attrs                               22.1.0-py39h06a4308_0 --> 23.1.0-py39h06a4308_0 
  beautifulsoup4                      4.11.1-py39h06a4308_0 --> 4.12.2-py39h06a4308_0 
  black                               22.6.0-py39h06a4308_0 --> 23.3.0-py39h06a4308_0 
  bokeh                                2.4.3-py39h06a4308_0 --> 3.2.1-py39h2f386ee_0 
  boto3                              1.24.28-py39h06a4308_0 --> 1.26.76-py39h06a4308_0 
  botocore                           1.27.59-py39h06a4308_0 --> 1.29.76-py39h06a4308_0 
  c-ares                                  1.18.1-h7f8727e_0 --> 1.19.1-h5eee18b_0 
  ca-certificates                     2023.01.10-h06a4308_0 --> 2023.08.22-h06a4308_0 
  certifi                          2022.12.7-py39h06a4308_0 --> 2023.7.22-py39h06a4308_0 
  cffi                                1.15.1-py39h74dc2b5_0 --> 1.15.1-py39h5eee18b_3 
  cfitsio                                  3.470-hf0d0db6_6 --> 3.470-h5893167_7 
  cloudpickle        pkgs/main/noarch::cloudpickle-2.0.0-p~ --> pkgs/main/linux-64::cloudpickle-2.2.1-py39h06a4308_0 
  conda                               23.1.0-py39h06a4308_0 --> 23.9.0-py39h06a4308_0 
  conda-build                         3.22.0-py39h06a4308_0 --> 3.27.0-py39h06a4308_0 
  conda-content-tru~                   0.1.3-py39h06a4308_0 --> 0.2.0-py39h06a4308_0 
  conda-package-han~                   2.0.2-py39h06a4308_0 --> 2.2.0-py39h06a4308_0 
  conda-package-str~                   0.7.0-py39h06a4308_0 --> 0.9.0-py39h06a4308_0 
  conda-repo-cli                      1.0.27-py39h06a4308_0 --> 1.0.75-py39h06a4308_0 
  cryptography                        38.0.4-py39h9ce1e76_0 --> 41.0.3-py39hdda0065_0 
  curl                                    7.87.0-h5eee18b_0 --> 8.4.0-hdbd6064_0 
  cython                             0.29.32-py39h6a678d5_0 --> 3.0.0-py39h5eee18b_0 
  daal4py                           2021.6.0-py39h79cecc1_1 --> 2023.1.1-py39h79cecc1_0 
  dal                                 2021.6.0-hdb19cb5_916 --> 2023.1.1-hdb19cb5_48679 
  dask               pkgs/main/noarch::dask-2022.2.1-pyhd3~ --> pkgs/main/linux-64::dask-2023.6.0-py39h06a4308_0 
  dask-core          pkgs/main/noarch::dask-core-2022.2.1-~ --> pkgs/main/linux-64::dask-core-2023.6.0-py39h06a4308_0 
  datashader                          0.14.3-py39h06a4308_0 --> 0.15.2-py39h06a4308_0 
  debugpy                              1.5.1-py39h295c915_0 --> 1.6.7-py39h6a678d5_0 
  dill                                 0.3.6-py39h06a4308_0 --> 0.3.7-py39h06a4308_0 
  distributed        pkgs/main/noarch::distributed-2022.2.~ --> pkgs/main/linux-64::distributed-2023.6.0-py39h06a4308_0 
  expat                                    2.4.9-h6a678d5_0 --> 2.5.0-h6a678d5_0 
  flake8             pkgs/main/noarch::flake8-4.0.1-pyhd3e~ --> pkgs/main/linux-64::flake8-6.0.0-py39h06a4308_0 
  flask              pkgs/main/noarch::flask-1.1.2-pyhd3eb~ --> pkgs/main/linux-64::flask-2.2.2-py39h06a4308_0 
  fontconfig                              2.14.1-h52c9d5c_1 --> 2.14.1-h4c34cd2_2 
  fsspec                           2022.11.0-py39h06a4308_0 --> 2023.9.2-py39h06a4308_0 
  future                              0.18.2-py39h06a4308_1 --> 0.18.3-py39h06a4308_0 
  giflib                                   5.2.1-h5eee18b_1 --> 5.2.1-h5eee18b_3 
  glib                                    2.69.1-h4ff587b_1 --> 2.69.1-he621ea3_2 
  gst-plugins-base                        1.14.0-h8213a91_2 --> 1.14.1-h6a678d5_1 
  gstreamer                               1.14.0-h28cd5cc_2 --> 1.14.1-h5eee18b_1 
  h5py                                 3.7.0-py39h737f45e_0 --> 3.9.0-py39he06866b_0 
  hdf5                                    1.10.6-hb1b8bf9_0 --> 1.12.1-h2b7332f_3 
  holoviews                           1.15.3-py39h06a4308_0 --> 1.17.1-py39h06a4308_0 
  hvplot                               0.8.2-py39h06a4308_0 --> 0.8.4-py39h06a4308_0 
  imagecodecs                      2021.8.26-py39hf0132c2_1 --> 2023.1.23-py39hc4b7b5f_0 
  imageio                             2.19.3-py39h06a4308_0 --> 2.31.4-py39h06a4308_0 
  importlib-metadata                  4.11.3-py39h06a4308_0 --> 6.0.0-py39h06a4308_0 
  importlib_metadata                      4.11.3-hd3eb1b0_0 --> 6.0.0-hd3eb1b0_0 
  intake                               0.6.6-py39h06a4308_0 --> 0.6.8-py39h06a4308_0 
  intel-openmp                       2021.4.0-h06a4308_3561 --> 2023.1.0-hdb19cb5_46305 
  ipykernel                           6.19.2-py39hb070fc8_0 --> 6.25.0-py39h2f386ee_0 
  ipython                             7.31.1-py39h06a4308_1 --> 8.15.0-py39h06a4308_0 
  ipywidgets         pkgs/main/noarch::ipywidgets-7.6.5-py~ --> pkgs/main/linux-64::ipywidgets-8.0.4-py39h06a4308_0 
  jellyfish                            0.9.0-py39h7f8727e_0 --> 1.0.1-py39hb02cf49_0 
  jinja2             pkgs/main/noarch::jinja2-2.11.3-pyhd3~ --> pkgs/main/linux-64::jinja2-3.1.2-py39h06a4308_0 
  joblib                               1.1.1-py39h06a4308_0 --> 1.2.0-py39h06a4308_0 
  jpeg                                        9e-h7f8727e_0 --> 9e-h5eee18b_1 
  jsonschema                          4.16.0-py39h06a4308_0 --> 4.17.3-py39h06a4308_0 
  jupyter_client                       7.4.8-py39h06a4308_0 --> 8.1.0-py39h06a4308_0 
  jupyter_console                      6.4.4-py39h06a4308_0 --> 6.6.3-py39h06a4308_0 
  jupyter_core                         5.1.1-py39h06a4308_0 --> 5.3.0-py39h06a4308_0 
  jupyter_server                      1.23.4-py39h06a4308_0 --> 2.5.0-py39h06a4308_0 
  jupyterlab                           3.5.3-py39h06a4308_0 --> 3.6.3-py39h06a4308_0 
  jupyterlab_server  pkgs/main/noarch::jupyterlab_server-2~ --> pkgs/main/linux-64::jupyterlab_server-2.22.0-py39h06a4308_0 
  jupyterlab_widgets pkgs/main/noarch::jupyterlab_widgets-~ --> pkgs/main/linux-64::jupyterlab_widgets-3.0.5-py39h06a4308_0 
  keyring                             23.4.0-py39h06a4308_0 --> 23.13.1-py39h06a4308_0 
  krb5                                    1.19.4-h568e23c_0 --> 1.20.1-h143b758_1 
  libarchive                               3.6.2-hab531cd_0 --> 3.6.2-h6ac8c49_2 
  libclang                        10.0.1-default_hb85057a_2 --> 14.0.6-default_hc6dbbc7_1 
  libcurl                                 7.87.0-h91b91d3_0 --> 8.4.0-h251f7ec_0 
  libdeflate                                 1.8-h7f8727e_5 --> 1.17-h5eee18b_1 
  libevent                                2.1.12-h8f2d780_0 --> 2.1.12-hdbd6064_1 
  libffi                                     3.3-he6710b0_2 --> 3.4.4-h6a678d5_0 
  libgfortran-ng                          7.5.0-ha8ba4b0_17 --> 11.2.0-h00389a5_1 
  libidn2                                  2.3.2-h7f8727e_0 --> 2.3.4-h5eee18b_0 
  libnghttp2                              1.46.0-hce63b2e_0 --> 1.57.0-h2d74bed_0 
  libpng                                  1.6.37-hbc83047_0 --> 1.6.39-h5eee18b_0 
  libpq                                     12.9-h16c4e8d_3 --> 12.15-hdbd6064_1 
  libssh2                                 1.10.0-h8f2d780_0 --> 1.10.0-hdbd6064_2 
  libtiff                                  4.5.0-h6a678d5_1 --> 4.5.1-h6a678d5_0 
  libwebp                                  1.2.4-h11a3e52_0 --> 1.3.2-h11a3e52_0 
  libwebp-base                             1.2.4-h5eee18b_0 --> 1.3.2-h5eee18b_0 
  libxkbcommon                             1.0.1-hfa300c1_0 --> 1.0.1-h5eee18b_1 
  libxml2                                 2.9.14-h74e7548_0 --> 2.10.4-hcbfbd50_0 
  libxslt                                 1.1.35-h4e12654_0 --> 1.1.37-h2085143_0 
  llvmlite                            0.39.1-py39he621ea3_0 --> 0.41.0-py39he621ea3_0 
  lxml                                 4.9.1-py39h1edc446_0 --> 4.9.3-py39hdbbb534_0 
  markupsafe                           2.0.1-py39h27cfd23_0 --> 2.1.1-py39h7f8727e_0 
  matplotlib                           3.6.2-py39h06a4308_0 --> 3.7.2-py39h06a4308_0 
  matplotlib-base                      3.6.2-py39h945d387_0 --> 3.7.2-py39h1128e8f_0 
  mkl                                 2021.4.0-h06a4308_640 --> 2023.1.0-h213fc3f_46343 
  mkl-service                          2.4.0-py39h7f8727e_0 --> 2.4.0-py39h5eee18b_1 
  mkl_fft                              1.3.1-py39hd3c417c_0 --> 1.3.8-py39h5eee18b_0 
  mkl_random                           1.2.2-py39h51133e4_0 --> 1.2.4-py39hdb19cb5_0 
  mpich                                    3.3.2-hc856adb_0 --> 4.1.1-hbae89fd_0 
  mpmath                               1.2.1-py39h06a4308_0 --> 1.3.0-py39h06a4308_0 
  mypy_extensions                      0.4.3-py39h06a4308_1 --> 1.0.0-py39h06a4308_0 
  nbclassic                            0.4.8-py39h06a4308_0 --> 0.5.5-py39h06a4308_0 
  nbconvert                            6.4.4-py39h06a4308_0 --> 6.5.4-py39h06a4308_0 
  nbformat                             5.7.0-py39h06a4308_0 --> 5.9.2-py39h06a4308_0 
  networkx                             2.8.4-py39h06a4308_0 --> 3.1-py39h06a4308_0 
  nltk               pkgs/main/noarch::nltk-3.7-pyhd3eb1b0~ --> pkgs/main/linux-64::nltk-3.8.1-py39h06a4308_0 
  nspr                                      4.33-h295c915_0 --> 4.35-h6a678d5_0 
  nss                                       3.74-h0370c37_0 --> 3.89.1-h6a678d5_0 
  numba                               0.56.4-py39h417a72b_0 --> 0.58.0-py39h1128e8f_0 
  numexpr                              2.8.4-py39he184ba9_0 --> 2.8.7-py39h85018f9_0 
  numpy                               1.21.5-py39h6c91a56_3 --> 1.24.3-py39hf6e8229_1 
  numpy-base                          1.21.5-py39ha15fc14_3 --> 1.24.3-py39h060ed82_1 
  openssl                                 1.1.1s-h7f8727e_0 --> 3.0.11-h7f8727e_2 
  packaging                             22.0-py39h06a4308_0 --> 23.1-py39h06a4308_0 
  pandas                               1.4.4-py39h6a678d5_0 --> 2.0.3-py39h1128e8f_0 
  panel                               0.14.2-py39h06a4308_0 --> 1.2.3-py39h06a4308_0 
  param                               1.12.3-py39h06a4308_0 --> 1.13.0-py39h06a4308_0 
  partd              pkgs/main/noarch::partd-1.2.0-pyhd3eb~ --> pkgs/main/linux-64::partd-1.4.0-py39h06a4308_0 
  pillow                               9.3.0-py39h6a678d5_2 --> 10.0.1-py39ha6cbd5a_0 
  pip                                 22.3.1-py39h06a4308_0 --> 23.2.1-py39h06a4308_0 
  pkginfo                              1.8.3-py39h06a4308_0 --> 1.9.6-py39h06a4308_0 
  platformdirs                         2.5.2-py39h06a4308_0 --> 3.10.0-py39h06a4308_0 
  pycodestyle        pkgs/main/noarch::pycodestyle-2.8.0-p~ --> pkgs/main/linux-64::pycodestyle-2.10.0-py39h06a4308_0 
  pycosat                              0.6.4-py39h5eee18b_0 --> 0.6.6-py39h5eee18b_0 
  pycurl                              7.45.1-py39h8f2d780_0 --> 7.45.2-py39hdbd6064_1 
  pyflakes           pkgs/main/noarch::pyflakes-2.4.0-pyhd~ --> pkgs/main/linux-64::pyflakes-3.0.1-py39h06a4308_0 
  pygments           pkgs/main/noarch::pygments-2.11.2-pyh~ --> pkgs/main/linux-64::pygments-2.15.1-py39h06a4308_1 
  pylint                              2.14.5-py39h06a4308_0 --> 2.16.2-py39h06a4308_0 
  pyodbc                              4.0.34-py39h6a678d5_0 --> 4.0.39-py39h6a678d5_0 
  pyopenssl          pkgs/main/noarch::pyopenssl-22.0.0-py~ --> pkgs/main/linux-64::pyopenssl-23.2.0-py39h06a4308_0 
  pytables                             3.7.0-py39hf19a122_1 --> 3.8.0-py39hb8ae3fc_3 
  pytest                               7.1.2-py39h06a4308_0 --> 7.4.0-py39h06a4308_0 
  python                                  3.9.13-haa1d7c7_1 --> 3.9.18-h955ad1f_0 
  python-lsp-server                    1.5.0-py39h06a4308_0 --> 1.7.2-py39h06a4308_0 
  pytz                                2022.7-py39h06a4308_0 --> 2023.3.post1-py39h06a4308_0 
  pyviz_comms        pkgs/main/noarch::pyviz_comms-2.0.2-p~ --> pkgs/main/linux-64::pyviz_comms-2.3.0-py39h06a4308_0 
  pyzmq                               23.2.0-py39h6a678d5_0 --> 25.1.0-py39h6a678d5_0 
  qt-main                                 5.15.2-h327a75a_7 --> 5.15.2-h7358343_9 
  qt-webengine                            5.15.9-hd2b0992_4 --> 5.15.9-h9ab4d14_7 
  qtconsole                            5.3.2-py39h06a4308_0 --> 5.4.2-py39h06a4308_0 
  qtwebkit                                 5.212-h4eab89a_4 --> 5.212-h3fafdc1_5 
  queuelib                             1.5.0-py39h06a4308_0 --> 1.6.2-py39h06a4308_0 
  regex                             2022.7.9-py39h5eee18b_0 --> 2023.10.3-py39h5eee18b_0 
  requests                            2.28.1-py39h06a4308_0 --> 2.31.0-py39h06a4308_0 
  rope               pkgs/main/noarch::rope-0.22.0-pyhd3eb~ --> pkgs/main/linux-64::rope-1.7.0-py39h06a4308_0 
  scikit-learn                         1.0.2-py39h51133e4_1 --> 1.3.0-py39h1128e8f_0 
  scikit-learn-inte~                2021.6.0-py39h06a4308_0 --> 2023.1.1-py39h06a4308_0 
  scipy                                1.7.3-py39hc147768_0 --> 1.11.3-py39h5f9d8c6_0 
  scrapy                               2.6.2-py39h06a4308_0 --> 2.8.0-py39h06a4308_0 
  secretstorage                        3.3.1-py39h06a4308_0 --> 3.3.1-py39h06a4308_1 
  setuptools                          65.6.3-py39h06a4308_0 --> 68.0.0-py39h06a4308_0 
  soupsieve                      2.3.2.post1-py39h06a4308_0 --> 2.5-py39h06a4308_0 
  spyder                               5.3.3-py39h06a4308_0 --> 5.4.3-py39h06a4308_1 
  spyder-kernels                       2.3.3-py39h06a4308_0 --> 2.4.4-py39h06a4308_0 
  sqlalchemy                          1.4.39-py39h5eee18b_0 --> 2.0.21-py39h5eee18b_0 
  sqlite                                  3.40.1-h5082296_0 --> 3.41.2-h5eee18b_0 
  statsmodels                         0.13.5-py39h7deecbd_0 --> 0.14.0-py39ha9d4c09_0 
  tbb                                   2021.6.0-hdb19cb5_1 --> 2021.8.0-hdb19cb5_0 
  tbb4py                            2021.6.0-py39hdb19cb5_1 --> 2021.8.0-py39hdb19cb5_0 
  tenacity                             8.0.1-py39h06a4308_1 --> 8.2.2-py39h06a4308_0 
  tifffile           pkgs/main/noarch::tifffile-2021.7.2-p~ --> pkgs/main/linux-64::tifffile-2023.4.12-py39h06a4308_0 
  tornado                                6.2-py39h5eee18b_0 --> 6.3.3-py39h5eee18b_0 
  tqdm                                4.64.1-py39h06a4308_0 --> 4.65.0-py39hb070fc8_0 
  twisted                             22.2.0-py39h5eee18b_1 --> 22.10.0-py39h5eee18b_0 
  typing-extensions                    4.4.0-py39h06a4308_0 --> 4.7.1-py39h06a4308_0 
  typing_extensions                    4.4.0-py39h06a4308_0 --> 4.7.1-py39h06a4308_0 
  tzdata                                   2022g-h04d1e81_0 --> 2023c-h04d1e81_0 
  urllib3                            1.26.14-py39h06a4308_0 --> 1.26.16-py39h06a4308_0 
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd~ --> pkgs/main/linux-64::werkzeug-2.2.3-py39h06a4308_0 
  wget                                    1.21.3-h0b77cf5_0 --> 1.21.4-h251f7ec_1 
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3e~ --> pkgs/main/linux-64::wheel-0.41.2-py39h06a4308_0 
  widgetsnbextension                   3.5.2-py39h06a4308_0 --> 4.0.5-py39h06a4308_0 
  xarray                           2022.11.0-py39h06a4308_0 --> 2023.6.0-py39h06a4308_0 
  xlrd                                   2.0.1-pyhd3eb1b0_0 --> 2.0.1-pyhd3eb1b0_1 
  xlsxwriter         pkgs/main/noarch::xlsxwriter-3.0.3-py~ --> pkgs/main/linux-64::xlsxwriter-3.1.1-py39h06a4308_0 
  xz                                      5.2.10-h5eee18b_1 --> 5.4.2-h5eee18b_0 
  zfp                                      0.5.5-h295c915_6 --> 1.0.0-h6a678d5_0 
  zict                                 2.1.0-py39h06a4308_0 --> 3.0.0-py39h06a4308_0 
  zstandard                           0.18.0-py39h5eee18b_0 --> 0.19.0-py39h5eee18b_0 
  zstd                                     1.5.2-ha4553b6_0 --> 1.5.5-hc292b87_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages
ypy-websocket-0.8.2  | 26 KB     | ############################################################################################################################################################################################# | 100% 
                                                                                                                                                                                                                                        
Preparing transaction: done                                                                                                                                                                                                             
Verifying transaction: done                                                                                                                                                                                                             
Executing transaction: /                                                                                                                                                                                                                
                                                                                                                                                                                                                                        
    Installed package of scikit-learn can be accelerated using scikit-learn-intelex.                                                                                                                                                    
    More details are available here: https://intel.github.io/scikit-learn-intelex                                                                                                                                                       
                                                                                                                                                                                                                                        
    For example:                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
        $ conda install scikit-learn-intelex                                                                                                                                                                                            
        $ python -m sklearnex my_application.py                                                                                                                                                                                         
                      
    
                                                                                                                                                                                                                                      done
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda update python
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3

  added / updated specs:
    - python


The following packages will be DOWNGRADED:

  dill                                 0.3.7-py39h06a4308_0 --> 0.3.6-py39h06a4308_0 
  queuelib                             1.6.2-py39h06a4308_0 --> 1.5.0-py39h06a4308_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.9.18
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda upgrade python
Collecting package metadata (current_repodata.json): done
Solving environment: done

# All requested packages already installed.

(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.9.18
(base) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda deactivate
willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda activate dasci
WARNING: overwriting environment variables set in the machine
overwriting variable ['PATH']
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.10.9
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda update python
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/dasci

  added / updated specs:
    - python


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    attrs-23.1.0               |  py310h06a4308_0         141 KB
    beautifulsoup4-4.12.2      |  py310h06a4308_0         212 KB
    certifi-2023.7.22          |  py310h06a4308_0         153 KB
    debugpy-1.6.7              |  py310h6a678d5_0         2.0 MB
    exceptiongroup-1.0.4       |  py310h06a4308_0          28 KB
    ipykernel-6.25.0           |  py310h2f386ee_0         231 KB
    ipython-8.15.0             |  py310h06a4308_0         1.1 MB
    jsonschema-4.17.3          |  py310h06a4308_0         142 KB
    jupyter_client-8.1.0       |  py310h06a4308_0         180 KB
    jupyter_core-5.3.0         |  py310h06a4308_0          89 KB
    jupyter_events-0.6.3       |  py310h06a4308_0          37 KB
    jupyter_server-2.5.0       |  py310h06a4308_0         467 KB
    jupyter_server_terminals-0.4.4|  py310h06a4308_1          24 KB
    lxml-4.9.3                 |  py310hdbbb534_0         1.5 MB
    mkl-service-2.4.0          |  py310h5eee18b_1          54 KB
    mkl_fft-1.3.8              |  py310h5eee18b_0         216 KB
    mkl_random-1.2.4           |  py310hdb19cb5_0         312 KB
    nbclassic-0.5.5            |  py310h06a4308_0         6.1 MB
    nbformat-5.9.2             |  py310h06a4308_0         136 KB
    numexpr-2.8.7              |  py310h85018f9_0         141 KB
    numpy-1.26.0               |  py310h5f9d8c6_0          10 KB
    numpy-base-1.26.0          |  py310hb5e798b_0         7.1 MB
    packaging-23.1             |  py310h06a4308_0          78 KB
    pandas-2.0.3               |  py310h1128e8f_0        12.3 MB
    pillow-10.0.1              |  py310ha6cbd5a_0         748 KB
    platformdirs-3.10.0        |  py310h06a4308_0          33 KB
    pyarrow-11.0.0             |  py310h468efa6_1         4.2 MB
    pygments-2.15.1            |  py310h06a4308_1         1.8 MB
    python-3.10.13             |       h955ad1f_0        26.8 MB
    python-json-logger-2.0.7   |  py310h06a4308_0          16 KB
    pytz-2023.3.post1          |  py310h06a4308_0         210 KB
    pyzmq-25.1.0               |  py310h6a678d5_0         462 KB
    rfc3339-validator-0.1.4    |  py310h06a4308_0           9 KB
    rfc3986-validator-0.1.1    |  py310h06a4308_0           9 KB
    setuptools-68.0.0          |  py310h06a4308_0         936 KB
    soupsieve-2.5              |  py310h06a4308_0          70 KB
    tornado-6.3.3              |  py310h5eee18b_0         644 KB
    typing-extensions-4.7.1    |  py310h06a4308_0           9 KB
    typing_extensions-4.7.1    |  py310h06a4308_0          55 KB
    wheel-0.41.2               |  py310h06a4308_0         109 KB
    ------------------------------------------------------------
                                           Total:        68.7 MB

The following NEW packages will be INSTALLED:

  cyrus-sasl         pkgs/main/linux-64::cyrus-sasl-2.1.28-h52b45da_1 
  exceptiongroup     pkgs/main/linux-64::exceptiongroup-1.0.4-py310h06a4308_0 
  jupyter_events     pkgs/main/linux-64::jupyter_events-0.6.3-py310h06a4308_0 
  jupyter_server_te~ pkgs/main/linux-64::jupyter_server_terminals-0.4.4-py310h06a4308_1 
  libclang13         pkgs/main/linux-64::libclang13-14.0.6-default_he11475f_1 
  libcups            pkgs/main/linux-64::libcups-2.4.2-h2d74bed_1 
  libllvm14          pkgs/main/linux-64::libllvm14-14.0.6-hdb19cb5_3 
  mysql              pkgs/main/linux-64::mysql-5.7.24-h721c034_2 
  openjpeg           pkgs/main/linux-64::openjpeg-2.4.0-h3ad879b_0 
  python-json-logger pkgs/main/linux-64::python-json-logger-2.0.7-py310h06a4308_0 
  python-tzdata      pkgs/main/noarch::python-tzdata-2023.3-pyhd3eb1b0_0 
  rfc3339-validator  pkgs/main/linux-64::rfc3339-validator-0.1.4-py310h06a4308_0 
  rfc3986-validator  pkgs/main/linux-64::rfc3986-validator-0.1.1-py310h06a4308_0 
  tbb                pkgs/main/linux-64::tbb-2021.8.0-hdb19cb5_0 

The following packages will be REMOVED:

  flit-core-3.6.0-pyhd3eb1b0_0
  libllvm10-10.0.1-hbcb73fb_5

The following packages will be UPDATED:

  arrow-cpp                           8.0.0-py310h3098874_0 --> 11.0.0-h374c478_2 
  attrs                              22.1.0-py310h06a4308_0 --> 23.1.0-py310h06a4308_0 
  aws-c-common                            0.4.57-he6710b0_1 --> 0.6.8-h5eee18b_1 
  aws-c-event-stream                       0.1.6-h2531618_5 --> 0.1.6-h6a678d5_6 
  aws-checksums                            0.1.9-he6710b0_0 --> 0.1.11-h5eee18b_2 
  aws-sdk-cpp                            1.8.185-hce553d0_0 --> 1.8.185-h721c034_1 
  beautifulsoup4                     4.11.1-py310h06a4308_0 --> 4.12.2-py310h06a4308_0 
  c-ares                                  1.18.1-h7f8727e_0 --> 1.19.1-h5eee18b_0 
  ca-certificates                     2023.01.10-h06a4308_0 --> 2023.08.22-h06a4308_0 
  certifi                         2022.12.7-py310h06a4308_0 --> 2023.7.22-py310h06a4308_0 
  debugpy                             1.5.1-py310h295c915_0 --> 1.6.7-py310h6a678d5_0 
  expat                                    2.4.9-h6a678d5_0 --> 2.5.0-h6a678d5_0 
  fontconfig                              2.14.1-h52c9d5c_1 --> 2.14.1-h4c34cd2_2 
  giflib                                   5.2.1-h5eee18b_1 --> 5.2.1-h5eee18b_3 
  grpc-cpp                                1.46.1-h33aed49_1 --> 1.48.2-he1ff14a_1 
  gst-plugins-base                        1.14.0-h8213a91_2 --> 1.14.1-h6a678d5_1 
  gstreamer                               1.14.0-h28cd5cc_2 --> 1.14.1-h5eee18b_1 
  intel-openmp                       2021.4.0-h06a4308_3561 --> 2023.1.0-hdb19cb5_46305 
  ipykernel                          6.19.2-py310h2f386ee_0 --> 6.25.0-py310h2f386ee_0 
  ipython                             8.8.0-py310h06a4308_0 --> 8.15.0-py310h06a4308_0 
  jpeg                                        9e-h7f8727e_0 --> 9e-h5eee18b_1 
  jsonschema                         4.16.0-py310h06a4308_0 --> 4.17.3-py310h06a4308_0 
  jupyter_client                      7.4.8-py310h06a4308_0 --> 8.1.0-py310h06a4308_0 
  jupyter_core                        5.1.1-py310h06a4308_0 --> 5.3.0-py310h06a4308_0 
  jupyter_server                     1.23.4-py310h06a4308_0 --> 2.5.0-py310h06a4308_0 
  krb5                                    1.19.4-h568e23c_0 --> 1.20.1-h143b758_1 
  libclang                        10.0.1-default_hb85057a_2 --> 14.0.6-default_hc6dbbc7_1 
  libcurl                                 7.87.0-h91b91d3_0 --> 8.4.0-h251f7ec_0 
  libdeflate                                 1.8-h7f8727e_5 --> 1.17-h5eee18b_1 
  libevent                                2.1.12-h8f2d780_0 --> 2.1.12-hdbd6064_1 
  libffi                                   3.4.2-h6a678d5_6 --> 3.4.4-h6a678d5_0 
  libidn2                                  2.3.2-h7f8727e_0 --> 2.3.4-h5eee18b_0 
  libnghttp2                              1.46.0-hce63b2e_0 --> 1.57.0-h2d74bed_0 
  libpng                                  1.6.37-hbc83047_0 --> 1.6.39-h5eee18b_0 
  libpq                                     12.9-h16c4e8d_3 --> 12.15-hdbd6064_1 
  libssh2                                 1.10.0-h8f2d780_0 --> 1.10.0-hdbd6064_2 
  libthrift                               0.15.0-hcc01f38_0 --> 0.15.0-h1795dd8_2 
  libtiff                                  4.5.0-h6a678d5_1 --> 4.5.1-h6a678d5_0 
  libwebp                                  1.2.4-h11a3e52_0 --> 1.3.2-h11a3e52_0 
  libwebp-base                             1.2.4-h5eee18b_0 --> 1.3.2-h5eee18b_0 
  libxkbcommon                             1.0.1-hfa300c1_0 --> 1.0.1-h5eee18b_1 
  libxml2                                 2.9.14-h74e7548_0 --> 2.10.4-hcbfbd50_0 
  libxslt                                 1.1.35-h4e12654_0 --> 1.1.37-h2085143_0 
  lxml                                4.9.1-py310h1edc446_0 --> 4.9.3-py310hdbbb534_0 
  mkl                                 2021.4.0-h06a4308_640 --> 2023.1.0-h213fc3f_46343 
  mkl-service                         2.4.0-py310h7f8727e_0 --> 2.4.0-py310h5eee18b_1 
  mkl_fft                             1.3.1-py310hd6ae3a3_0 --> 1.3.8-py310h5eee18b_0 
  mkl_random                          1.2.2-py310h00e6091_0 --> 1.2.4-py310hdb19cb5_0 
  nbclassic                           0.4.8-py310h06a4308_0 --> 0.5.5-py310h06a4308_0 
  nbformat                            5.7.0-py310h06a4308_0 --> 5.9.2-py310h06a4308_0 
  nspr                                      4.33-h295c915_0 --> 4.35-h6a678d5_0 
  nss                                       3.74-h0370c37_0 --> 3.89.1-h6a678d5_0 
  numexpr                             2.8.4-py310h8879344_0 --> 2.8.7-py310h85018f9_0 
  numpy                              1.23.5-py310hd5efca6_0 --> 1.26.0-py310h5f9d8c6_0 
  numpy-base                         1.23.5-py310h8e6c178_0 --> 1.26.0-py310hb5e798b_0 
  openssl                                 1.1.1s-h7f8727e_0 --> 3.0.11-h7f8727e_2 
  orc                                      1.7.4-h07ed6aa_0 --> 1.7.4-hb3bc3d3_1 
  packaging                            22.0-py310h06a4308_0 --> 23.1-py310h06a4308_0 
  pandas                              1.5.2-py310h1128e8f_0 --> 2.0.3-py310h1128e8f_0 
  pillow                              9.3.0-py310h6a678d5_2 --> 10.0.1-py310ha6cbd5a_0 
  platformdirs                        2.5.2-py310h06a4308_0 --> 3.10.0-py310h06a4308_0 
  pyarrow                             8.0.0-py310h468efa6_0 --> 11.0.0-py310h468efa6_1 
  pygments           pkgs/main/noarch::pygments-2.11.2-pyh~ --> pkgs/main/linux-64::pygments-2.15.1-py310h06a4308_1 
  python                                  3.10.9-h7a1cb2a_0 --> 3.10.13-h955ad1f_0 
  pytz                               2022.7-py310h06a4308_0 --> 2023.3.post1-py310h06a4308_0 
  pyzmq                              23.2.0-py310h6a678d5_0 --> 25.1.0-py310h6a678d5_0 
  qt-main                                 5.15.2-h327a75a_7 --> 5.15.2-h7358343_9 
  qt-webengine                            5.15.9-hd2b0992_4 --> 5.15.9-h9ab4d14_7 
  qtwebkit                                 5.212-h4eab89a_4 --> 5.212-h3fafdc1_5 
  setuptools                         65.6.3-py310h06a4308_0 --> 68.0.0-py310h06a4308_0 
  soupsieve                     2.3.2.post1-py310h06a4308_0 --> 2.5-py310h06a4308_0 
  sqlite                                  3.40.1-h5082296_0 --> 3.41.2-h5eee18b_0 
  tornado                               6.2-py310h5eee18b_0 --> 6.3.3-py310h5eee18b_0 
  typing-extensions                   4.4.0-py310h06a4308_0 --> 4.7.1-py310h06a4308_0 
  typing_extensions                   4.4.0-py310h06a4308_0 --> 4.7.1-py310h06a4308_0 
  tzdata                                   2022g-h04d1e81_0 --> 2023c-h04d1e81_0 
  wget                                    1.21.3-h0b77cf5_0 --> 1.21.4-h251f7ec_1 
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3e~ --> pkgs/main/linux-64::wheel-0.41.2-py310h06a4308_0 
  xz                                      5.2.10-h5eee18b_1 --> 5.4.2-h5eee18b_0 
  zstd                                     1.5.2-ha4553b6_0 --> 1.5.5-hc292b87_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                                                                                        
Preparing transaction: done                                                                                                                                                                                                             
Verifying transaction: done                                                                                                                                                                                                             
Executing transaction: done                                                                                                                                                                                                             
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ python --version                                                                                                                                                 
Python 3.10.13                                                                                                                                                                                                                          
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ conda update conda
                                                                                                                                                                                                                                        
PackageNotInstalledError: Package is not installed in prefix.                                                                                                                                                                           
  prefix: /home/willem/anaconda3/envs/dasci                                                                                                                                                                                             
  package name: conda                                                                                                                                                                                                                   
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ 

```

## Testing the dasci environment with the jupyter notebook of ~/Documents/zakelijk/financieel/ING/transacties
It turns out that the new Spark 3.4.0 installation doesn't work with the current dasci package configuration, with
only the python version updated.

However, when I force the Spark version back to 3.3.1 on the SDKMan per session base the problems disappear:
```bash
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ sdk current spark

Using spark version 3.4.0
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ sdk use spark 3.3.1

Using spark version 3.3.1 in this shell.
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv PATH
/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ jupyter notebook
[I 22:48:10.159 NotebookApp] [nb_conda_kernels] enabled, 2 kernels found
[I 22:48:10.318 NotebookApp] [jupyter_nbextensions_configurator] enabled 0.4.1
[I 22:48:10.322 NotebookApp] Serving notebooks from local directory: /home/willem/Documents/zakelijk/financieel/ING/transacties
[I 22:48:10.322 NotebookApp] Jupyter Notebook 6.5.2 is running at:
[I 22:48:10.322 NotebookApp] http://localhost:8888/?token=b787f139d077098c6ca7761413a6b70f4ccd6bbe1b3860c1
[I 22:48:10.322 NotebookApp]  or http://127.0.0.1:8888/?token=b787f139d077098c6ca7761413a6b70f4ccd6bbe1b3860c1
[I 22:48:10.322 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 22:48:10.333 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/willem/.local/share/jupyter/runtime/nbserver-39636-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=b787f139d077098c6ca7761413a6b70f4ccd6bbe1b3860c1
     or http://127.0.0.1:8888/?token=b787f139d077098c6ca7761413a6b70f4ccd6bbe1b3860c1


```

The new plan is to force the old dasci environment to keep using the SDKMan Spark 3.3.1 installation and create a whole
new environment with the latest python and other package dependencies and hope it will work well together.
Basically we had to redo the following commands to permanently fix the dasci environment.
```bash
conda env config vars set SPARK_HOME=$SDKMAN_CANDIDATES_DIR/spark/3.3.1
conda activate dasci
conda env config vars set PATH=/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:$JAVA_HOME/bin:$SPARK_HOME/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
To make your changes take effect please reactivate your environment
conda activate dasci
```

In full:
```bash
WARNING: overwriting environment variables set in the machine
overwriting variable ['SPARK_HOME', 'PATH']
(dasci) willem@linux-laptop:~/git/DataAnalysisWithPythonAndPySpark$ cd ~/Documents/zakelijk/financieel/ING/transacties/
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ sdk current spark

Using spark version 3.4.0
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv SPARK_HOME
/home/willem/.sdkman/candidates/spark/current
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ sdk list spark
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv PATH
/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/.sdkman/candidates/spark/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ conda env config vars set SPARK_HOME=$SDKMAN_CANDIDATES_DIR/spark/3.3.1
To make your changes take effect please reactivate your environment
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ conda activate dasci
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv SPARK_HOME
/home/willem/.sdkman/candidates/spark/3.3.1
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv PATH
/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/.sdkman/candidates/spark/current/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ conda env config vars set PATH=/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:$JAVA_HOME/bin:$SPARK_HOME/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
To make your changes take effect please reactivate your environment
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ conda activate dasci
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ printenv PATH
/home/willem/anaconda3/envs/dasci/bin:/home/willem/anaconda3/condabin:/home/willem/.sdkman/candidates/java/current/bin:/home/willem/.sdkman/candidates/spark/3.3.1/bin:/home/willem/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/willem/.local/share/JetBrains/Toolbox/scripts
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ sdk current spark

Using spark version 3.3.1
(dasci) willem@linux-laptop:~/Documents/zakelijk/financieel/ING/transacties$ jupyter notebook

```

This was successful in opening and recalculating the appropriate jupyter notebook file.

We now have to create a new anaconda environment based on the most recent python version and try to match package 
versions with Spark 3.4.0.
Starting with 
- `conda create -n py3.11-spark3.4 python=3.11 anaconda`
- [https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html)
- [https://spark.apache.org/docs/latest/api/python/getting_started/install.html](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
- [https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html)

Also the warning
```bash
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/home/willem/anaconda3/envs/dasci/lib/python3.10/site-packages/pyspark/jars/spark-unsafe_2.12-3.2.1.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
```
Should be resolved in the new Spark 3.4.0 so it works fine with Java 11
- [https://issues.apache.org/jira/browse/SYSTEMDS-3229](https://issues.apache.org/jira/browse/SYSTEMDS-3229)