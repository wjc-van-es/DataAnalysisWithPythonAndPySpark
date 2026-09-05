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

# Conda `ds312` environment update @mint-22 on 20260905

## Context
Direct reason was that we would like to install The **Manim** Community Edition on the environment. We tried that on our
latest greatest ds314 environment, but we couldn't get it to work.

See [ds314-conda-env-update@mint-22.md](ds314-conda-env-update@mint-22.md)

## Steps for general updates of the `base` and the `ds314` environments
1. `(ds314) $ conda activate ds312`
2. `(ds312) $ python --version` (reveals `Python 3.12.11`)
3. `(ds312) $ conda update -n ds312 --all --no-pin`
4. `(ds312) $ python --version` (reveals `Python 3.12.11`)

## Adding `Manim CE`
- [https://docs.manim.community/en/stable/installation/conda.html](https://docs.manim.community/en/stable/installation/conda.html)
- `(ds312) $ conda install -c conda-forge manim`
- `(ds312) $ conda activate ds312`


<details>

```bash
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ python --version
Python 3.12.11
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -n ds312 --all --no-pin
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    arrow-cpp-23.0.1           |   cpu_h1194d3f_5        12.3 MB
    aws-c-auth-0.10.3          |       h47b2149_0         117 KB
    aws-c-cal-0.9.14           |       h1b28b03_0          53 KB
    aws-c-common-0.14.0        |       h47b2149_0         235 KB
    aws-c-compression-0.3.2    |       h47b2149_1          18 KB
    aws-c-event-stream-0.7.1   |       h1a3b0be_0          54 KB
    aws-c-http-0.11.0          |       h47b2149_1         203 KB
    aws-c-io-0.26.3            |       h1b29dbc_1         161 KB
    aws-c-mqtt-0.15.2          |       h47b2149_1         197 KB
    aws-c-s3-0.12.5            |       h1b28b03_0         134 KB
    aws-c-sdkutils-0.2.4       |       h47b2149_3          54 KB
    aws-checksums-0.2.10       |       h47b2149_1          96 KB
    aws-crt-cpp-0.40.1         |       hcff5ade_0         369 KB
    aws-sdk-cpp-1.11.826       |       h8c0960e_0         2.9 MB
    blas-1.0                   |         openblas          46 KB
    cairo-1.18.4               |       ha82d1dd_1         660 KB
    cuda-cudart-13.3.29        |       h7354ed3_0          22 KB
    cuda-cudart_linux-64-13.3.29|       hfb20e49_0         199 KB
    cuda-version-13.3          |       h0dc9999_3          20 KB
    fontconfig-2.17.1          |       h062c814_0         269 KB
    gst-plugins-base-1.28.4    |       h446d7a6_1         2.8 MB
    gstreamer-1.28.4           |       hbd6b80e_1         2.0 MB
    harfbuzz-12.3.0            |       h572a7f1_2         2.3 MB
    icu-78.3                   |       h53478e7_1        23.0 MB
    ipykernel-7.3.0            |  py312h7040dfc_0         256 KB
    jedi-0.20.0                |  py312h06a4308_0         3.0 MB
    lcms2-2.19.1               |       h425df66_1         245 KB
    libboost-1.88.0            |       h5c7ffa9_2         2.9 MB
    libclang-22.1.2            |default_h0b3d5db_2         133 KB
    libcurl-8.21.0             |       hd8fa685_0         501 KB
    libhwloc-2.13.0            |default_hcb8a28c_1002         2.3 MB
    libjpeg-turbo-3.1.3        |       h47b2149_0         607 KB
    libllvm22-22.1.2           |       h7fb75ab_2        43.4 MB
    libnghttp2-1.69.0          |       hc59f8b6_0         647 KB
    libogg-1.3.5               |       h5a08620_2         201 KB
    libopenblas-0.3.31         |       hf7dbefb_3         5.7 MB
    libtiff-4.7.2              |       h2b43d3b_0         449 KB
    libutf8proc-2.11.3         |       hadbecdc_1          83 KB
    libxkbcommon-1.13.1        |       h13fa2f1_0         822 KB
    libxml2-2.14.6             |       hf2a51f9_1         645 KB
    libxslt-1.1.43             |       hf1eb641_1         238 KB
    lxml-6.1.0                 |  py312h20df5e8_0         1.5 MB
    mysql-libs-9.3.0           |       he5ffe59_6         1.3 MB
    nest-asyncio2-1.7.2        |  py312h06a4308_0          25 KB
    numpy-2.4.6                |  py312h35deafb_0          19 KB
    numpy-base-2.4.6           |  py312h4bc27c9_0         8.0 MB
    pillow-12.3.0              |  py312h652d24c_0         1.0 MB
    python_abi-3.12            |          4_cp312           5 KB
    qt-main-6.11.0             |       hd81f5f1_0          11 KB
    qt5compat-6.11.0           |       hed7d4da_2         673 KB
    qtbase-6.11.0              |       ha82b782_2        12.3 MB
    qtbase-devel-6.11.0        |       h598a104_2         4.9 MB
    qtimageformats-6.11.0      |       h00148ef_1          71 KB
    qttranslations-6.11.0      |       h490eead_1         2.0 MB
    qtwayland-6.11.0           |       h84ca50f_1         968 KB
    scipy-1.17.1               |  py312h35deafb_1        23.4 MB
    tbb-2023.0.0               |       h78989d2_0         181 KB
    tbb-devel-2023.0.0         |       h78989d2_0         1.1 MB
    ------------------------------------------------------------
                                           Total:       167.6 MB

The following NEW packages will be INSTALLED:

  libboost           pkgs/main/linux-64::libboost-1.88.0-h5c7ffa9_2 
  libjpeg-turbo      pkgs/main/linux-64::libjpeg-turbo-3.1.3-h47b2149_0 
  libllvm22          pkgs/main/linux-64::libllvm22-22.1.2-h7fb75ab_2 
  libopenblas        pkgs/main/linux-64::libopenblas-0.3.31-hf7dbefb_3 
  libutf8proc        pkgs/main/linux-64::libutf8proc-2.11.3-hadbecdc_1 
  nest-asyncio2      pkgs/main/linux-64::nest-asyncio2-1.7.2-py312h06a4308_0 

The following packages will be REMOVED:

  fribidi-1.0.16-h9fb5f84_0
  intel-openmp-2025.0.0-h06a4308_1171
  jpeg-9f-h5ce9db8_0
  libgomp-15.2.0-h4751f2c_7
  libllvm15-15.0.7-he89c38a_4
  libllvm21-21.1.8-h5ad376a_0
  mkl-2025.0.0-hacee8c2_941
  mkl-service-2.5.2-py312hacdc0fc_0
  mkl_fft-2.1.1-py312h8fe796d_0
  mkl_random-1.3.0-py312h505adc9_0
  nest-asyncio-1.6.0-py312h06a4308_0
  utf8proc-2.6.1-h5eee18b_1

The following packages will be UPDATED:

  _openmp_mutex                                   5.1-1_gnu --> 5.1-52_gnu 
  aom                                     3.12.1-h7934f7d_0 --> 3.13.2-h664349e_0 
  async-lru                           2.0.5-py312h06a4308_0 --> 2.3.0-py312h06a4308_0 
  attrs                              25.4.0-py312h06a4308_2 --> 26.1.0-py312h0c820a0_0 
  aws-c-auth                               0.9.4-h47b2149_0 --> 0.10.3-h47b2149_0 
  aws-c-cal                               0.9.13-h1b28b03_0 --> 0.9.14-h1b28b03_0 
  aws-c-common                            0.12.6-h47b2149_0 --> 0.14.0-h47b2149_0 
  aws-c-compression                        0.3.1-h47b2149_3 --> 0.3.2-h47b2149_1 
  aws-c-event-stream                       0.5.9-h47b2149_0 --> 0.7.1-h1a3b0be_0 
  aws-c-http                              0.10.7-h47b2149_0 --> 0.11.0-h47b2149_1 
  aws-c-io                                0.23.3-h47b2149_0 --> 0.26.3-h1b29dbc_1 
  aws-c-mqtt                              0.13.3-h47b2149_1 --> 0.15.2-h47b2149_1 
  aws-c-s3                                0.11.3-h1b28b03_0 --> 0.12.5-h1b28b03_0 
  aws-c-sdkutils                           0.2.4-h47b2149_2 --> 0.2.4-h47b2149_3 
  aws-checksums                            0.2.8-h47b2149_0 --> 0.2.10-h47b2149_1 
  aws-crt-cpp                             0.35.4-h7354ed3_0 --> 0.40.1-hcff5ade_0 
  aws-sdk-cpp                           1.11.720-h47cf5e4_0 --> 1.11.826-h8c0960e_0 
  babel                              2.17.0-py312h06a4308_0 --> 2.18.0-py312h06a4308_0 
  beautifulsoup4                     4.14.3-py312h06a4308_0 --> 4.15.0-py312h06a4308_0 
  blas                                              1.0-mkl --> 1.0-openblas 
  bleach                              6.3.0-py312h06a4308_0 --> 6.4.0-py312h06a4308_0 
  brotlicffi                        1.2.0.0-py312h7354ed3_0 --> 1.2.0.1-py312h7354ed3_0 
  c-ares                                  1.34.6-hd44998d_0 --> 1.34.7-hd44998d_0 
  ca-certificates                      2025.12.2-h06a4308_0 --> 2026.8.13-h06a4308_0 
  cairo                                   1.18.4-h44eff21_0 --> 1.18.4-ha82d1dd_1 
  certifi                        2026.01.04-py312h06a4308_0 --> 2026.7.22-py312h06a4308_0 
  cffi                                2.0.0-py312h4eded50_1 --> 2.1.1-py312h3b52fac_0 
  charset-normalizer                  3.4.4-py312h06a4308_0 --> 3.4.7-py312h06a4308_0 
  cuda-cudart                            13.1.80-h7354ed3_0 --> 13.3.29-h7354ed3_0 
  cuda-cudart_linux~                     13.1.80-hfb20e49_0 --> 13.3.29-hfb20e49_0 
  cuda-version                              13.1-he7c9b7b_3 --> 13.3-h0dc9999_3 
  cyrus-sasl                              2.1.28-h83b0a09_4 --> 2.1.28-h2f687bf_5 
  dav1d                                    1.2.1-h5eee18b_0 --> 1.5.3-h12c9f22_1 
  debugpy                            1.8.16-py312hbdd6827_1 --> 1.8.21-py312h7354ed3_0 
  decorator                           5.2.1-py312h06a4308_0 --> 5.3.1-py312h06a4308_0 
  executing                           2.2.1-py312h06a4308_0 --> 2.2.1-py312h06a4308_1 
  expat                                    2.7.5-h7354ed3_0 --> 2.8.4-h7354ed3_0 
  fontconfig                              2.15.0-h2c49b7f_0 --> 2.17.1-h062c814_0 
  fonttools                          4.62.1-py312h47b2149_0 --> 4.63.0-py312h47b2149_0 
  frozendict                          2.4.6-py312hee96239_0 --> 2.4.7-py312h47b2149_0 
  gflags                                   2.2.2-h6a678d5_1 --> 2.3.1-h86178c3_1 
  glog                                     0.5.0-h6a678d5_1 --> 0.7.1-h485759d_0 
  gmp                                      6.3.0-h6a678d5_0 --> 6.3.0-haace2f4_1 
  gmpy2                               2.2.2-py312ha78e65c_0 --> 2.3.1-py312h1cd8627_0 
  graphite2                               1.3.14-h295c915_1 --> 1.3.15-h9ba177b_0 
  gst-plugins-base                       1.26.10-hf0a17ef_0 --> 1.28.4-h446d7a6_1 
  gstreamer                              1.26.10-hd23371b_0 --> 1.28.4-hbd6b80e_1 
  harfbuzz                                12.3.0-h79d275a_1 --> 12.3.0-h572a7f1_2 
  icu                                       73.1-h6a678d5_0 --> 78.3-h53478e7_1 
  idna                                 3.11-py312h06a4308_0 --> 3.18-py312h06a4308_0 
  ipykernel                           7.2.0-py312h7040dfc_0 --> 7.3.0-py312h7040dfc_0 
  ipython                            9.11.0-py312h06a4308_0 --> 9.15.0-py312h06a4308_0 
  jansson                                   2.14-h5eee18b_1 --> 2.15.0-hbcba0ee_0 
  jedi                               0.19.2-py312h06a4308_0 --> 0.20.0-py312h06a4308_0 
  jinja2                              3.1.6-py312h06a4308_0 --> 3.1.6-py312h06a4308_1 
  json5                              0.12.1-py312h06a4308_0 --> 0.15.0-py312h06a4308_0 
  jsonschema                         4.25.1-py312h06a4308_0 --> 4.26.0-py312h06a4308_0 
  jupyter_client                      8.8.0-py312h06a4308_0 --> 8.9.1-py312h06a4308_0 
  jupyter_events                     0.12.0-py312h06a4308_1 --> 0.12.1-py312h06a4308_0 
  jupyter_server                     2.17.0-py312h06a4308_1 --> 2.20.0-py312h06a4308_0 
  jupyterlab                          4.5.3-py312h06a4308_1 --> 4.5.9-py312h06a4308_1 
  kiwisolver                          1.4.9-py312h24d9097_0 --> 1.5.0-py312h7354ed3_0 
  lcms2                                     2.17-heab6991_0 --> 2.19.1-h425df66_1 
  lerc                                     4.0.0-h6a678d5_0 --> 4.1.0-h7354ed3_2 
  libavif                                  1.3.0-h3539ee5_0 --> 1.3.0-h2b90b00_1 
  libclang                        21.1.8-default_h05d3d09_0 --> 22.1.2-default_h0b3d5db_2 
  libclang13                      21.1.8-default_hdcc6915_0 --> 22.1.2-default_hc2d2b39_2 
  libcups                                 2.4.15-hbe4054b_0 --> 2.4.19-h23114ae_0 
  libcurl                                 8.19.0-ha05a353_0 --> 8.21.0-hd8fa685_0 
  libdrm                                 2.4.124-h5eee18b_0 --> 2.4.134-h9c74679_0 
  libexpat                                 2.7.5-h7354ed3_0 --> 2.8.4-h7354ed3_0 
  libffi                                   3.4.4-h6a678d5_1 --> 3.4.8-h06d3fd0_3 
  libgcc                                  15.2.0-h69a1729_7 --> 15.2.0-h69a1729_8 
  libgcc-ng                               15.2.0-h166f726_7 --> 15.2.0-h166f726_8 
  libgfortran                             15.2.0-h166f726_7 --> 15.2.0-h166f726_8 
  libgfortran5                            15.2.0-hc633d37_7 --> 15.2.0-hc633d37_8 
  libglib                                 2.86.3-h8b17d9a_0 --> 2.88.3-ha16e27a_0 
  libgrpc                                 1.78.0-h79c45ec_0 --> 1.78.0-h01ccb81_1 
  libhwloc                     2.12.1-default_hf1bbc79_1000 --> 2.13.0-default_hcb8a28c_1002 
  libkrb5                                 1.22.1-h6d2bf13_0 --> 1.22.2-hbd13c29_0 
  libnghttp2                              1.67.1-h697f920_0 --> 1.69.0-hc59f8b6_0 
  libogg                                   1.3.5-h27cfd23_1 --> 1.3.5-h5a08620_2 
  libopenjpeg                              2.5.4-hee96239_1 --> 2.5.4-h47b2149_2 
  libpq                                     17.6-h5ca1609_1 --> 17.10-h0cb448f_2 
  libsodium                               1.0.20-heac8642_0 --> 1.0.21-h83fc4cd_1 
  libssh2                                 1.11.1-h251f7ec_0 --> 1.11.1-hfbabe93_1 
  libstdcxx                               15.2.0-h39759b7_7 --> 15.2.0-h39759b7_8 
  libstdcxx-ng                            15.2.0-hc03a8fd_7 --> 15.2.0-hc03a8fd_8 
  libtiff                                  4.7.1-h029b1ac_0 --> 4.7.2-h2b43d3b_0 
  libunistring                               1.3-hb25bd0a_0 --> 1.4.2-h34b0ebb_0 
  libxkbcommon                             1.9.1-h69220b7_0 --> 1.13.1-h13fa2f1_0 
  libxml2                                 2.13.9-h2c43086_0 --> 2.14.6-hf2a51f9_1 
  libxslt                                 1.1.43-h28b3bda_0 --> 1.1.43-hf1eb641_1 
  libzlib                                  1.3.1-hb25bd0a_0 --> 1.3.2-h47b2149_0 
  lmdb                                    0.9.31-hb25bd0a_0 --> 1.0.0-hfe55579_0 
  lxml                                5.3.0-py312hd70a998_2 --> 6.1.0-py312h20df5e8_0 
  lz4-c                                    1.9.4-h6a678d5_1 --> 1.9.4-h7354ed3_5 
  markupsafe                          3.0.2-py312h5eee18b_0 --> 3.0.3-py312h47b2149_0 
  matplotlib                         3.10.8-py312h06a4308_0 --> 3.11.0-py312h06a4308_0 
  matplotlib-base                    3.10.8-py312h8a257da_0 --> 3.11.0-py312h8a257da_0 
  matplotlib-inline                   0.2.1-py312h06a4308_0 --> 0.2.2-py312h06a4308_0 
  mesalib                                 25.1.5-hac3cb23_1 --> 25.1.5-h3583ad3_5 
  mistune                             3.1.2-py312h06a4308_0 --> 3.3.3-py312h06a4308_0 
  mysql-common                             9.3.0-h9e076cb_5 --> 9.3.0-h9e076cb_6 
  mysql-libs                               9.3.0-h6ecde68_5 --> 9.3.0-he5ffe59_6 
  nbclient                           0.10.4-py312h06a4308_0 --> 0.11.0-py312h06a4308_0 
  nbconvert                          7.17.0-py312h06a4308_0 --> 7.17.1-py312h06a4308_0 
  nbconvert-core                     7.17.0-py312h06a4308_0 --> 7.17.1-py312h06a4308_0 
  nbconvert-pandoc                   7.17.0-py312h06a4308_0 --> 7.17.1-py312h06a4308_0 
  nbformat                           5.10.4-py312h06a4308_0 --> 5.11.0-py312h06a4308_0 
  ncurses                                    6.5-h7934f7d_0 --> 6.6-hfaaeb4e_0 
  notebook                            7.5.3-py312h06a4308_0 --> 7.5.7-py312h06a4308_0 
  numpy                               2.4.3-py312h08c6c3d_0 --> 2.4.6-py312h35deafb_0 
  numpy-base                          2.4.3-py312h00548fb_0 --> 2.4.6-py312h4bc27c9_0 
  openldap                                2.6.12-hb446bd0_0 --> 2.6.12-h007892f_1 
  openssl                                  3.5.5-h1b28b03_0 --> 3.5.8-h1b28b03_0 
  packaging                            25.0-py312h06a4308_1 --> 26.3-py312h06a4308_0 
  pandas                              3.0.1-py312h86c3e14_0 --> 3.0.5-py312h86c3e14_0 
  parso                               0.8.5-py312h06a4308_0 --> 0.8.7-py312h06a4308_0 
  pillow                             12.1.1-py312h8263a33_0 --> 12.3.0-py312h652d24c_0 
  pip                                   26.0.1-pyhc872135_0 --> 26.2.1-pyhc872135_0 
  pixman                                  0.46.4-h7934f7d_0 --> 0.46.4-h86ba9f7_1 
  platformdirs                        4.9.4-py312h06a4308_0 --> 4.11.0-py312h06a4308_0 
  prompt-toolkit                     3.0.52-py312h06a4308_1 --> 3.0.53-py312h06a4308_0 
  prompt_toolkit                          3.0.52-hd3eb1b0_1 --> 3.0.53-hd3eb1b0_0 
  psutil                              7.0.0-py312hee96239_1 --> 7.2.2-py312h47b2149_0 
  pthread-stubs                              0.3-h0ce48e5_1 --> 0.3-h47b2149_2 
  pycparser                            2.23-py312h06a4308_0 --> 3.0-py312h06a4308_0 
  pygments                           2.19.2-py312h06a4308_0 --> 2.20.0-py312h06a4308_0 
  pyparsing                           3.2.5-py312h06a4308_0 --> 3.3.2-py312h06a4308_0 
  pyqt                               6.10.2-py312h559a8f0_1 --> 6.11.0-py312h0eb9b55_0 
  pyqt6-sip                         13.11.0-py312h47b2149_1 --> 13.11.1-py312h47b2149_0 
  python-dotenv                       1.2.1-py312h06a4308_0 --> 1.2.2-py312h06a4308_0 
  python-fastjsonsc~                 2.21.2-py312h06a4308_0 --> 2.22.1-py312h06a4308_0 
  python-json-logger                  4.0.0-py312h06a4308_0 --> 4.1.0-py312h06a4308_0 
  python_abi                                   3.12-3_cp312 --> 3.12-4_cp312 
  pytz                         2026.1.post1-py312h06a4308_0 --> 2026.3.post1-py312h06a4308_0 
  qt-main                                 6.10.2-ha538ae8_1 --> 6.11.0-hd81f5f1_0 
  qt5compat                               6.10.2-h9c40958_0 --> 6.11.0-hed7d4da_2 
  qtbase                                  6.10.2-h4a60b0a_0 --> 6.11.0-ha82b782_2 
  qtbase-devel                            6.10.2-h4f52c18_0 --> 6.11.0-h598a104_2 
  qtdeclarative                           6.10.2-hc22446d_0 --> 6.11.0-h89ee561_1 
  qtimageformats                          6.10.2-h074ac99_0 --> 6.11.0-h00148ef_1 
  qtshadertools                           6.10.2-h3453093_0 --> 6.11.0-h5973cd6_1 
  qtsvg                                   6.10.2-hb876869_0 --> 6.11.0-hbecefc2_1 
  qttools                                 6.10.2-h96d7b9c_0 --> 6.11.0-h0af0a4d_1 
  qttranslations                          6.10.2-h9595907_0 --> 6.11.0-h490eead_1 
  qtwayland                               6.10.2-h796633b_0 --> 6.11.0-h84ca50f_1 
  qtwebchannel                            6.10.2-hf28f473_0 --> 6.11.0-h7ebffc9_1 
  qtwebsockets                            6.10.2-h58c21ad_0 --> 6.11.0-h03d4248_1 
  requests                           2.32.5-py312h06a4308_1 --> 2.34.2-py312h06a4308_0 
  scipy                              1.17.1-py312h804029f_0 --> 1.17.1-py312h35deafb_1 
  setuptools                        80.10.2-py312h06a4308_0 --> 83.0.0-py312h06a4308_0 
  soupsieve                             2.5-py312h06a4308_0 --> 2.8.4-py312h06a4308_0 
  sqlite                                  3.51.2-h3e8d24a_0 --> 3.53.2-h795bf6d_0 
  tbb                                   2022.3.0-h698db13_0 --> 2023.0.0-h78989d2_0 
  tbb-devel                             2022.3.0-h698db13_0 --> 2023.0.0-h78989d2_0 
  tinycss2                            1.4.0-py312h06a4308_0 --> 1.5.1-py312h06a4308_0 
  tornado                             6.5.5-py312h47b2149_0 --> 6.5.7-py312h47b2149_0 
  traitlets                          5.14.3-py312h06a4308_0 --> 5.15.0-py312h06a4308_0 
  typing-extensions                  4.15.0-py312h06a4308_0 --> 4.16.0-py312h06a4308_0 
  typing_extensions                  4.15.0-py312h06a4308_0 --> 4.16.0-py312h06a4308_0 
  tzdata                                   2026a-he532380_0 --> 2026c-he532380_0 
  urllib3                             2.6.3-py312h06a4308_0 --> 2.7.0-py312h06a4308_0 
  wcwidth                            0.2.14-py312h06a4308_0 --> 0.8.2-py312h06a4308_0 
  webencodings                        0.5.1-py312h06a4308_2 --> 0.6.1-py312h06a4308_0 
  websockets                         15.0.1-py312h5eee18b_0 --> 16.0-py312h47b2149_0 
  wheel                              0.46.3-py312h06a4308_0 --> 0.47.0-py312h06a4308_0 
  xkeyboard-config                          2.44-h382ed1a_1 --> 2.48-h382ed1a_0 
  xorg-libxext                             1.3.6-h9b100fa_0 --> 1.3.7-h1ce37a7_0 
  xorg-xorgproto                          2024.1-h5eee18b_1 --> 2024.1-h47b2149_2 
  yaml                                     0.2.5-h7b6447c_0 --> 0.2.5-h591646f_1 
  zeromq                                   4.3.5-hb0a5e54_1 --> 4.3.5-hf801bfb_2 
  zlib                                     1.3.1-hb25bd0a_0 --> 1.3.2-h47b2149_0 

The following packages will be REVISED:

  arrow-cpp                     23.0.1-cuda131_hb40dd18_101 --> 23.0.1-cpu_h1194d3f_5 
  pyarrow                  23.0.1-cuda131_py312hdf5fc99_101 --> 23.0.1-cpu_py312h9a353a3_3 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: done                                                                                                                                     
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ python --version                                              
Python 3.12.11                                                                                                                                                  
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -n ds312 -c conda-forge x264
Channels:                                                                                                                                                       
 - conda-forge                                                                                                                                                  
 - defaults           
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312

  added / updated specs:
    - x264


The following NEW packages will be INSTALLED:

  x264               conda-forge/linux-64::x264-1!164.3095-h166bdaf_2 

The following packages will be UPDATED:

  openssl               pkgs/main::openssl-3.5.8-h1b28b03_0 --> conda-forge::openssl-3.6.4-h781a0a9_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -n ds312 -c conda-forge manim
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312

  added / updated specs:
    - manim


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    click-default-group-1.2.4  |     pyhd8ed1ab_1          10 KB  conda-forge
    cryptography-50.0.1        |  py312h89f293a_0         1.8 MB  conda-forge
    dulwich-1.2.10             |  py312hc767a74_3         2.8 MB  conda-forge
    fribidi-1.0.16             |       h7cc23a3_2          61 KB  conda-forge
    gdk-pixbuf-2.44.6          |       h2b0a6b4_0         564 KB  conda-forge
    glcontext-3.0.0            |  py312h835c14e_2          23 KB  conda-forge
    glib-2.48.0                |                3         4.4 MB  conda-forge
    leptonica-1.87.0           |       h12c84f9_1         2.5 MB  conda-forge
    libfreetype-2.14.1         |       ha770c72_0           7 KB  conda-forge
    libfreetype6-2.14.1        |       h73754d4_0         378 KB  conda-forge
    libgd-2.3.3                |      h5fbf134_12         173 KB  conda-forge
    libva-2.22.0               |       h4f16b4b_2         212 KB  conda-forge
    manim-0.18.1               |     pyhd8ed1ab_1         401 KB  conda-forge
    manimpango-0.6.0           |  py312h6802ac9_0          98 KB  conda-forge
    mapbox_earcut-1.0.3        |  py312hf890105_2          90 KB  conda-forge
    moderngl-5.11.1            |  py312h4f16dfd_1         129 KB  conda-forge
    msgpack-python-1.2.2       |  py312h9be0db6_2         112 KB  conda-forge
    pango-1.56.4               |       hadf4263_0         445 KB  conda-forge
    pcre-8.45                  |       h9c3ff4c_0         253 KB  conda-forge
    pycairo-1.29.0             |  py312h2596900_1         117 KB  conda-forge
    pyglm-2.8.3                |  py312h9be0db6_3         1.6 MB  conda-forge
    rapidfuzz-3.14.6           |  py312ha6a3dbb_0         2.1 MB  conda-forge
    screeninfo-0.8.1           |  py312h7900ff3_3          32 KB  conda-forge
    secretstorage-3.5.0        |  py312h7900ff3_1          32 KB  conda-forge
    skia-pathops-0.9.2         |  py312h9be0db6_2         408 KB  conda-forge
    watchdog-6.0.0             |  py312h20c3967_4         148 KB  conda-forge
    xorg-libxi-1.8.2           |       hb9d3cd8_0          46 KB  conda-forge
    xorg-libxtst-1.2.5         |       hb9d3cd8_3          32 KB  conda-forge
    zstandard-0.25.0           |  py312h1b36aeb_4         456 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        19.3 MB

The following NEW packages will be INSTALLED:

  alsa-lib           conda-forge/linux-64::alsa-lib-1.2.16.1-h7cc23a3_1 
  backports          conda-forge/noarch::backports-1.0-pyhd8ed1ab_5 
  backports.tarfile  conda-forge/noarch::backports.tarfile-1.2.0-pyhcf101f3_2 
  cachecontrol       conda-forge/noarch::cachecontrol-0.14.4-pyha770c72_0 
  cachecontrol-with~ conda-forge/noarch::cachecontrol-with-filecache-0.14.4-pyhd8ed1ab_0 
  cleo               conda-forge/noarch::cleo-2.1.0-pyhd8ed1ab_1 
  click              conda-forge/noarch::click-8.4.2-pyhc90fa1f_0 
  click-default-gro~ conda-forge/noarch::click-default-group-1.2.4-pyhd8ed1ab_1 
  cloup              conda-forge/noarch::cloup-3.0.9-pyhd8ed1ab_0 
  colorama           conda-forge/noarch::colorama-0.4.6-pyhd8ed1ab_1 
  crashtest          conda-forge/noarch::crashtest-0.4.1-pyhd8ed1ab_1 
  cryptography       conda-forge/linux-64::cryptography-50.0.1-py312h89f293a_0 
  distlib            conda-forge/noarch::distlib-0.4.3-pyhcf101f3_0 
  dulwich            conda-forge/linux-64::dulwich-1.2.10-py312hc767a74_3 
  ffmpeg             pkgs/main/linux-64::ffmpeg-8.1.2-h5758e9d_0 
  fftw               conda-forge/linux-64::fftw-3.3.11-nompi_h3b011a4_100 
  filelock           conda-forge/noarch::filelock-3.32.5-pyhd8ed1ab_0 
  findpython         conda-forge/noarch::findpython-0.8.0-pyhcf101f3_1 
  font-ttf-dejavu-s~ conda-forge/noarch::font-ttf-dejavu-sans-mono-2.37-hab24e00_0 
  font-ttf-inconsol~ conda-forge/noarch::font-ttf-inconsolata-3.000-h77eed37_0 
  font-ttf-source-c~ conda-forge/noarch::font-ttf-source-code-pro-2.038-h77eed37_0 
  font-ttf-ubuntu    conda-forge/noarch::font-ttf-ubuntu-0.83-h77eed37_3 
  fonts-conda-ecosy~ conda-forge/noarch::fonts-conda-ecosystem-1-0 
  fonts-conda-forge  conda-forge/noarch::fonts-conda-forge-1-hc364b38_1 
  fribidi            conda-forge/linux-64::fribidi-1.0.16-h7cc23a3_2 
  gdk-pixbuf         conda-forge/linux-64::gdk-pixbuf-2.44.6-h2b0a6b4_0 
  giflib             conda-forge/linux-64::giflib-5.2.2-ha257d8a_1 
  glcontext          conda-forge/linux-64::glcontext-3.0.0-py312h835c14e_2 
  glib               conda-forge/linux-64::glib-2.48.0-3 
  glslang            conda-forge/linux-64::glslang-16.5.0-h980caa0_2 
  importlib-metadata conda-forge/noarch::importlib-metadata-9.0.1-pyhcf101f3_0 
  importlib_resourc~ conda-forge/noarch::importlib_resources-7.1.0-pyhd8ed1ab_0 
  intel-gmmlib       conda-forge/linux-64::intel-gmmlib-22.10.0-hb700be7_0 
  intel-media-driver conda-forge/linux-64::intel-media-driver-25.3.4-hecca717_0 
  isosurfaces        conda-forge/noarch::isosurfaces-0.1.2-pyhd8ed1ab_0 
  jack               conda-forge/linux-64::jack-1.9.22-hf4617a5_3 
  jaraco.classes     conda-forge/noarch::jaraco.classes-3.4.0-pyhcf101f3_3 
  jaraco.context     conda-forge/noarch::jaraco.context-6.1.2-pyhcf101f3_0 
  jaraco.functools   conda-forge/noarch::jaraco.functools-4.6.0-pyhcf101f3_0 
  jeepney            conda-forge/noarch::jeepney-0.9.0-pyhd8ed1ab_0 
  keyring            conda-forge/noarch::keyring-25.7.0-pyha804496_0 
  lame               conda-forge/linux-64::lame-3.100-h166bdaf_1003 
  leptonica          conda-forge/linux-64::leptonica-1.87.0-h12c84f9_1 
  libarchive         pkgs/main/linux-64::libarchive-3.8.7-hb3cce40_0 
  libass             conda-forge/linux-64::libass-0.17.4-h96ad9f0_0 
  libcap             conda-forge/linux-64::libcap-2.77-hd0affe5_1 
  libflac            conda-forge/linux-64::libflac-1.5.0-he200343_1 
  libfreetype        conda-forge/linux-64::libfreetype-2.14.1-ha770c72_0 
  libfreetype6       conda-forge/linux-64::libfreetype6-2.14.1-h73754d4_0 
  libgd              conda-forge/linux-64::libgd-2.3.3-h5fbf134_12 
  libgomp            pkgs/main/linux-64::libgomp-15.2.0-h4751f2c_8 
  libltdl            conda-forge/linux-64::libltdl-2.4.3a-h5888daf_0 
  liblzma            conda-forge/linux-64::liblzma-5.8.2-hb03c661_0 
  librsvg            pkgs/main/linux-64::librsvg-2.62.1-h4367520_0 
  libsndfile         conda-forge/linux-64::libsndfile-1.2.2-hc7d488a_2 
  libsystemd0        conda-forge/linux-64::libsystemd0-260.2-h6569c3e_0 
  libtheora          conda-forge/linux-64::libtheora-1.2.0-h85c0a6d_0 
  libtool            conda-forge/linux-64::libtool-2.5.4-h5888daf_0 
  libudev1           conda-forge/linux-64::libudev1-260.2-h6569c3e_0 
  libva              conda-forge/linux-64::libva-2.22.0-h4f16b4b_2 
  libvpl             conda-forge/linux-64::libvpl-2.15.0-h54a6638_1 
  libvpx             pkgs/main/linux-64::libvpx-1.16.0-h4b463fa_0 
  manim              conda-forge/noarch::manim-0.18.1-pyhd8ed1ab_1 
  manimpango         conda-forge/linux-64::manimpango-0.6.0-py312h6802ac9_0 
  mapbox_earcut      conda-forge/linux-64::mapbox_earcut-1.0.3-py312hf890105_2 
  markdown-it-py     conda-forge/noarch::markdown-it-py-4.2.0-pyhd8ed1ab_0 
  mdurl              conda-forge/noarch::mdurl-0.1.2-pyhd8ed1ab_1 
  moderngl           conda-forge/linux-64::moderngl-5.11.1-py312h4f16dfd_1 
  moderngl-window    conda-forge/noarch::moderngl-window-3.1.1-pyhcf101f3_2 
  more-itertools     conda-forge/noarch::more-itertools-11.1.0-pyhcf101f3_0 
  mpg123             conda-forge/linux-64::mpg123-1.32.9-h8142553_0 
  msgpack-python     conda-forge/linux-64::msgpack-python-1.2.2-py312h9be0db6_2 
  networkx           conda-forge/noarch::networkx-3.6.1-pyhcf101f3_0 
  openh264           conda-forge/linux-64::openh264-2.6.0-h8c49934_2 
  openjpeg           conda-forge/linux-64::openjpeg-2.5.4-h55fea9a_0 
  pango              conda-forge/linux-64::pango-1.56.4-hadf4263_0 
  pbs-installer      conda-forge/noarch::pbs-installer-2026.9.1-pyhd8ed1ab_0 
  pcre               conda-forge/linux-64::pcre-8.45-h9c3ff4c_0 
  pkginfo            conda-forge/noarch::pkginfo-1.12.1.2-pyhd8ed1ab_0 
  poetry             conda-forge/noarch::poetry-2.4.3-pyhc9edb4d_0 
  poetry-core        conda-forge/noarch::poetry-core-2.4.0-pyhcf101f3_0 
  pulseaudio         conda-forge/linux-64::pulseaudio-17.0-haebf07f_3 
  pulseaudio-client  conda-forge/linux-64::pulseaudio-client-17.0-h9a6aba3_3 
  pulseaudio-daemon  conda-forge/linux-64::pulseaudio-daemon-17.0-h33dcb6b_3 
  pycairo            conda-forge/linux-64::pycairo-1.29.0-py312h2596900_1 
  pydub              conda-forge/noarch::pydub-0.25.1-pyhd8ed1ab_1 
  pyglet             conda-forge/noarch::pyglet-2.1.15-pyhd8ed1ab_0 
  pyglm              conda-forge/linux-64::pyglm-2.8.3-py312h9be0db6_3 
  pyproject_hooks    conda-forge/noarch::pyproject_hooks-1.2.0-pyhd8ed1ab_1 
  python-build       conda-forge/noarch::python-build-1.6.0-pyhc364b38_0 
  python-discovery   conda-forge/noarch::python-discovery-1.6.0-pyhcf101f3_0 
  python-installer   conda-forge/noarch::python-installer-1.0.1-pyh332efcf_0 
  rapidfuzz          conda-forge/linux-64::rapidfuzz-3.14.6-py312ha6a3dbb_0 
  requests-toolbelt  conda-forge/noarch::requests-toolbelt-1.0.0-pyhd8ed1ab_1 
  rich               conda-forge/noarch::rich-15.0.0-pyhcf101f3_0 
  screeninfo         conda-forge/linux-64::screeninfo-0.8.1-py312h7900ff3_3 
  secretstorage      conda-forge/linux-64::secretstorage-3.5.0-py312h7900ff3_1 
  shaderc            conda-forge/linux-64::shaderc-2025.5-h718be3e_1 
  shellingham        conda-forge/noarch::shellingham-1.5.4-pyhd8ed1ab_2 
  skia-pathops       conda-forge/linux-64::skia-pathops-0.9.2-py312h9be0db6_2 
  soxr               conda-forge/linux-64::soxr-0.1.3-h0b41bf4_3 
  srt                conda-forge/noarch::srt-3.5.3-pyhd8ed1ab_1 
  svgelements        conda-forge/noarch::svgelements-1.9.6-pyhcf101f3_1 
  svt-av1            conda-forge/linux-64::svt-av1-3.1.2-hecca717_0 
  tesseract          pkgs/main/linux-64::tesseract-5.2.0-hc7272f1_5 
  tomli              conda-forge/noarch::tomli-2.4.1-pyhcf101f3_0 
  tomlkit            conda-forge/noarch::tomlkit-0.15.1-pyhcf101f3_0 
  tqdm               conda-forge/noarch::tqdm-4.70.0-pyh8f84b5b_0 
  trove-classifiers  conda-forge/noarch::trove-classifiers-2026.6.1.19-pyhcf101f3_0 
  virtualenv         conda-forge/noarch::virtualenv-21.7.8-pyh5ded981_0 
  watchdog           conda-forge/linux-64::watchdog-6.0.0-py312h20c3967_4 
  wayland-protocols  conda-forge/noarch::wayland-protocols-1.49-hd8ed1ab_0 
  xorg-libxi         conda-forge/linux-64::xorg-libxi-1.8.2-hb9d3cd8_0 
  xorg-libxtst       conda-forge/linux-64::xorg-libxtst-1.2.5-hb9d3cd8_3 
  zipp               conda-forge/noarch::zipp-4.1.0-pyhcf101f3_0 
  zstandard          conda-forge/linux-64::zstandard-0.25.0-py312h1b36aeb_4 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: | /home/willem/anaconda3/envs/ds312/bin/gdk-pixbuf-query-loaders: error while loading shared libraries: libffi.so.6: cannot open shared object file: No such file or directory                                                                                                                            
ERROR: Failed to update gdk-pixbuf's cache, some plugins may not be found.                                                                                      
To fix this, activate the environment and run:                                                                                                                  
    gdk-pixbuf-query-loaders --update-cache                                                                                                                     
                                                                                                                                                               / /home/willem/anaconda3/envs/ds312/bin/gdk-pixbuf-query-loaders: error while loading shared libraries: libffi.so.6: cannot open shared object file: No such file or directory
ERROR: Failed to update gdk-pixbuf's cache, some plugins may not be found.
To fix this, activate the environment and run:
    gdk-pixbuf-query-loaders --update-cache
                                                                                                                                                               done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -n ds312 --all --no-pin
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    backports-1.1              |     pyhd3eb1b0_1           6 KB
    crashtest-0.4.1            |  py312h06a4308_2          20 KB
    dulwich-1.2.12             |  py312h553a12c_0         2.0 MB
    gdk-pixbuf-2.44.6          |       h268f190_1         512 KB
    importlib_resources-7.1.0  |  py312h06a4308_1          84 KB
    libass-0.17.4              |       h682e061_2         129 KB
    libtheora-1.2.0            |       h32ad74f_1         417 KB
    libva-2.23.0               |       h80f46ad_0         214 KB
    openjpeg-2.5.4             |       h81d0f9f_2         106 KB
    ------------------------------------------------------------
                                           Total:         3.5 MB

The following NEW packages will be INSTALLED:

  glib-tools         pkgs/main/linux-64::glib-tools-2.88.3-h9fad118_0 

The following packages will be REMOVED:

  pcre-8.45-h9c3ff4c_0

The following packages will be UPDATED:

  backports          conda-forge::backports-1.0-pyhd8ed1ab~ --> pkgs/main::backports-1.1-pyhd3eb1b0_1 
  click              conda-forge/noarch::click-8.4.2-pyhc9~ --> pkgs/main/linux-64::click-8.5.0-py312h06a4308_0 
  crashtest          conda-forge/noarch::crashtest-0.4.1-p~ --> pkgs/main/linux-64::crashtest-0.4.1-py312h06a4308_2 
  dulwich            conda-forge::dulwich-1.2.10-py312hc76~ --> pkgs/main::dulwich-1.2.12-py312h553a12c_0 
  gdk-pixbuf         conda-forge::gdk-pixbuf-2.44.6-h2b0a6~ --> pkgs/main::gdk-pixbuf-2.44.6-h268f190_1 
  glib                           conda-forge::glib-2.48.0-3 --> pkgs/main::glib-2.88.3-h617169b_0 
  importlib_resourc~ conda-forge/noarch::importlib_resourc~ --> pkgs/main/linux-64::importlib_resources-7.1.0-py312h06a4308_1 
  libass              conda-forge::libass-0.17.4-h96ad9f0_0 --> pkgs/main::libass-0.17.4-h682e061_2 
  libtheora          conda-forge::libtheora-1.2.0-h85c0a6d~ --> pkgs/main::libtheora-1.2.0-h32ad74f_1 
  libva                conda-forge::libva-2.22.0-h4f16b4b_2 --> pkgs/main::libva-2.23.0-h80f46ad_0 
  openjpeg           conda-forge::openjpeg-2.5.4-h55fea9a_0 --> pkgs/main::openjpeg-2.5.4-h81d0f9f_2 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: done                                                                    
```

</details>


## Testing the installation
Leads to the same problems. Therefore, we will create a fresh new environment: `manim312`

<details>

```bash
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.18.1                                                                                                                                         
                                                                                                                                                                
Animation 0: Create(Circle):   0%|                                                                                                       | 0/15 [00:00<?, ?it/s][vost#0:0 @ 0x60e886b94040] Unknown encoder 'libx264'                                                                                                            
[vost#0:0 @ 0x60e886b94040] Error selecting an encoder                                                                                                           
Error opening output file /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/media/videos/main/480p15/partial_movie_files/CreateCircle/1185818338_41213021_223132457.mp4.                                                                                                                                           
Error opening output files: Encoder not found                                                                                                                    
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮                                                             
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/cli/render/commands.py:120  │
│ in render                                                                                        │
│                                                                                                  │
│   117 │   │   │   try:                                                                           │
│   118 │   │   │   │   with tempconfig({}):                                                       │
│   119 │   │   │   │   │   scene = SceneClass()                                                   │
│ ❱ 120 │   │   │   │   │   scene.render()                                                         │
│   121 │   │   │   except Exception:                                                              │
│   122 │   │   │   │   error_console.print_exception()                                            │
│   123 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:229 in       │
│ render                                                                                           │
│                                                                                                  │
│    226 │   │   """                                                                               │
│    227 │   │   self.setup()                                                                      │
│    228 │   │   try:                                                                              │
│ ❱  229 │   │   │   self.construct()                                                              │
│    230 │   │   except EndSceneEarlyException:                                                    │
│    231 │   │   │   pass                                                                          │
│    232 │   │   except RerunSceneException as e:                                                  │
│                                                                                                  │
│ /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/main.py:8 in construct          │
│                                                                                                  │
│   5 │   def construct(self):                                                                     │
│   6 │   │   circle = Circle()  # create a circle                                                 │
│   7 │   │   circle.set_fill(PINK, opacity=0.5)  # set the color and transparency                 │
│ ❱ 8 │   │   self.play(Create(circle))  # show the circle on screen                               │
│   9                                                                                              │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1092 in play │
│                                                                                                  │
│   1089 │   │   │   return                                                                        │
│   1090 │   │                                                                                     │
│   1091 │   │   start_time = self.renderer.time                                                   │
│ ❱ 1092 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1093 │   │   run_time = self.renderer.time - start_time                                        │
│   1094 │   │   if subcaption:                                                                    │
│   1095 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 114 in play                                                                                      │
│                                                                                                  │
│   111 │   │   │   # In this case, as there is only a wait, it will be the length of the wait.    │
│   112 │   │   │   self.freeze_current_frame(scene.duration)                                      │
│   113 │   │   else:                                                                              │
│ ❱ 114 │   │   │   scene.play_internal()                                                          │
│   115 │   │   self.file_writer.end_animation(not self.skip_animations)                           │
│   116 │   │                                                                                      │
│   117 │   │   self.num_plays += 1                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1261 in      │
│ play_internal                                                                                    │
│                                                                                                  │
│   1258 │   │   for t in self.time_progression:                                                   │
│   1259 │   │   │   self.update_to_time(t)                                                        │
│   1260 │   │   │   if not skip_rendering and not self.skip_animation_preview:                    │
│ ❱ 1261 │   │   │   │   self.renderer.render(self, t, self.moving_mobjects)                       │
│   1262 │   │   │   if self.stop_condition is not None and self.stop_condition():                 │
│   1263 │   │   │   │   self.time_progression.close()                                             │
│   1264 │   │   │   │   break                                                                     │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 160 in render                                                                                    │
│                                                                                                  │
│   157 │                                                                                          │
│   158 │   def render(self, scene, time, moving_mobjects):                                        │
│   159 │   │   self.update_frame(scene, moving_mobjects)                                          │
│ ❱ 160 │   │   self.add_frame(self.get_frame())                                                   │
│   161 │                                                                                          │
│   162 │   def get_frame(self):                                                                   │
│   163 │   │   """                                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 190 in add_frame                                                                                 │
│                                                                                                  │
│   187 │   │   │   return                                                                         │
│   188 │   │   self.time += num_frames * dt                                                       │
│   189 │   │   for _ in range(num_frames):                                                        │
│ ❱ 190 │   │   │   self.file_writer.write_frame(frame)                                            │
│   191 │                                                                                          │
│   192 │   def freeze_current_frame(self, duration: float):                                       │
│   193 │   │   """Adds a static frame to the movie for a given duration. The static frame is th   │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 391 in write_frame                                                                               │
│                                                                                                  │
│   388 │   │   elif config.renderer == RendererType.CAIRO:                                        │
│   389 │   │   │   frame = frame_or_renderer                                                      │
│   390 │   │   │   if write_to_movie():                                                           │
│ ❱ 391 │   │   │   │   self.writing_process.stdin.write(frame.tobytes())                          │
│   392 │   │   │   if is_png_format() and not config["dry_run"]:                                  │
│   393 │   │   │   │   self.output_image_from_array(frame)                                        │
│   394                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
BrokenPipeError: [Errno 32] Broken pipe
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ gdk-pixbuf-query-loaders --update-cache
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -n ds312 --all --no-pin
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

# All requested packages already installed.

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.18.1

Animation 0: Create(Circle):   0%|                                                                                                       | 0/15 [00:00<?, ?it/s][vost#0:0 @ 0x6180da47c040] Unknown encoder 'libx264'                                                                                                             
[vost#0:0 @ 0x6180da47c040] Error selecting an encoder                                                                                                           
Error opening output file /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/media/videos/main/480p15/partial_movie_files/CreateCircle/1185818338_41213021_223132457.mp4.                                                                                                                                           
Error opening output files: Encoder not found                                                                                                                    
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮                                                             
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/cli/render/commands.py:120  │
│ in render                                                                                        │
│                                                                                                  │
│   117 │   │   │   try:                                                                           │
│   118 │   │   │   │   with tempconfig({}):                                                       │
│   119 │   │   │   │   │   scene = SceneClass()                                                   │
│ ❱ 120 │   │   │   │   │   scene.render()                                                         │
│   121 │   │   │   except Exception:                                                              │
│   122 │   │   │   │   error_console.print_exception()                                            │
│   123 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:229 in       │
│ render                                                                                           │
│                                                                                                  │
│    226 │   │   """                                                                               │
│    227 │   │   self.setup()                                                                      │
│    228 │   │   try:                                                                              │
│ ❱  229 │   │   │   self.construct()                                                              │
│    230 │   │   except EndSceneEarlyException:                                                    │
│    231 │   │   │   pass                                                                          │
│    232 │   │   except RerunSceneException as e:                                                  │
│                                                                                                  │
│ /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/main.py:8 in construct          │
│                                                                                                  │
│   5 │   def construct(self):                                                                     │
│   6 │   │   circle = Circle()  # create a circle                                                 │
│   7 │   │   circle.set_fill(PINK, opacity=0.5)  # set the color and transparency                 │
│ ❱ 8 │   │   self.play(Create(circle))  # show the circle on screen                               │
│   9                                                                                              │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1092 in play │
│                                                                                                  │
│   1089 │   │   │   return                                                                        │
│   1090 │   │                                                                                     │
│   1091 │   │   start_time = self.renderer.time                                                   │
│ ❱ 1092 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1093 │   │   run_time = self.renderer.time - start_time                                        │
│   1094 │   │   if subcaption:                                                                    │
│   1095 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 114 in play                                                                                      │
│                                                                                                  │
│   111 │   │   │   # In this case, as there is only a wait, it will be the length of the wait.    │
│   112 │   │   │   self.freeze_current_frame(scene.duration)                                      │
│   113 │   │   else:                                                                              │
│ ❱ 114 │   │   │   scene.play_internal()                                                          │
│   115 │   │   self.file_writer.end_animation(not self.skip_animations)                           │
│   116 │   │                                                                                      │
│   117 │   │   self.num_plays += 1                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1261 in      │
│ play_internal                                                                                    │
│                                                                                                  │
│   1258 │   │   for t in self.time_progression:                                                   │
│   1259 │   │   │   self.update_to_time(t)                                                        │
│   1260 │   │   │   if not skip_rendering and not self.skip_animation_preview:                    │
│ ❱ 1261 │   │   │   │   self.renderer.render(self, t, self.moving_mobjects)                       │
│   1262 │   │   │   if self.stop_condition is not None and self.stop_condition():                 │
│   1263 │   │   │   │   self.time_progression.close()                                             │
│   1264 │   │   │   │   break                                                                     │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 160 in render                                                                                    │
│                                                                                                  │
│   157 │                                                                                          │
│   158 │   def render(self, scene, time, moving_mobjects):                                        │
│   159 │   │   self.update_frame(scene, moving_mobjects)                                          │
│ ❱ 160 │   │   self.add_frame(self.get_frame())                                                   │
│   161 │                                                                                          │
│   162 │   def get_frame(self):                                                                   │
│   163 │   │   """                                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 190 in add_frame                                                                                 │
│                                                                                                  │
│   187 │   │   │   return                                                                         │
│   188 │   │   self.time += num_frames * dt                                                       │
│   189 │   │   for _ in range(num_frames):                                                        │
│ ❱ 190 │   │   │   self.file_writer.write_frame(frame)                                            │
│   191 │                                                                                          │
│   192 │   def freeze_current_frame(self, duration: float):                                       │
│   193 │   │   """Adds a static frame to the movie for a given duration. The static frame is th   │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 391 in write_frame                                                                               │
│                                                                                                  │
│   388 │   │   elif config.renderer == RendererType.CAIRO:                                        │
│   389 │   │   │   frame = frame_or_renderer                                                      │
│   390 │   │   │   if write_to_movie():                                                           │
│ ❱ 391 │   │   │   │   self.writing_process.stdin.write(frame.tobytes())                          │
│   392 │   │   │   if is_png_format() and not config["dry_run"]:                                  │
│   393 │   │   │   │   self.output_image_from_array(frame)                                        │
│   394                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
BrokenPipeError: [Errno 32] Broken pipe
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -n ds312 -c conda-forge ffmpeg x264 av --force-reinstall
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312

  added / updated specs:
    - av
    - ffmpeg
    - x264


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    av-18.0.0                  |  py312h46547aa_0         1.3 MB  conda-forge
    ------------------------------------------------------------
                                           Total:         1.3 MB

The following NEW packages will be INSTALLED:

  av                 conda-forge/linux-64::av-18.0.0-py312h46547aa_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.18.1

Animation 0: Create(Circle):   0%|                                                                                                       | 0/15 [00:00<?, ?it/s][vost#0:0 @ 0x575c6b6a4040] Unknown encoder 'libx264'                                                                                                             
[vost#0:0 @ 0x575c6b6a4040] Error selecting an encoder                                                                                                           
Error opening output file /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/media/videos/main/480p15/partial_movie_files/CreateCircle/1185818338_41213021_223132457.mp4.                                                                                                                                           
Error opening output files: Encoder not found                                                                                                                    
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮                                                             
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/cli/render/commands.py:120  │
│ in render                                                                                        │
│                                                                                                  │
│   117 │   │   │   try:                                                                           │
│   118 │   │   │   │   with tempconfig({}):                                                       │
│   119 │   │   │   │   │   scene = SceneClass()                                                   │
│ ❱ 120 │   │   │   │   │   scene.render()                                                         │
│   121 │   │   │   except Exception:                                                              │
│   122 │   │   │   │   error_console.print_exception()                                            │
│   123 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:229 in       │
│ render                                                                                           │
│                                                                                                  │
│    226 │   │   """                                                                               │
│    227 │   │   self.setup()                                                                      │
│    228 │   │   try:                                                                              │
│ ❱  229 │   │   │   self.construct()                                                              │
│    230 │   │   except EndSceneEarlyException:                                                    │
│    231 │   │   │   pass                                                                          │
│    232 │   │   except RerunSceneException as e:                                                  │
│                                                                                                  │
│ /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/main.py:8 in construct          │
│                                                                                                  │
│   5 │   def construct(self):                                                                     │
│   6 │   │   circle = Circle()  # create a circle                                                 │
│   7 │   │   circle.set_fill(PINK, opacity=0.5)  # set the color and transparency                 │
│ ❱ 8 │   │   self.play(Create(circle))  # show the circle on screen                               │
│   9                                                                                              │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1092 in play │
│                                                                                                  │
│   1089 │   │   │   return                                                                        │
│   1090 │   │                                                                                     │
│   1091 │   │   start_time = self.renderer.time                                                   │
│ ❱ 1092 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1093 │   │   run_time = self.renderer.time - start_time                                        │
│   1094 │   │   if subcaption:                                                                    │
│   1095 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 114 in play                                                                                      │
│                                                                                                  │
│   111 │   │   │   # In this case, as there is only a wait, it will be the length of the wait.    │
│   112 │   │   │   self.freeze_current_frame(scene.duration)                                      │
│   113 │   │   else:                                                                              │
│ ❱ 114 │   │   │   scene.play_internal()                                                          │
│   115 │   │   self.file_writer.end_animation(not self.skip_animations)                           │
│   116 │   │                                                                                      │
│   117 │   │   self.num_plays += 1                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1261 in      │
│ play_internal                                                                                    │
│                                                                                                  │
│   1258 │   │   for t in self.time_progression:                                                   │
│   1259 │   │   │   self.update_to_time(t)                                                        │
│   1260 │   │   │   if not skip_rendering and not self.skip_animation_preview:                    │
│ ❱ 1261 │   │   │   │   self.renderer.render(self, t, self.moving_mobjects)                       │
│   1262 │   │   │   if self.stop_condition is not None and self.stop_condition():                 │
│   1263 │   │   │   │   self.time_progression.close()                                             │
│   1264 │   │   │   │   break                                                                     │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 160 in render                                                                                    │
│                                                                                                  │
│   157 │                                                                                          │
│   158 │   def render(self, scene, time, moving_mobjects):                                        │
│   159 │   │   self.update_frame(scene, moving_mobjects)                                          │
│ ❱ 160 │   │   self.add_frame(self.get_frame())                                                   │
│   161 │                                                                                          │
│   162 │   def get_frame(self):                                                                   │
│   163 │   │   """                                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 190 in add_frame                                                                                 │
│                                                                                                  │
│   187 │   │   │   return                                                                         │
│   188 │   │   self.time += num_frames * dt                                                       │
│   189 │   │   for _ in range(num_frames):                                                        │
│ ❱ 190 │   │   │   self.file_writer.write_frame(frame)                                            │
│   191 │                                                                                          │
│   192 │   def freeze_current_frame(self, duration: float):                                       │
│   193 │   │   """Adds a static frame to the movie for a given duration. The static frame is th   │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 391 in write_frame                                                                               │
│                                                                                                  │
│   388 │   │   elif config.renderer == RendererType.CAIRO:                                        │
│   389 │   │   │   frame = frame_or_renderer                                                      │
│   390 │   │   │   if write_to_movie():                                                           │
│ ❱ 391 │   │   │   │   self.writing_process.stdin.write(frame.tobytes())                          │
│   392 │   │   │   if is_png_format() and not config["dry_run"]:                                  │
│   393 │   │   │   │   self.output_image_from_array(frame)                                        │
│   394                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
BrokenPipeError: [Errno 32] Broken pipe
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda -n ds312 -c conda-forge update manim
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'ds312' (choose from activate, build, check, clean, commands, compare, config, content-trust, convert, create, deactivate, debug, develop, doctor, env, export, index, info, init, inspect, install, list, menuinst, metapackage, notices, package, pypi, remove, rename, render, repo, repoquery, run, search, self, skeleton, token, uninstall, update, upgrade)
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda -c conda-forge update manim
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'conda-forge' (choose from activate, build, check, clean, commands, compare, config, content-trust, convert, create, deactivate, debug, develop, doctor, env, export, index, info, init, inspect, install, list, menuinst, metapackage, notices, package, pypi, remove, rename, render, repo, repoquery, run, search, self, skeleton, token, uninstall, update, upgrade)
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -n ds312 -c conda-forge manim
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312

  added / updated specs:
    - manim


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    audioop-lts-0.2.2          |  py312h5253ce2_2          13 KB  conda-forge
    libnsl-2.0.1               |       hb9d3cd8_1          33 KB  conda-forge
    libsqlite-3.53.4           |       h13e7031_1         952 KB  conda-forge
    libxcrypt-4.4.38           |       h280c20c_0         100 KB  conda-forge
    manimpango-0.6.1           |  py312hb0bc1a6_2         118 KB  conda-forge
    python-3.12.12             |hfe2f287_0_cpython        30.1 MB  conda-forge
    xorg-xorgproto-2024.1      |       hb9d3cd8_1         552 KB  conda-forge
    ------------------------------------------------------------
                                           Total:        31.8 MB

The following NEW packages will be INSTALLED:

  audioop-lts        conda-forge/linux-64::audioop-lts-0.2.2-py312h5253ce2_2 
  libharfbuzz        conda-forge/linux-64::libharfbuzz-14.4.0-h23af247_1 
  libnsl             conda-forge/linux-64::libnsl-2.0.1-hb9d3cd8_1 
  libsqlite          conda-forge/linux-64::libsqlite-3.53.4-h13e7031_1 
  libxcrypt          conda-forge/linux-64::libxcrypt-4.4.38-h280c20c_0 
  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-hb9d3cd8_1004 

The following packages will be REMOVED:

  click-default-group-1.2.4-pyhd8ed1ab_1

The following packages will be UPDATED:

  fontconfig         pkgs/main::fontconfig-2.17.1-h062c814~ --> conda-forge::fontconfig-2.18.3-h4db4eae_1 
  freetype            pkgs/main::freetype-2.14.1-hf5b9546_0 --> conda-forge::freetype-2.14.3-ha770c72_2 
  libfreetype                             2.14.1-ha770c72_0 --> 2.14.3-ha770c72_2 
  libfreetype6                            2.14.1-h73754d4_0 --> 2.14.3-h5e6c136_2 
  libpng                pkgs/main::libpng-1.6.56-h22898a0_0 --> conda-forge::libpng-1.6.58-h922cc85_1 
  libuuid              pkgs/main::libuuid-1.41.5-h5eee18b_0 --> conda-forge::libuuid-2.42.3-hcfc3c73_0 
  manim                                 0.18.1-pyhd8ed1ab_1 --> 0.20.1-pyhc364b38_0 
  manimpango                          0.6.0-py312h6802ac9_0 --> 0.6.1-py312hb0bc1a6_2 
  pango                                   1.56.4-hadf4263_0 --> 1.58.2-h7bb47b9_1 
  python               pkgs/main::python-3.12.11-h22baa00_0 --> conda-forge::python-3.12.12-hfe2f287_0_cpython 
  xorg-libsm         pkgs/main::xorg-libsm-1.2.6-h9b100fa_0 --> conda-forge::xorg-libsm-1.2.6-h0d788c3_1 

The following packages will be SUPERSEDED by a higher-priority channel:

  xorg-xorgproto     pkgs/main::xorg-xorgproto-2024.1-h47b~ --> conda-forge::xorg-xorgproto-2024.1-hb9d3cd8_1 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: done                                                                                                                                     
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.20.1                                                                                                                                         

╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/cli/render/commands.py:125  │
│ in render                                                                                        │
│                                                                                                  │
│   122 │   │   │   try:                                                                           │
│   123 │   │   │   │   with tempconfig({}):                                                       │
│   124 │   │   │   │   │   scene = SceneClass()                                                   │
│ ❱ 125 │   │   │   │   │   scene.render()                                                         │
│   126 │   │   │   except Exception:                                                              │
│   127 │   │   │   │   error_console.print_exception()                                            │
│   128 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:259 in       │
│ render                                                                                           │
│                                                                                                  │
│    256 │   │   """                                                                               │
│    257 │   │   self.setup()                                                                      │
│    258 │   │   try:                                                                              │
│ ❱  259 │   │   │   self.construct()                                                              │
│    260 │   │   except EndSceneEarlyException:                                                    │
│    261 │   │   │   pass                                                                          │
│    262 │   │   except RerunSceneException:                                                       │
│                                                                                                  │
│ /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/main.py:8 in construct          │
│                                                                                                  │
│   5 │   def construct(self):                                                                     │
│   6 │   │   circle = Circle()  # create a circle                                                 │
│   7 │   │   circle.set_fill(PINK, opacity=0.5)  # set the color and transparency                 │
│ ❱ 8 │   │   self.play(Create(circle))  # show the circle on screen                               │
│   9                                                                                              │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1194 in play │
│                                                                                                  │
│   1191 │   │   │   return                                                                        │
│   1192 │   │                                                                                     │
│   1193 │   │   start_time = self.time                                                            │
│ ❱ 1194 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1195 │   │   run_time = self.time - start_time                                                 │
│   1196 │   │   if subcaption:                                                                    │
│   1197 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 108 in play                                                                                      │
│                                                                                                  │
│   105 │   │   │   {"h": str(self.animations_hashes[:5])},                                        │
│   106 │   │   )                                                                                  │
│   107 │   │                                                                                      │
│ ❱ 108 │   │   self.file_writer.begin_animation(not self.skip_animations)                         │
│   109 │   │   scene.begin_animations()                                                           │
│   110 │   │                                                                                      │
│   111 │   │   # Save a static image, to avoid rendering non moving objects.                      │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 416 in begin_animation                                                                           │
│                                                                                                  │
│   413 │   │   │   Whether or not to write to a video file.                                       │
│   414 │   │   """                                                                                │
│   415 │   │   if write_to_movie() and allow_write:                                               │
│ ❱ 416 │   │   │   self.open_partial_movie_stream(file_path=file_path)                            │
│   417 │                                                                                          │
│   418 │   def end_animation(self, allow_write: bool = False) -> None:                            │
│   419 │   │   """Internally used by Manim to stop streaming to FFMPEG gracefully.                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 570 in open_partial_movie_stream                                                                 │
│                                                                                                  │
│   567 │   │   │   partial_movie_file_pix_fmt = "argb"                                            │
│   568 │   │                                                                                      │
│   569 │   │   video_container = av.open(file_path, mode="w")                                     │
│ ❱ 570 │   │   stream = video_container.add_stream(                                               │
│   571 │   │   │   partial_movie_file_codec,                                                      │
│   572 │   │   │   rate=fps,                                                                      │
│   573 │   │   │   options=av_options,                                                            │
│                                                                                                  │
│ in av.container.output.OutputContainer.add_stream:108                                            │
│                                                                                                  │
│ in av.codec.codec.Codec.__cinit__:121                                                            │
│                                                                                                  │
│ in av.codec.codec.Codec._init:130                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
UnknownCodecError: libx264
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -c conda-forge ffmpeg x264 av --force-reinstall
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds312

  added / updated specs:
    - av
    - ffmpeg
    - x264



Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds312
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -n ds312 -c conda-forge manim
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

# All requested packages already installed.

(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.20.1

╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/cli/render/commands.py:125  │
│ in render                                                                                        │
│                                                                                                  │
│   122 │   │   │   try:                                                                           │
│   123 │   │   │   │   with tempconfig({}):                                                       │
│   124 │   │   │   │   │   scene = SceneClass()                                                   │
│ ❱ 125 │   │   │   │   │   scene.render()                                                         │
│   126 │   │   │   except Exception:                                                              │
│   127 │   │   │   │   error_console.print_exception()                                            │
│   128 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:259 in       │
│ render                                                                                           │
│                                                                                                  │
│    256 │   │   """                                                                               │
│    257 │   │   self.setup()                                                                      │
│    258 │   │   try:                                                                              │
│ ❱  259 │   │   │   self.construct()                                                              │
│    260 │   │   except EndSceneEarlyException:                                                    │
│    261 │   │   │   pass                                                                          │
│    262 │   │   except RerunSceneException:                                                       │
│                                                                                                  │
│ /home/willem/git/DataAnalysisWithPythonAndPySpark/src/manim_test/main.py:8 in construct          │
│                                                                                                  │
│   5 │   def construct(self):                                                                     │
│   6 │   │   circle = Circle()  # create a circle                                                 │
│   7 │   │   circle.set_fill(PINK, opacity=0.5)  # set the color and transparency                 │
│ ❱ 8 │   │   self.play(Create(circle))  # show the circle on screen                               │
│   9                                                                                              │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene.py:1194 in play │
│                                                                                                  │
│   1191 │   │   │   return                                                                        │
│   1192 │   │                                                                                     │
│   1193 │   │   start_time = self.time                                                            │
│ ❱ 1194 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1195 │   │   run_time = self.time - start_time                                                 │
│   1196 │   │   if subcaption:                                                                    │
│   1197 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/renderer/cairo_renderer.py: │
│ 108 in play                                                                                      │
│                                                                                                  │
│   105 │   │   │   {"h": str(self.animations_hashes[:5])},                                        │
│   106 │   │   )                                                                                  │
│   107 │   │                                                                                      │
│ ❱ 108 │   │   self.file_writer.begin_animation(not self.skip_animations)                         │
│   109 │   │   scene.begin_animations()                                                           │
│   110 │   │                                                                                      │
│   111 │   │   # Save a static image, to avoid rendering non moving objects.                      │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 416 in begin_animation                                                                           │
│                                                                                                  │
│   413 │   │   │   Whether or not to write to a video file.                                       │
│   414 │   │   """                                                                                │
│   415 │   │   if write_to_movie() and allow_write:                                               │
│ ❱ 416 │   │   │   self.open_partial_movie_stream(file_path=file_path)                            │
│   417 │                                                                                          │
│   418 │   def end_animation(self, allow_write: bool = False) -> None:                            │
│   419 │   │   """Internally used by Manim to stop streaming to FFMPEG gracefully.                │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds312/lib/python3.12/site-packages/manim/scene/scene_file_writer.py: │
│ 570 in open_partial_movie_stream                                                                 │
│                                                                                                  │
│   567 │   │   │   partial_movie_file_pix_fmt = "argb"                                            │
│   568 │   │                                                                                      │
│   569 │   │   video_container = av.open(file_path, mode="w")                                     │
│ ❱ 570 │   │   stream = video_container.add_stream(                                               │
│   571 │   │   │   partial_movie_file_codec,                                                      │
│   572 │   │   │   rate=fps,                                                                      │
│   573 │   │   │   options=av_options,                                                            │
│                                                                                                  │
│ in av.container.output.OutputContainer.add_stream:108                                            │
│                                                                                                  │
│ in av.codec.codec.Codec.__cinit__:121                                                            │
│                                                                                                  │
│ in av.codec.codec.Codec._init:130                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
UnknownCodecError: libx264
(ds312) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$
```

</details>
