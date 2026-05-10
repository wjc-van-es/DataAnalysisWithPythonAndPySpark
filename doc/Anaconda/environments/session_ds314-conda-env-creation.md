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

# Session `ds314` conda env creation

## commands with output
```bash
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda create -n ds314
Retrieving notices: done
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314



Proceed ([y]/n)? 


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate ds314
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 python=3.14
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - python=3.14


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pip-26.0.1                 |     pyh0d26453_1         1.1 MB
    python-3.14.4              |h490e9c7_100_cp314        35.1 MB
    python_abi-3.14            |          2_cp314           6 KB
    ------------------------------------------------------------
                                           Total:        36.2 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_6 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2026.3.19-h06a4308_0 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.44-h9e0c5a2_3 
  libexpat           pkgs/main/linux-64::libexpat-2.8.0-h7354ed3_0 
  libffi             pkgs/main/linux-64::libffi-3.4.8-hc5d346e_2 
  libgcc             pkgs/main/linux-64::libgcc-15.2.0-h69a1729_7 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-15.2.0-h166f726_7 
  libgomp            pkgs/main/linux-64::libgomp-15.2.0-h4751f2c_7 
  libmpdec           pkgs/main/linux-64::libmpdec-4.0.0-h5eee18b_0 
  libstdcxx          pkgs/main/linux-64::libstdcxx-15.2.0-h39759b7_7 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-15.2.0-hc03a8fd_7 
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  libxcb             pkgs/main/linux-64::libxcb-1.17.0-h9b100fa_0 
  libzlib            pkgs/main/linux-64::libzlib-1.3.1-h47b2149_1 
  lz4-c              pkgs/main/linux-64::lz4-c-1.9.4-h6a678d5_1 
  ncurses            pkgs/main/linux-64::ncurses-6.5-h7934f7d_0 
  openssl            pkgs/main/linux-64::openssl-3.5.6-h1b28b03_0 
  pip                pkgs/main/noarch::pip-26.0.1-pyh0d26453_1 
  pthread-stubs      pkgs/main/linux-64::pthread-stubs-0.3-h0ce48e5_1 
  python             pkgs/main/linux-64::python-3.14.4-h490e9c7_100_cp314 
  python_abi         pkgs/main/linux-64::python_abi-3.14-2_cp314 
  readline           pkgs/main/linux-64::readline-8.3-hc2a1206_0 
  sqlite             pkgs/main/linux-64::sqlite-3.51.2-h3e8d24a_0 
  tk                 pkgs/main/linux-64::tk-8.6.15-h54e0aa7_0 
  tzdata             pkgs/main/noarch::tzdata-2026a-he532380_0 
  xorg-libx11        pkgs/main/linux-64::xorg-libx11-1.8.12-h9b100fa_1 
  xorg-libxau        pkgs/main/linux-64::xorg-libxau-1.0.12-h9b100fa_0 
  xorg-libxdmcp      pkgs/main/linux-64::xorg-libxdmcp-1.1.5-h9b100fa_0 
  xorg-xorgproto     pkgs/main/linux-64::xorg-xorgproto-2024.1-h5eee18b_1 
  xz                 pkgs/main/linux-64::xz-5.8.2-h448239c_0 
  zlib               pkgs/main/linux-64::zlib-1.3.1-h47b2149_1 
  zstd               pkgs/main/linux-64::zstd-1.5.7-h11fc155_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.14.4
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ which python
/home/willem/anaconda3/envs/ds314/bin/python
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 pyspark
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - pyspark


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    blas-1.0                   |              mkl           6 KB
    bottleneck-1.4.2           |  py314h6a40391_1         135 KB
    gettext-0.25.1             |       hd8bbc44_1         523 KB
    gettext-tools-0.25.1       |       hecf7c64_1         3.3 MB
    icu-78.3                   |       h84d19a5_0        23.2 MB
    libasprintf-0.25.1         |       ha6c9436_1          51 KB
    libasprintf-devel-0.25.1   |       ha6c9436_1          33 KB
    libcurl-8.20.0             |       hd8fa685_1         491 KB
    libgettextpo-0.25.1        |       h64fc44f_1         186 KB
    libgettextpo-devel-0.25.1  |       h64fc44f_1          35 KB
    libnghttp2-1.69.0          |       hc59f8b6_0         647 KB
    libxml2-2.14.4             |       h4481af1_1         645 KB
    mkl-service-2.5.2          |  py314hacdc0fc_0          77 KB
    mkl_fft-2.2.0              |  py314hc849d88_0         180 KB
    mkl_random-1.3.0           |  py314hda4e5d8_0         312 KB
    numexpr-2.14.1             |  py314hee8fbad_1         212 KB
    numpy-2.4.4                |  py314hc4ca38b_1          20 KB
    numpy-base-2.4.4           |  py314h7c74580_1         8.2 MB
    pandas-2.3.3               |  py314hda4e5d8_1        14.5 MB
    py4j-0.10.9.9              |  py314h06a4308_0         299 KB
    pyarrow-23.0.1             |cpu_py314h790a952_3         9.3 MB
    pyspark-4.1.1              |  py314h06a4308_0       429.2 MB
    python-dateutil-2.9.0post0 |  py314h06a4308_2         312 KB
    pytz-2026.1.post1          |  py314h06a4308_0         223 KB
    six-1.17.0                 |  py314h06a4308_0          39 KB
    ------------------------------------------------------------
                                           Total:       492.0 MB

The following NEW packages will be INSTALLED:

  arrow-cpp          pkgs/main/linux-64::arrow-cpp-23.0.1-cpu_h3e9d749_4 
  aws-c-auth         pkgs/main/linux-64::aws-c-auth-0.10.1-h47b2149_0 
  aws-c-cal          pkgs/main/linux-64::aws-c-cal-0.9.13-h1b28b03_0 
  aws-c-common       pkgs/main/linux-64::aws-c-common-0.12.6-h47b2149_0 
  aws-c-compression  pkgs/main/linux-64::aws-c-compression-0.3.2-h47b2149_0 
  aws-c-event-stream pkgs/main/linux-64::aws-c-event-stream-0.6.1-h47b2149_0 
  aws-c-http         pkgs/main/linux-64::aws-c-http-0.10.13-h47b2149_0 
  aws-c-io           pkgs/main/linux-64::aws-c-io-0.26.3-h1b29dbc_0 
  aws-c-mqtt         pkgs/main/linux-64::aws-c-mqtt-0.15.2-h47b2149_0 
  aws-c-s3           pkgs/main/linux-64::aws-c-s3-0.12.0-h1b28b03_1 
  aws-c-sdkutils     pkgs/main/linux-64::aws-c-sdkutils-0.2.4-h47b2149_2 
  aws-checksums      pkgs/main/linux-64::aws-checksums-0.2.10-h47b2149_0 
  aws-crt-cpp        pkgs/main/linux-64::aws-crt-cpp-0.37.4-h7354ed3_1 
  aws-sdk-cpp        pkgs/main/linux-64::aws-sdk-cpp-1.11.774-h8c0960e_1 
  blas               pkgs/main/linux-64::blas-1.0-mkl 
  bottleneck         pkgs/main/linux-64::bottleneck-1.4.2-py314h6a40391_1 
  c-ares             pkgs/main/linux-64::c-ares-1.34.6-hd44998d_0 
  gettext            pkgs/main/linux-64::gettext-0.25.1-hd8bbc44_1 
  gettext-tools      pkgs/main/linux-64::gettext-tools-0.25.1-hecf7c64_1 
  gflags             pkgs/main/linux-64::gflags-2.3.0-h861b1fb_0 
  glog               pkgs/main/linux-64::glog-0.7.1-h485759d_0 
  icu                pkgs/main/linux-64::icu-78.3-h84d19a5_0 
  intel-openmp       pkgs/main/linux-64::intel-openmp-2025.0.0-h06a4308_1171 
  jansson            pkgs/main/linux-64::jansson-2.14-h5eee18b_1 
  libabseil          pkgs/main/linux-64::libabseil-20260107.0-cxx17_h6199ee8_0 
  libasprintf        pkgs/main/linux-64::libasprintf-0.25.1-ha6c9436_1 
  libasprintf-devel  pkgs/main/linux-64::libasprintf-devel-0.25.1-ha6c9436_1 
  libbrotlicommon    pkgs/main/linux-64::libbrotlicommon-1.2.0-h32cd6e7_0 
  libbrotlidec       pkgs/main/linux-64::libbrotlidec-1.2.0-ha2c5f68_0 
  libbrotlienc       pkgs/main/linux-64::libbrotlienc-1.2.0-h2e96acb_0 
  libcurl            pkgs/main/linux-64::libcurl-8.20.0-hd8fa685_1 
  libev              pkgs/main/linux-64::libev-4.33-h7f8727e_1 
  libevent           pkgs/main/linux-64::libevent-2.1.12-hdbd6064_1 
  libgettextpo       pkgs/main/linux-64::libgettextpo-0.25.1-h64fc44f_1 
  libgettextpo-devel pkgs/main/linux-64::libgettextpo-devel-0.25.1-h64fc44f_1 
  libgrpc            pkgs/main/linux-64::libgrpc-1.78.0-h79c45ec_0 
  libiconv           pkgs/main/linux-64::libiconv-1.18-h75a1612_0 
  libidn2            pkgs/main/linux-64::libidn2-2.3.8-hf80d704_0 
  libkrb5            pkgs/main/linux-64::libkrb5-1.22.1-h869c75e_1 
  libnghttp2         pkgs/main/linux-64::libnghttp2-1.69.0-hc59f8b6_0 
  libprotobuf        pkgs/main/linux-64::libprotobuf-6.33.5-h4435b4a_0 
  libre2-11          pkgs/main/linux-64::libre2-11-2025.11.05-h3356fce_1 
  libssh2            pkgs/main/linux-64::libssh2-1.11.1-h251f7ec_0 
  libthrift          pkgs/main/linux-64::libthrift-0.22.0-hd8eb582_0 
  libunistring       pkgs/main/linux-64::libunistring-1.4.2-h34b0ebb_0 
  libxml2            pkgs/main/linux-64::libxml2-2.14.4-h4481af1_1 
  lmdb               pkgs/main/linux-64::lmdb-0.9.31-hb25bd0a_0 
  mkl                pkgs/main/linux-64::mkl-2025.0.0-hacee8c2_941 
  mkl-service        pkgs/main/linux-64::mkl-service-2.5.2-py314hacdc0fc_0 
  mkl_fft            pkgs/main/linux-64::mkl_fft-2.2.0-py314hc849d88_0 
  mkl_random         pkgs/main/linux-64::mkl_random-1.3.0-py314hda4e5d8_0 
  numexpr            pkgs/main/linux-64::numexpr-2.14.1-py314hee8fbad_1 
  numpy              pkgs/main/linux-64::numpy-2.4.4-py314hc4ca38b_1 
  numpy-base         pkgs/main/linux-64::numpy-base-2.4.4-py314h7c74580_1 
  orc                pkgs/main/linux-64::orc-2.2.0-haed8af1_2 
  pandas             pkgs/main/linux-64::pandas-2.3.3-py314hda4e5d8_1 
  py4j               pkgs/main/linux-64::py4j-0.10.9.9-py314h06a4308_0 
  pyarrow            pkgs/main/linux-64::pyarrow-23.0.1-cpu_py314h790a952_3 
  pyspark            pkgs/main/linux-64::pyspark-4.1.1-py314h06a4308_0 
  python-dateutil    pkgs/main/linux-64::python-dateutil-2.9.0post0-py314h06a4308_2 
  python-tzdata      pkgs/main/noarch::python-tzdata-2026.2-pyhd3eb1b0_0 
  pytz               pkgs/main/linux-64::pytz-2026.1.post1-py314h06a4308_0 
  re2                pkgs/main/linux-64::re2-2025.11.05-h71b5c5c_1 
  s2n                pkgs/main/linux-64::s2n-1.6.2-h02aa81b_0 
  six                pkgs/main/linux-64::six-1.17.0-py314h06a4308_0 
  snappy             pkgs/main/linux-64::snappy-1.2.2-h4bcf44c_1 
  tbb                pkgs/main/linux-64::tbb-2022.0.0-hdb19cb5_0 
  tbb-devel          pkgs/main/linux-64::tbb-devel-2022.0.0-hdb19cb5_0 
  utf8proc           pkgs/main/linux-64::utf8proc-2.6.1-h5eee18b_1 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done                                                                                                                                      
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314                                          
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 notebook                                                                  
Channels:             
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - notebook


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    anyio-4.12.1               |  py314h06a4308_0         330 KB
    argon2-cffi-25.1.0         |  py314h06a4308_0          35 KB
    argon2-cffi-bindings-25.1.0|  py314hee96239_0          36 KB
    asttokens-3.0.1            |  py314h06a4308_0          69 KB
    async-lru-2.0.5            |  py314h06a4308_0          24 KB
    attrs-26.1.0               |  py314h0c820a0_0         180 KB
    babel-2.17.0               |  py314h06a4308_0        13.3 MB
    beautifulsoup4-4.14.3      |  py314h06a4308_0         260 KB
    bleach-6.3.0               |  py314h06a4308_1          98 KB
    brotlicffi-1.2.0.0         |  py314h7354ed3_0         372 KB
    certifi-2026.4.22          |  py314h06a4308_0         133 KB
    cffi-2.0.0                 |  py314h4eded50_1         291 KB
    charset-normalizer-3.4.4   |  py314h06a4308_0         102 KB
    comm-0.2.3                 |  py314h06a4308_0          20 KB
    debugpy-1.8.16             |  py314hbdd6827_1         2.6 MB
    decorator-5.2.1            |  py314h06a4308_0          45 KB
    executing-2.2.1            |  py314h06a4308_0         324 KB
    h11-0.16.0                 |  py314h06a4308_1          66 KB
    httpcore-1.0.9             |  py314h06a4308_0         126 KB
    httpx-0.28.1               |  py314h06a4308_1         221 KB
    idna-3.11                  |  py314h06a4308_0         208 KB
    ipykernel-7.2.0            |  py314h6fa48dc_0         255 KB
    ipython-9.11.0             |  py314h06a4308_0         1.2 MB
    ipython_pygments_lexers-1.1.1|  py314h06a4308_0          20 KB
    jedi-0.19.2                |  py314h06a4308_0         1.1 MB
    jinja2-3.1.6               |  py314h06a4308_0         358 KB
    json5-0.12.1               |  py314h06a4308_0          71 KB
    jsonschema-4.25.1          |  py314h06a4308_0         198 KB
    jsonschema-specifications-2025.9.1|  py314h06a4308_0          17 KB
    jupyter-lsp-2.3.0          |  py314h06a4308_0         118 KB
    jupyter_client-8.8.0       |  py314h06a4308_0         245 KB
    jupyter_core-5.9.1         |  py314h06a4308_0          99 KB
    jupyter_events-0.12.1      |  py314h06a4308_0          45 KB
    jupyter_server-2.17.0      |  py314h06a4308_1         595 KB
    jupyter_server_terminals-0.5.4|  py314h06a4308_0          27 KB
    jupyterlab-4.5.7           |  py314h06a4308_0         8.5 MB
    jupyterlab_pygments-0.3.0  |  py314h06a4308_0          21 KB
    jupyterlab_server-2.28.0   |  py314h06a4308_1         123 KB
    markupsafe-3.0.2           |  py314h5eee18b_0          30 KB
    matplotlib-inline-0.2.1    |  py314h06a4308_0          20 KB
    mistune-3.1.2              |  py314h06a4308_0         147 KB
    nbclient-0.10.4            |  py314h06a4308_0          56 KB
    nbconvert-core-7.17.0      |  py314h06a4308_0         505 KB
    nbformat-5.10.4            |  py314h06a4308_0         153 KB
    nest-asyncio-1.5.1         |     pyhd3eb1b0_0          10 KB
    notebook-7.5.5             |  py314h06a4308_0         5.8 MB
    notebook-shim-0.2.4        |  py314h06a4308_1          26 KB
    packaging-26.0             |  py314h06a4308_0         202 KB
    pandocfilters-1.5.1        |  py314h06a4308_0          20 KB
    parso-0.8.5                |  py314h06a4308_0         233 KB
    pexpect-4.9.0              |  py314h06a4308_1         152 KB
    platformdirs-4.9.4         |  py314h06a4308_0          57 KB
    prometheus_client-0.24.1   |  py314h06a4308_0         172 KB
    prompt-toolkit-3.0.52      |  py314h06a4308_1         758 KB
    psutil-7.0.0               |  py314hee96239_1         546 KB
    pure_eval-0.2.3            |  py314h06a4308_0          37 KB
    pycparser-3.0              |  py314h06a4308_0         157 KB
    pygments-2.20.0            |  py314h06a4308_0         4.8 MB
    pysocks-1.7.1              |  py314h06a4308_1          35 KB
    python-fastjsonschema-2.21.2|  py314h06a4308_0         249 KB
    python-json-logger-4.0.0   |  py314h06a4308_0          36 KB
    pyyaml-6.0.3               |  py314h591646f_0         247 KB
    pyzmq-27.1.0               |  py314hcf8288c_1         384 KB
    referencing-0.37.0         |  py314h06a4308_0          82 KB
    requests-2.33.1            |  py314h06a4308_0         167 KB
    rfc3339-validator-0.1.4    |  py314h06a4308_0          10 KB
    rfc3986-validator-0.1.1    |  py314h06a4308_0          12 KB
    rpds-py-0.28.0             |  py314h498d7c9_0         331 KB
    send2trash-1.8.3           |  py314h06a4308_0          35 KB
    setuptools-82.0.1          |  py314h06a4308_0         1.6 MB
    soupsieve-2.5              |  py314h06a4308_0          93 KB
    stack_data-0.6.3           |  py314h06a4308_0          69 KB
    terminado-0.18.1           |  py314h06a4308_1          34 KB
    tinycss2-1.5.1             |  py314h06a4308_0         108 KB
    tornado-6.5.5              |  py314h47b2149_0         888 KB
    traitlets-5.14.3           |  py314h06a4308_0         221 KB
    typing-extensions-4.15.0   |  py314h06a4308_0          11 KB
    typing_extensions-4.15.0   |  py314h06a4308_0          99 KB
    urllib3-2.6.3              |  py314h06a4308_0         360 KB
    wcwidth-0.2.14             |  py314h06a4308_0          66 KB
    webencodings-0.5.1         |  py314h06a4308_2          28 KB
    websocket-client-1.8.0     |  py314h06a4308_0         117 KB
    ------------------------------------------------------------
                                           Total:        50.8 MB

The following NEW packages will be INSTALLED:

  anyio              pkgs/main/linux-64::anyio-4.12.1-py314h06a4308_0 
  argon2-cffi        pkgs/main/linux-64::argon2-cffi-25.1.0-py314h06a4308_0 
  argon2-cffi-bindi~ pkgs/main/linux-64::argon2-cffi-bindings-25.1.0-py314hee96239_0 
  asttokens          pkgs/main/linux-64::asttokens-3.0.1-py314h06a4308_0 
  async-lru          pkgs/main/linux-64::async-lru-2.0.5-py314h06a4308_0 
  attrs              pkgs/main/linux-64::attrs-26.1.0-py314h0c820a0_0 
  babel              pkgs/main/linux-64::babel-2.17.0-py314h06a4308_0 
  beautifulsoup4     pkgs/main/linux-64::beautifulsoup4-4.14.3-py314h06a4308_0 
  bleach             pkgs/main/linux-64::bleach-6.3.0-py314h06a4308_1 
  brotlicffi         pkgs/main/linux-64::brotlicffi-1.2.0.0-py314h7354ed3_0 
  certifi            pkgs/main/linux-64::certifi-2026.4.22-py314h06a4308_0 
  cffi               pkgs/main/linux-64::cffi-2.0.0-py314h4eded50_1 
  charset-normalizer pkgs/main/linux-64::charset-normalizer-3.4.4-py314h06a4308_0 
  comm               pkgs/main/linux-64::comm-0.2.3-py314h06a4308_0 
  debugpy            pkgs/main/linux-64::debugpy-1.8.16-py314hbdd6827_1 
  decorator          pkgs/main/linux-64::decorator-5.2.1-py314h06a4308_0 
  defusedxml         pkgs/main/noarch::defusedxml-0.7.1-pyhd3eb1b0_0 
  executing          pkgs/main/linux-64::executing-2.2.1-py314h06a4308_0 
  h11                pkgs/main/linux-64::h11-0.16.0-py314h06a4308_1 
  html5lib           pkgs/main/noarch::html5lib-1.1-pyhd3eb1b0_0 
  httpcore           pkgs/main/linux-64::httpcore-1.0.9-py314h06a4308_0 
  httpx              pkgs/main/linux-64::httpx-0.28.1-py314h06a4308_1 
  idna               pkgs/main/linux-64::idna-3.11-py314h06a4308_0 
  ipykernel          pkgs/main/linux-64::ipykernel-7.2.0-py314h6fa48dc_0 
  ipython            pkgs/main/linux-64::ipython-9.11.0-py314h06a4308_0 
  ipython_pygments_~ pkgs/main/linux-64::ipython_pygments_lexers-1.1.1-py314h06a4308_0 
  jedi               pkgs/main/linux-64::jedi-0.19.2-py314h06a4308_0 
  jinja2             pkgs/main/linux-64::jinja2-3.1.6-py314h06a4308_0 
  json5              pkgs/main/linux-64::json5-0.12.1-py314h06a4308_0 
  jsonschema         pkgs/main/linux-64::jsonschema-4.25.1-py314h06a4308_0 
  jsonschema-specif~ pkgs/main/linux-64::jsonschema-specifications-2025.9.1-py314h06a4308_0 
  jupyter-lsp        pkgs/main/linux-64::jupyter-lsp-2.3.0-py314h06a4308_0 
  jupyter_client     pkgs/main/linux-64::jupyter_client-8.8.0-py314h06a4308_0 
  jupyter_core       pkgs/main/linux-64::jupyter_core-5.9.1-py314h06a4308_0 
  jupyter_events     pkgs/main/linux-64::jupyter_events-0.12.1-py314h06a4308_0 
  jupyter_server     pkgs/main/linux-64::jupyter_server-2.17.0-py314h06a4308_1 
  jupyter_server_te~ pkgs/main/linux-64::jupyter_server_terminals-0.5.4-py314h06a4308_0 
  jupyterlab         pkgs/main/linux-64::jupyterlab-4.5.7-py314h06a4308_0 
  jupyterlab_pygmen~ pkgs/main/linux-64::jupyterlab_pygments-0.3.0-py314h06a4308_0 
  jupyterlab_server  pkgs/main/linux-64::jupyterlab_server-2.28.0-py314h06a4308_1 
  libsodium          pkgs/main/linux-64::libsodium-1.0.21-h81596b7_0 
  markupsafe         pkgs/main/linux-64::markupsafe-3.0.2-py314h5eee18b_0 
  matplotlib-inline  pkgs/main/linux-64::matplotlib-inline-0.2.1-py314h06a4308_0 
  mistune            pkgs/main/linux-64::mistune-3.1.2-py314h06a4308_0 
  nbclient           pkgs/main/linux-64::nbclient-0.10.4-py314h06a4308_0 
  nbconvert-core     pkgs/main/linux-64::nbconvert-core-7.17.0-py314h06a4308_0 
  nbformat           pkgs/main/linux-64::nbformat-5.10.4-py314h06a4308_0 
  nest-asyncio       pkgs/main/noarch::nest-asyncio-1.5.1-pyhd3eb1b0_0 
  notebook           pkgs/main/linux-64::notebook-7.5.5-py314h06a4308_0 
  notebook-shim      pkgs/main/linux-64::notebook-shim-0.2.4-py314h06a4308_1 
  packaging          pkgs/main/linux-64::packaging-26.0-py314h06a4308_0 
  pandocfilters      pkgs/main/linux-64::pandocfilters-1.5.1-py314h06a4308_0 
  parso              pkgs/main/linux-64::parso-0.8.5-py314h06a4308_0 
  pexpect            pkgs/main/linux-64::pexpect-4.9.0-py314h06a4308_1 
  platformdirs       pkgs/main/linux-64::platformdirs-4.9.4-py314h06a4308_0 
  prometheus_client  pkgs/main/linux-64::prometheus_client-0.24.1-py314h06a4308_0 
  prompt-toolkit     pkgs/main/linux-64::prompt-toolkit-3.0.52-py314h06a4308_1 
  prompt_toolkit     pkgs/main/noarch::prompt_toolkit-3.0.52-hd3eb1b0_1 
  psutil             pkgs/main/linux-64::psutil-7.0.0-py314hee96239_1 
  ptyprocess         pkgs/main/noarch::ptyprocess-0.7.0-pyhd3eb1b0_3 
  pure_eval          pkgs/main/linux-64::pure_eval-0.2.3-py314h06a4308_0 
  pycparser          pkgs/main/linux-64::pycparser-3.0-py314h06a4308_0 
  pygments           pkgs/main/linux-64::pygments-2.20.0-py314h06a4308_0 
  pysocks            pkgs/main/linux-64::pysocks-1.7.1-py314h06a4308_1 
  python-fastjsonsc~ pkgs/main/linux-64::python-fastjsonschema-2.21.2-py314h06a4308_0 
  python-json-logger pkgs/main/linux-64::python-json-logger-4.0.0-py314h06a4308_0 
  pyyaml             pkgs/main/linux-64::pyyaml-6.0.3-py314h591646f_0 
  pyzmq              pkgs/main/linux-64::pyzmq-27.1.0-py314hcf8288c_1 
  referencing        pkgs/main/linux-64::referencing-0.37.0-py314h06a4308_0 
  requests           pkgs/main/linux-64::requests-2.33.1-py314h06a4308_0 
  rfc3339-validator  pkgs/main/linux-64::rfc3339-validator-0.1.4-py314h06a4308_0 
  rfc3986-validator  pkgs/main/linux-64::rfc3986-validator-0.1.1-py314h06a4308_0 
  rpds-py            pkgs/main/linux-64::rpds-py-0.28.0-py314h498d7c9_0 
  send2trash         pkgs/main/linux-64::send2trash-1.8.3-py314h06a4308_0 
  setuptools         pkgs/main/linux-64::setuptools-82.0.1-py314h06a4308_0 
  soupsieve          pkgs/main/linux-64::soupsieve-2.5-py314h06a4308_0 
  stack_data         pkgs/main/linux-64::stack_data-0.6.3-py314h06a4308_0 
  terminado          pkgs/main/linux-64::terminado-0.18.1-py314h06a4308_1 
  tinycss2           pkgs/main/linux-64::tinycss2-1.5.1-py314h06a4308_0 
  tornado            pkgs/main/linux-64::tornado-6.5.5-py314h47b2149_0 
  traitlets          pkgs/main/linux-64::traitlets-5.14.3-py314h06a4308_0 
  typing-extensions  pkgs/main/linux-64::typing-extensions-4.15.0-py314h06a4308_0 
  typing_extensions  pkgs/main/linux-64::typing_extensions-4.15.0-py314h06a4308_0 
  urllib3            pkgs/main/linux-64::urllib3-2.6.3-py314h06a4308_0 
  wcwidth            pkgs/main/linux-64::wcwidth-0.2.14-py314h06a4308_0 
  webencodings       pkgs/main/linux-64::webencodings-0.5.1-py314h06a4308_2 
  websocket-client   pkgs/main/linux-64::websocket-client-1.8.0-py314h06a4308_0 
  yaml               pkgs/main/linux-64::yaml-0.2.5-h7b6447c_0 
  zeromq             pkgs/main/linux-64::zeromq-4.3.5-hf801bfb_2 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done                                                                                                                                      
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314                                                                   
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 matplotlib                                                                
Channels:             
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - matplotlib


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    contourpy-1.3.3            |  py314hdb19cb5_0        11.3 MB
    cycler-0.12.1              |  py314h06a4308_0          20 KB
    fontconfig-2.17.1          |       h062c814_0         269 KB
    fonttools-4.62.1           |  py314h47b2149_0         4.2 MB
    kiwisolver-1.4.9           |  py314h24d9097_0          76 KB
    libllvm21-21.1.8           |       h3801bc2_1        42.0 MB
    libxkbcommon-1.13.1        |       h13fa2f1_0         822 KB
    libxml2-2.14.4             |       h3457413_0         646 KB
    matplotlib-3.10.9          |  py314h06a4308_0           7 KB
    matplotlib-base-3.10.9     |  py314h54cb298_0         8.1 MB
    pillow-12.2.0              |  py314haa37d31_0        34.8 MB
    pyparsing-3.2.5            |  py314h06a4308_0         572 KB
    pyqt-6.11.0                |  py314h0eb9b55_0         4.5 MB
    pyqt6-sip-13.11.1          |  py314h47b2149_0          78 KB
    sip-6.15.1                 |  py314he6c97cb_0         712 KB
    ------------------------------------------------------------
                                           Total:       108.1 MB

The following NEW packages will be INSTALLED:

  aom                pkgs/main/linux-64::aom-3.13.2-h664349e_0 
  cairo              pkgs/main/linux-64::cairo-1.18.4-h44eff21_0 
  contourpy          pkgs/main/linux-64::contourpy-1.3.3-py314hdb19cb5_0 
  cycler             pkgs/main/linux-64::cycler-0.12.1-py314h06a4308_0 
  cyrus-sasl         pkgs/main/linux-64::cyrus-sasl-2.1.28-h83b0a09_4 
  dav1d              pkgs/main/linux-64::dav1d-1.5.3-h3e43c27_0 
  expat              pkgs/main/linux-64::expat-2.8.0-h7354ed3_0 
  fontconfig         pkgs/main/linux-64::fontconfig-2.17.1-h062c814_0 
  fonttools          pkgs/main/linux-64::fonttools-4.62.1-py314h47b2149_0 
  freetype           pkgs/main/linux-64::freetype-2.14.1-hf5b9546_0 
  fribidi            pkgs/main/linux-64::fribidi-1.0.16-h9fb5f84_0 
  graphite2          pkgs/main/linux-64::graphite2-1.3.14-h295c915_1 
  harfbuzz           pkgs/main/linux-64::harfbuzz-12.3.0-h79d275a_1 
  jpeg               pkgs/main/linux-64::jpeg-9f-h5ce9db8_0 
  kiwisolver         pkgs/main/linux-64::kiwisolver-1.4.9-py314h24d9097_0 
  lcms2              pkgs/main/linux-64::lcms2-2.19-he283960_0 
  lerc               pkgs/main/linux-64::lerc-4.1.0-h7354ed3_2 
  libavif            pkgs/main/linux-64::libavif-1.3.0-h2b90b00_1 
  libcups            pkgs/main/linux-64::libcups-2.4.15-hbe4054b_0 
  libdeflate         pkgs/main/linux-64::libdeflate-1.22-h5eee18b_0 
  libdrm             pkgs/main/linux-64::libdrm-2.4.124-h5eee18b_0 
  libegl             pkgs/main/linux-64::libegl-1.7.0-h5eee18b_2 
  libgl              pkgs/main/linux-64::libgl-1.7.0-h5eee18b_2 
  libglib            pkgs/main/linux-64::libglib-2.86.3-h8b17d9a_0 
  libglvnd           pkgs/main/linux-64::libglvnd-1.7.0-h5eee18b_2 
  libglx             pkgs/main/linux-64::libglx-1.7.0-h5eee18b_2 
  libllvm21          pkgs/main/linux-64::libllvm21-21.1.8-h3801bc2_1 
  libopengl          pkgs/main/linux-64::libopengl-1.7.0-h5eee18b_2 
  libopenjpeg        pkgs/main/linux-64::libopenjpeg-2.5.4-hee96239_1 
  libpciaccess       pkgs/main/linux-64::libpciaccess-0.18-h5eee18b_0 
  libpng             pkgs/main/linux-64::libpng-1.6.56-h22898a0_0 
  libpq              pkgs/main/linux-64::libpq-17.9-h0cb448f_1 
  libtiff            pkgs/main/linux-64::libtiff-4.7.1-h029b1ac_0 
  libwebp-base       pkgs/main/linux-64::libwebp-base-1.6.0-hb7bb969_0 
  libxkbcommon       pkgs/main/linux-64::libxkbcommon-1.13.1-h13fa2f1_0 
  matplotlib         pkgs/main/linux-64::matplotlib-3.10.9-py314h06a4308_0 
  matplotlib-base    pkgs/main/linux-64::matplotlib-base-3.10.9-py314h54cb298_0 
  mesalib            pkgs/main/linux-64::mesalib-25.1.5-h3583ad3_3 
  mysql-common       pkgs/main/linux-64::mysql-common-9.3.0-h9e076cb_6 
  mysql-libs         pkgs/main/linux-64::mysql-libs-9.3.0-he5ffe59_6 
  openldap           pkgs/main/linux-64::openldap-2.6.12-h007892f_1 
  pcre2              pkgs/main/linux-64::pcre2-10.46-hf426167_0 
  pillow             pkgs/main/linux-64::pillow-12.2.0-py314haa37d31_0 
  pixman             pkgs/main/linux-64::pixman-0.46.4-h7934f7d_0 
  pyparsing          pkgs/main/linux-64::pyparsing-3.2.5-py314h06a4308_0 
  pyqt               pkgs/main/linux-64::pyqt-6.11.0-py314h0eb9b55_0 
  pyqt6-sip          pkgs/main/linux-64::pyqt6-sip-13.11.1-py314h47b2149_0 
  qtbase             pkgs/main/linux-64::qtbase-6.11.0-h9201cad_0 
  qtdeclarative      pkgs/main/linux-64::qtdeclarative-6.11.0-h69798bf_0 
  qtsvg              pkgs/main/linux-64::qtsvg-6.11.0-h6af1df9_0 
  qttools            pkgs/main/linux-64::qttools-6.11.0-h50cdde4_0 
  qtwayland          pkgs/main/linux-64::qtwayland-6.11.0-h9a62c7d_0 
  qtwebchannel       pkgs/main/linux-64::qtwebchannel-6.11.0-h27b496b_0 
  qtwebsockets       pkgs/main/linux-64::qtwebsockets-6.11.0-h8bda742_0 
  sip                pkgs/main/linux-64::sip-6.15.1-py314he6c97cb_0 
  spirv-tools        pkgs/main/linux-64::spirv-tools-2026.1-h24d9097_0 
  wayland            pkgs/main/linux-64::wayland-1.24.0-hdac8c69_0 
  xcb-util           pkgs/main/linux-64::xcb-util-0.4.1-h5eee18b_2 
  xcb-util-cursor    pkgs/main/linux-64::xcb-util-cursor-0.1.5-h5eee18b_0 
  xcb-util-image     pkgs/main/linux-64::xcb-util-image-0.4.0-h5eee18b_2 
  xcb-util-keysyms   pkgs/main/linux-64::xcb-util-keysyms-0.4.1-h5eee18b_0 
  xcb-util-renderut~ pkgs/main/linux-64::xcb-util-renderutil-0.3.10-h5eee18b_0 
  xcb-util-wm        pkgs/main/linux-64::xcb-util-wm-0.4.2-h5eee18b_0 
  xkeyboard-config   pkgs/main/linux-64::xkeyboard-config-2.44-h382ed1a_1 
  xorg-libice        pkgs/main/linux-64::xorg-libice-1.1.2-h9b100fa_0 
  xorg-libsm         pkgs/main/linux-64::xorg-libsm-1.2.6-h9b100fa_0 
  xorg-libxext       pkgs/main/linux-64::xorg-libxext-1.3.6-h9b100fa_0 
  xorg-libxfixes     pkgs/main/linux-64::xorg-libxfixes-6.0.1-h9b100fa_0 
  xorg-libxrandr     pkgs/main/linux-64::xorg-libxrandr-1.5.4-h9b100fa_0 
  xorg-libxrender    pkgs/main/linux-64::xorg-libxrender-0.9.12-h9b100fa_0 
  xorg-libxshmfence  pkgs/main/linux-64::xorg-libxshmfence-1.3.3-h9b100fa_0 
  xorg-libxxf86vm    pkgs/main/linux-64::xorg-libxxf86vm-1.1.6-h9b100fa_0 

The following packages will be DOWNGRADED:

  icu                                       78.3-h84d19a5_0 --> 73.1-h6a678d5_0 

The following packages will be REVISED:

  libxml2                                 2.14.4-h4481af1_1 --> 2.14.4-h3457413_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done                                                                                                                                      
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314                                                                 
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 wget
Channels:             
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - wget


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    wget-1.25.0                |       he4200e1_2         755 KB
    ------------------------------------------------------------
                                           Total:         755 KB

The following NEW packages will be INSTALLED:

  wget               pkgs/main/linux-64::wget-1.25.0-he4200e1_2 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 yfinance
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundInChannelsError: The following packages are not available from current channels:

  - yfinance

Current channels:

  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 -c conda-forge yfinance
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - yfinance


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    appdirs-1.4.4              |     pyhd8ed1ab_1          14 KB  conda-forge
    ca-certificates-2026.4.22  |       hbd8a1cb_0         128 KB  conda-forge
    curl-cffi-0.15.0           |  py314ha768014_1         9.4 MB  conda-forge
    frozendict-2.4.7           |  py314h5bd0f2a_0          31 KB  conda-forge
    gettext-0.21.1             |       h27087fc_0         4.1 MB  conda-forge
    gettext-tools-0.25.1       |       h3f43e3d_1         3.5 MB  conda-forge
    libnghttp2-1.67.1          |       had1ee68_0         651 KB  conda-forge
    libsqlite-3.52.0           |       h0c1763c_0         928 KB  conda-forge
    libxkbcommon-1.11.0        |       he8b52b9_0         773 KB  conda-forge
    libxslt-1.1.43             |       h7a3aeb2_0         239 KB  conda-forge
    lxml-6.0.2                 |  py314hd59e8af_0         1.5 MB  conda-forge
    markdown-it-py-4.2.0       |     pyhd8ed1ab_0          67 KB  conda-forge
    mdurl-0.1.2                |     pyhd8ed1ab_1          14 KB  conda-forge
    multitasking-0.0.13        |     pyhd8ed1ab_0          21 KB  conda-forge
    openssl-3.6.2              |       h35e630c_0         3.0 MB  conda-forge
    peewee-4.0.4               |  py314h0fc9818_0         417 KB  conda-forge
    protobuf-6.33.5            |  py314h61e7c5f_0         478 KB  conda-forge
    rich-15.0.0                |     pyhcf101f3_0         204 KB  conda-forge
    websockets-16.0            |  py314h0f05182_1         374 KB  conda-forge
    yfinance-1.3.0             |     pyhd8ed1ab_0         109 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        25.9 MB

The following NEW packages will be INSTALLED:

  appdirs            conda-forge/noarch::appdirs-1.4.4-pyhd8ed1ab_1 
  curl-cffi          conda-forge/linux-64::curl-cffi-0.15.0-py314ha768014_1 
  frozendict         conda-forge/linux-64::frozendict-2.4.7-py314h5bd0f2a_0 
  libsqlite          conda-forge/linux-64::libsqlite-3.52.0-h0c1763c_0 
  libxslt            conda-forge/linux-64::libxslt-1.1.43-h7a3aeb2_0 
  lxml               conda-forge/linux-64::lxml-6.0.2-py314hd59e8af_0 
  markdown-it-py     conda-forge/noarch::markdown-it-py-4.2.0-pyhd8ed1ab_0 
  mdurl              conda-forge/noarch::mdurl-0.1.2-pyhd8ed1ab_1 
  multitasking       conda-forge/noarch::multitasking-0.0.13-pyhd8ed1ab_0 
  peewee             conda-forge/linux-64::peewee-4.0.4-py314h0fc9818_0 
  protobuf           conda-forge/linux-64::protobuf-6.33.5-py314h61e7c5f_0 
  rich               conda-forge/noarch::rich-15.0.0-pyhcf101f3_0 
  websockets         conda-forge/linux-64::websockets-16.0-py314h0f05182_1 
  yfinance           conda-forge/noarch::yfinance-1.3.0-pyhd8ed1ab_0 

The following packages will be UPDATED:

  ca-certificates    pkgs/main/linux-64::ca-certificates-2~ --> conda-forge/noarch::ca-certificates-2026.4.22-hbd8a1cb_0 
  openssl               pkgs/main::openssl-3.5.6-h1b28b03_0 --> conda-forge::openssl-3.6.2-h35e630c_0 

The following packages will be SUPERSEDED by a higher-priority channel:

  gettext              pkgs/main::gettext-0.25.1-hd8bbc44_1 --> conda-forge::gettext-0.21.1-h27087fc_0 
  gettext-tools      pkgs/main::gettext-tools-0.25.1-hecf7~ --> conda-forge::gettext-tools-0.25.1-h3f43e3d_1 
  libnghttp2         pkgs/main::libnghttp2-1.69.0-hc59f8b6~ --> conda-forge::libnghttp2-1.67.1-had1ee68_0 
  libxkbcommon       pkgs/main::libxkbcommon-1.13.1-h13fa2~ --> conda-forge::libxkbcommon-1.11.0-he8b52b9_0 

The following packages will be DOWNGRADED:

  fontconfig                              2.17.1-h062c814_0 --> 2.15.0-h2c49b7f_0 
  libcurl                                 8.20.0-hd8fa685_1 --> 8.19.0-ha05a353_0 
  libxml2                                 2.14.4-h3457413_0 --> 2.13.9-h2c43086_0 

The following packages will be REVISED:

  libllvm21                               21.1.8-h3801bc2_1 --> 21.1.8-h5ad376a_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done                                                                                                                                      
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314                                                    
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 sympy                                                                      
Channels:             
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - sympy


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    gmpy2-2.2.2                |  py314ha78e65c_0         265 KB
    mpmath-1.3.0               |  py314h06a4308_0        1008 KB
    sympy-1.14.0               |  py314h06a4308_1        14.6 MB
    ------------------------------------------------------------
                                           Total:        15.8 MB

The following NEW packages will be INSTALLED:

  gmp                pkgs/main/linux-64::gmp-6.3.0-h6a678d5_0 
  gmpy2              pkgs/main/linux-64::gmpy2-2.2.2-py314ha78e65c_0 
  mpc                pkgs/main/linux-64::mpc-1.3.1-h5eee18b_0 
  mpfr               pkgs/main/linux-64::mpfr-4.2.1-h5eee18b_0 
  mpmath             pkgs/main/linux-64::mpmath-1.3.0-py314h06a4308_0 
  sympy              pkgs/main/linux-64::sympy-1.14.0-py314h06a4308_1 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install conda-forge::scipy-typed
Channels:
 - defaults
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - conda-forge::scipy-typed


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    scipy-1.17.1               |  py314h3d0cd3c_1        23.6 MB
    scipy-stubs-1.17.1.4       |     pyhc364b38_0         362 KB  conda-forge
    scipy-typed-1.17.1.4       |     pyh4d59ecc_0          11 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        23.9 MB

The following NEW packages will be INSTALLED:

  libgfortran        pkgs/main/linux-64::libgfortran-15.2.0-h166f726_7 
  libgfortran5       pkgs/main/linux-64::libgfortran5-15.2.0-hc633d37_7 
  numpy-typing-comp~ conda-forge/noarch::numpy-typing-compat-20251206.2.4-pyhd6139ff_0 
  optype             conda-forge/noarch::optype-0.17.0-pyhc364b38_0 
  optype-numpy       conda-forge/noarch::optype-numpy-0.17.0-pyhada4073_0 
  scipy              pkgs/main/linux-64::scipy-1.17.1-py314h3d0cd3c_1 
  scipy-stubs        conda-forge/noarch::scipy-stubs-1.17.1.4-pyhc364b38_0 
  scipy-typed        conda-forge/noarch::scipy-typed-1.17.1.4-pyh4d59ecc_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done                                                                                                                                      
Verifying transaction: done                                                                                                                                      
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -n ds314 seaborn
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - seaborn


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    seaborn-0.13.2             |  py314h06a4308_3         690 KB
    ------------------------------------------------------------
                                           Total:         690 KB

The following NEW packages will be INSTALLED:

  seaborn            pkgs/main/linux-64::seaborn-0.13.2-py314h06a4308_3 


Proceed ([y]/n)? 


Downloading and Extracting Packages:
                                                                                                                                                                 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda update -n ds314 --all --no-pin
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314


The following NEW packages will be INSTALLED:

  libhwloc           pkgs/main/linux-64::libhwloc-2.12.1-default_hf1bbc79_1000 

The following packages will be UPDATED:

  tbb                                   2022.0.0-hdb19cb5_0 --> 2022.3.0-h698db13_0 
  tbb-devel                             2022.0.0-hdb19cb5_0 --> 2022.3.0-h698db13_0 


Proceed ([y]/n)? 


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda env export --no-builds > ds314_env_--no-builds_20260510.yml
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ 
```