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

# Session

## update
```bash
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda --version
conda 26.7.2
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ python --version
Python 3.14.4
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda update -n ds314 --all --no-pin
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    async-lru-2.3.0            |  py314h06a4308_0          29 KB
    babel-2.18.0               |  py314h06a4308_0        13.3 MB
    beautifulsoup4-4.15.0      |  py314h06a4308_0         266 KB
    bleach-6.4.0               |  py314h06a4308_0         345 KB
    bottleneck-1.6.0           |  py314hc849d88_0         142 KB
    brotlicffi-1.2.0.1         |  py314h7354ed3_0         375 KB
    certifi-2026.7.22          |  py314h06a4308_0         136 KB
    cffi-2.1.1                 |  py314h3b52fac_0         296 KB
    charset-normalizer-3.4.7   |  py314h06a4308_0         140 KB
    debugpy-1.8.21             |  py314h7354ed3_0         2.6 MB
    decorator-5.3.1            |  py314h06a4308_0          43 KB
    executing-2.2.1            |  py314h06a4308_1         340 KB
    fonttools-4.63.0           |  py314h47b2149_0         6.0 MB
    gmpy2-2.3.1                |  py314h1cd8627_0         279 KB
    idna-3.18                  |  py314h06a4308_0         187 KB
    ipykernel-7.3.0            |  py314h6fa48dc_0         263 KB
    ipython-9.15.0             |  py314h06a4308_0         1.3 MB
    jedi-0.20.0                |  py314h06a4308_0         3.0 MB
    jinja2-3.1.6               |  py314h06a4308_1         363 KB
    json5-0.15.0               |  py314h06a4308_0          76 KB
    jsonschema-4.26.0          |  py314h06a4308_0         199 KB
    jupyter_client-8.9.1       |  py314h06a4308_0         252 KB
    jupyter_server-2.20.0      |  py314h06a4308_0         616 KB
    jupyterlab-4.5.9           |  py314h06a4308_1         8.0 MB
    kiwisolver-1.5.0           |  py314h7354ed3_0          77 KB
    libegl-1.7.0               |       h4cac700_3          43 KB
    libgl-1.7.0                |       hb0f338c_3         129 KB
    libglvnd-1.7.0             |       h47b2149_3         130 KB
    libglx-1.7.0               |       h71acf41_3          77 KB
    libmpdec-4.0.1             |       h47b2149_0          88 KB
    libopengl-1.7.0            |       h4cac700_3          50 KB
    markupsafe-3.0.3           |  py314h47b2149_0          29 KB
    matplotlib-3.11.0          |  py314h06a4308_0           7 KB
    matplotlib-base-3.11.0     |  py314h54cb298_0         9.3 MB
    matplotlib-inline-0.2.2    |  py314h06a4308_0          21 KB
    mistune-3.3.3              |  py314h06a4308_0         188 KB
    mkl-service-2.7.2          |  py314h365c7f6_0          75 KB
    mkl_random-1.4.1           |  py314h973aee8_0         393 KB
    mpmath-1.4.0               |  py314h06a4308_0         1.1 MB
    nbclient-0.11.0            |  py314h06a4308_0          93 KB
    nbconvert-core-7.17.1      |  py314h06a4308_0         509 KB
    nbformat-5.11.0            |  py314h06a4308_0         159 KB
    nest-asyncio2-1.7.2        |  py314h06a4308_0          25 KB
    notebook-7.5.7             |  py314h06a4308_0         5.8 MB
    numexpr-2.14.2             |  py314hee8fbad_0         214 KB
    numpy-2.4.6                |  py314ha8834a8_0          20 KB
    numpy-base-2.4.6           |  py314h7c74580_0         8.1 MB
    packaging-26.3             |  py314h06a4308_0         390 KB
    parso-0.8.7                |  py314h06a4308_0         235 KB
    pip-26.2.1                 |     pyh0d26453_0         1.1 MB
    platformdirs-4.11.0        |  py314h06a4308_0          63 KB
    prompt-toolkit-3.0.53      |  py314h06a4308_0         773 KB
    psutil-7.2.2               |  py314h47b2149_0         288 KB
    pyparsing-3.3.2            |  py314h06a4308_0         5.9 MB
    python-3.14.7              |h2bd7c14_101_cp314        35.5 MB
    python-dotenv-1.2.2        |  py314h06a4308_0          56 KB
    python-fastjsonschema-2.22.1|  py314h06a4308_0         259 KB
    python-json-logger-4.1.0   |  py314h06a4308_0          36 KB
    python_abi-3.14            |          4_cp314           5 KB
    pytz-2026.3.post1          |  py314h06a4308_0         223 KB
    requests-2.34.2            |  py314h06a4308_0         191 KB
    setuptools-83.0.0          |  py314h06a4308_0         1.6 MB
    soupsieve-2.8.4            |  py314h06a4308_0          95 KB
    tk-9.0.4                   |       h3840b71_1         4.0 MB
    tornado-6.5.7              |  py314h47b2149_0         897 KB
    traitlets-5.15.0           |  py314h06a4308_0         223 KB
    typing-extensions-4.16.0   |  py314h06a4308_0           9 KB
    typing_extensions-4.16.0   |  py314h06a4308_0         101 KB
    urllib3-2.7.0              |  py314h06a4308_0         360 KB
    wayland-1.25.0             |       h9bbe5da_0         325 KB
    wcwidth-0.8.2              |  py314h06a4308_0         359 KB
    webencodings-0.6.1         |  py314h06a4308_0          22 KB
    xcb-util-cursor-0.1.6      |       h9d8ba18_0          20 KB
    xcb-util-image-0.4.1       |       hb2b27ac_0          23 KB
    xkeyboard-config-2.48      |       h658fd9e_1         943 KB
    xorg-libice-1.1.2          |       h0525522_1          57 KB
    xorg-libsm-1.2.6           |       h984eb1c_1          26 KB
    xorg-libx11-1.8.13         |       h65de747_0         817 KB
    xorg-libxfixes-6.0.2       |       h5f4defd_0          19 KB
    xorg-libxrandr-1.5.5       |       he366e75_0          28 KB
    xorg-libxrender-0.9.12     |       h5f4defd_1          32 KB
    xorg-libxxf86vm-1.1.7      |       hc450a19_0          17 KB
    xorg-xorgproto-2025.1      |       h47b2149_0         555 KB
    ------------------------------------------------------------
                                           Total:       120.3 MB

The following NEW packages will be INSTALLED:

  libllvm22          pkgs/main/linux-64::libllvm22-22.1.2-hfb1d434_0 
  nest-asyncio2      pkgs/main/linux-64::nest-asyncio2-1.7.2-py314h06a4308_0 

The following packages will be REMOVED:

  libgomp-15.2.0-h4751f2c_7
  libllvm21-21.1.8-h5ad376a_0
  nest-asyncio-1.5.1-pyhd3eb1b0_0

The following packages will be UPDATED:

  _openmp_mutex                                   5.1-1_gnu --> 5.1-52_gnu 
  async-lru                           2.0.5-py314h06a4308_0 --> 2.3.0-py314h06a4308_0 
  babel                              2.17.0-py314h06a4308_0 --> 2.18.0-py314h06a4308_0 
  beautifulsoup4                     4.14.3-py314h06a4308_0 --> 4.15.0-py314h06a4308_0 
  bleach                              6.3.0-py314h06a4308_1 --> 6.4.0-py314h06a4308_0 
  bottleneck                          1.4.2-py314h6a40391_1 --> 1.6.0-py314hc849d88_0 
  brotlicffi                        1.2.0.0-py314h7354ed3_0 --> 1.2.0.1-py314h7354ed3_0 
  c-ares                                  1.34.6-hd44998d_0 --> 1.34.7-hd44998d_0 
  ca-certificates    conda-forge/noarch::ca-certificates-2~ --> pkgs/main/linux-64::ca-certificates-2026.8.13-h06a4308_0 
  certifi            conda-forge/noarch::certifi-2026.5.20~ --> pkgs/main/linux-64::certifi-2026.7.22-py314h06a4308_0 
  cffi                                2.0.0-py314h4eded50_1 --> 2.1.1-py314h3b52fac_0 
  charset-normalizer                  3.4.4-py314h06a4308_0 --> 3.4.7-py314h06a4308_0 
  cyrus-sasl                              2.1.28-h83b0a09_4 --> 2.1.28-h2f687bf_5 
  dav1d                                    1.5.3-h3e43c27_0 --> 1.5.3-h12c9f22_1 
  debugpy                            1.8.16-py314hbdd6827_1 --> 1.8.21-py314h7354ed3_0 
  decorator                           5.2.1-py314h06a4308_0 --> 5.3.1-py314h06a4308_0 
  executing                           2.2.1-py314h06a4308_0 --> 2.2.1-py314h06a4308_1 
  expat                                    2.8.0-h7354ed3_0 --> 2.8.4-h7354ed3_0 
  fonttools                          4.62.1-py314h47b2149_0 --> 4.63.0-py314h47b2149_0 
  fribidi                                 1.0.16-h9fb5f84_0 --> 1.0.16-h10f3c28_1 
  gettext            conda-forge::gettext-0.21.1-h27087fc_0 --> pkgs/main::gettext-0.25.1-h92eb808_0 
  gflags                                   2.3.0-h861b1fb_0 --> 2.3.1-h86178c3_1 
  gmp                                      6.3.0-h6a678d5_0 --> 6.3.0-haace2f4_1 
  gmpy2                               2.2.2-py314ha78e65c_0 --> 2.3.1-py314h1cd8627_0 
  graphite2                               1.3.14-h295c915_1 --> 1.3.15-h9ba177b_0 
  idna                                 3.11-py314h06a4308_0 --> 3.18-py314h06a4308_0 
  intel-openmp                       2025.0.0-h06a4308_1171 --> 2025.0.0-h06a4308_1172 
  ipykernel                           7.2.0-py314h6fa48dc_0 --> 7.3.0-py314h6fa48dc_0 
  ipython                            9.11.0-py314h06a4308_0 --> 9.15.0-py314h06a4308_0 
  jansson                                   2.14-h5eee18b_1 --> 2.15.0-hbcba0ee_0 
  jedi                               0.19.2-py314h06a4308_0 --> 0.20.0-py314h06a4308_0 
  jinja2                              3.1.6-py314h06a4308_0 --> 3.1.6-py314h06a4308_1 
  jpeg                                        9f-h5ce9db8_0 --> 9f-he7e78df_1 
  json5                              0.12.1-py314h06a4308_0 --> 0.15.0-py314h06a4308_0 
  jsonschema                         4.25.1-py314h06a4308_0 --> 4.26.0-py314h06a4308_0 
  jupyter_client                      8.8.0-py314h06a4308_0 --> 8.9.1-py314h06a4308_0 
  jupyter_server                     2.17.0-py314h06a4308_1 --> 2.20.0-py314h06a4308_0 
  jupyterlab                          4.5.7-py314h06a4308_0 --> 4.5.9-py314h06a4308_1 
  kiwisolver                          1.4.9-py314h24d9097_0 --> 1.5.0-py314h7354ed3_0 
  libcups                                 2.4.15-hbe4054b_0 --> 2.4.19-h23114ae_0 
  libdrm                                 2.4.124-h5eee18b_0 --> 2.4.134-h9c74679_0 
  libegl                                   1.7.0-h5eee18b_2 --> 1.7.0-h4cac700_3 
  libexpat                                 2.8.0-h7354ed3_0 --> 2.8.4-h7354ed3_0 
  libffi                                   3.4.8-hc5d346e_2 --> 3.4.8-h06d3fd0_3 
  libgcc                                  15.2.0-h69a1729_7 --> 15.2.0-h69a1729_8 
  libgcc-ng                               15.2.0-h166f726_7 --> 15.2.0-h166f726_8 
  libgfortran                             15.2.0-h166f726_7 --> 15.2.0-h166f726_8 
  libgfortran5                            15.2.0-hc633d37_7 --> 15.2.0-hc633d37_8 
  libgl                                    1.7.0-h5eee18b_2 --> 1.7.0-hb0f338c_3 
  libglib                                 2.86.3-h8b17d9a_0 --> 2.88.3-ha16e27a_0 
  libglvnd                                 1.7.0-h5eee18b_2 --> 1.7.0-h47b2149_3 
  libglx                                   1.7.0-h5eee18b_2 --> 1.7.0-h71acf41_3 
  libgrpc                                 1.78.0-h79c45ec_0 --> 1.78.0-h01ccb81_1 
  libkrb5                                 1.22.1-h869c75e_1 --> 1.22.2-hbd13c29_0 
  libmpdec                                 4.0.0-h5eee18b_0 --> 4.0.1-h47b2149_0 
  libopengl                                1.7.0-h5eee18b_2 --> 1.7.0-h4cac700_3 
  libopenjpeg                              2.5.4-hee96239_1 --> 2.5.4-h47b2149_2 
  libpq                                     17.9-h0cb448f_1 --> 17.10-h0cb448f_2 
  libsodium                               1.0.21-h81596b7_0 --> 1.0.21-h83fc4cd_1 
  libssh2                                 1.11.1-h251f7ec_0 --> 1.11.1-hfbabe93_1 
  libstdcxx                               15.2.0-h39759b7_7 --> 15.2.0-h39759b7_8 
  libstdcxx-ng                            15.2.0-hc03a8fd_7 --> 15.2.0-hc03a8fd_8 
  libzlib                                  1.3.1-h47b2149_1 --> 1.3.2-h47b2149_0 
  lmdb                                    0.9.31-hb25bd0a_0 --> 1.0.0-hfe55579_0 
  lz4-c                                    1.9.4-h6a678d5_1 --> 1.9.4-h7354ed3_5 
  markupsafe                          3.0.2-py314h5eee18b_0 --> 3.0.3-py314h47b2149_0 
  matplotlib                         3.10.9-py314h06a4308_0 --> 3.11.0-py314h06a4308_0 
  matplotlib-base                    3.10.9-py314h54cb298_0 --> 3.11.0-py314h54cb298_0 
  matplotlib-inline                   0.2.1-py314h06a4308_0 --> 0.2.2-py314h06a4308_0 
  mesalib                                 25.1.5-h3583ad3_3 --> 25.1.5-h3583ad3_5 
  mistune                             3.1.2-py314h06a4308_0 --> 3.3.3-py314h06a4308_0 
  mkl                                 2025.0.0-hacee8c2_941 --> 2025.0.0-h6d8faa4_942 
  mkl-service                         2.5.2-py314hacdc0fc_0 --> 2.7.2-py314h365c7f6_0 
  mkl_random                          1.3.0-py314hda4e5d8_0 --> 1.4.1-py314h973aee8_0 
  mpmath                              1.3.0-py314h06a4308_0 --> 1.4.0-py314h06a4308_0 
  nbclient                           0.10.4-py314h06a4308_0 --> 0.11.0-py314h06a4308_0 
  nbconvert-core                     7.17.0-py314h06a4308_0 --> 7.17.1-py314h06a4308_0 
  nbformat                           5.10.4-py314h06a4308_0 --> 5.11.0-py314h06a4308_0 
  ncurses                                    6.5-h7934f7d_0 --> 6.6-hfaaeb4e_0 
  notebook                            7.5.5-py314h06a4308_0 --> 7.5.7-py314h06a4308_0 
  numexpr                            2.14.1-py314hee8fbad_1 --> 2.14.2-py314hee8fbad_0 
  numpy                               2.4.4-py314hc4ca38b_1 --> 2.4.6-py314ha8834a8_0 
  numpy-base                          2.4.4-py314h7c74580_1 --> 2.4.6-py314h7c74580_0 
  packaging                            26.0-py314h06a4308_0 --> 26.3-py314h06a4308_0 
  parso                               0.8.5-py314h06a4308_0 --> 0.8.7-py314h06a4308_0 
  pip                                   26.0.1-pyh0d26453_1 --> 26.2.1-pyh0d26453_0 
  pixman                                  0.46.4-h7934f7d_0 --> 0.46.4-h86ba9f7_1 
  platformdirs                        4.9.4-py314h06a4308_0 --> 4.11.0-py314h06a4308_0 
  prompt-toolkit                     3.0.52-py314h06a4308_1 --> 3.0.53-py314h06a4308_0 
  prompt_toolkit                          3.0.52-hd3eb1b0_1 --> 3.0.53-hd3eb1b0_0 
  psutil                              7.0.0-py314hee96239_1 --> 7.2.2-py314h47b2149_0 
  pthread-stubs                              0.3-h0ce48e5_1 --> 0.3-h47b2149_2 
  pyparsing                           3.2.5-py314h06a4308_0 --> 3.3.2-py314h06a4308_0 
  python                          3.14.4-h490e9c7_100_cp314 --> 3.14.7-h2bd7c14_101_cp314 
  python-dotenv                       1.2.1-py314h06a4308_0 --> 1.2.2-py314h06a4308_0 
  python-fastjsonsc~                 2.21.2-py314h06a4308_0 --> 2.22.1-py314h06a4308_0 
  python-json-logger                  4.0.0-py314h06a4308_0 --> 4.1.0-py314h06a4308_0 
  python-tzdata                         2026.2-pyhd3eb1b0_0 --> 2026.3-pyhd3eb1b0_0 
  python_abi                                   3.14-2_cp314 --> 3.14-4_cp314 
  pytz                         2026.1.post1-py314h06a4308_0 --> 2026.3.post1-py314h06a4308_0 
  qtdeclarative                           6.11.0-h69798bf_0 --> 6.11.0-h89ee561_1 
  qtsvg                                   6.11.0-h6af1df9_0 --> 6.11.0-hbecefc2_1 
  qttools                                 6.11.0-h50cdde4_0 --> 6.11.0-h0af0a4d_1 
  qtwebchannel                            6.11.0-h27b496b_0 --> 6.11.0-h7ebffc9_1 
  qtwebsockets                            6.11.0-h8bda742_0 --> 6.11.0-h03d4248_1 
  requests                           2.33.1-py314h06a4308_0 --> 2.34.2-py314h06a4308_0 
  setuptools                         82.0.1-py314h06a4308_0 --> 83.0.0-py314h06a4308_0 
  soupsieve                             2.5-py314h06a4308_0 --> 2.8.4-py314h06a4308_0 
  sqlite                                  3.51.2-h3e8d24a_0 --> 3.53.2-h795bf6d_0 
  tk                                      8.6.15-h54e0aa7_0 --> 9.0.4-h3840b71_1 
  tornado                             6.5.5-py314h47b2149_0 --> 6.5.7-py314h47b2149_0 
  traitlets                          5.14.3-py314h06a4308_0 --> 5.15.0-py314h06a4308_0 
  typing-extensions                  4.15.0-py314h06a4308_0 --> 4.16.0-py314h06a4308_0 
  typing_extensions                  4.15.0-py314h06a4308_0 --> 4.16.0-py314h06a4308_0 
  tzdata                                   2026a-he532380_0 --> 2026c-he532380_0 
  urllib3                             2.6.3-py314h06a4308_0 --> 2.7.0-py314h06a4308_0 
  utf8proc                                 2.6.1-h5eee18b_1 --> 2.11.3-h47b2149_0 
  wayland                                 1.24.0-hdac8c69_0 --> 1.25.0-h9bbe5da_0 
  wcwidth                            0.2.14-py314h06a4308_0 --> 0.8.2-py314h06a4308_0 
  webencodings                        0.5.1-py314h06a4308_2 --> 0.6.1-py314h06a4308_0 
  xcb-util-cursor                          0.1.5-h5eee18b_0 --> 0.1.6-h9d8ba18_0 
  xcb-util-image                           0.4.0-h5eee18b_2 --> 0.4.1-hb2b27ac_0 
  xkeyboard-config                          2.44-h382ed1a_1 --> 2.48-h658fd9e_1 
  xorg-libice                              1.1.2-h9b100fa_0 --> 1.1.2-h0525522_1 
  xorg-libsm                               1.2.6-h9b100fa_0 --> 1.2.6-h984eb1c_1 
  xorg-libx11                             1.8.12-h9b100fa_1 --> 1.8.13-h65de747_0 
  xorg-libxext                             1.3.6-h9b100fa_0 --> 1.3.7-h1ce37a7_0 
  xorg-libxfixes                           6.0.1-h9b100fa_0 --> 6.0.2-h5f4defd_0 
  xorg-libxrandr                           1.5.4-h9b100fa_0 --> 1.5.5-he366e75_0 
  xorg-libxrender                         0.9.12-h9b100fa_0 --> 0.9.12-h5f4defd_1 
  xorg-libxxf86vm                          1.1.6-h9b100fa_0 --> 1.1.7-hc450a19_0 
  xorg-xorgproto                          2024.1-h5eee18b_1 --> 2025.1-h47b2149_0 
  yaml                                     0.2.5-h7b6447c_0 --> 0.2.5-h591646f_1 
  zlib                                     1.3.1-h47b2149_1 --> 1.3.2-h47b2149_0 

The following packages will be SUPERSEDED by a higher-priority channel:

  gettext-tools      conda-forge::gettext-tools-0.25.1-h3f~ --> pkgs/main::gettext-tools-0.25.1-h6a67909_0 

The following packages will be REVISED:

  libasprintf                             0.25.1-ha6c9436_1 --> 0.25.1-hf2ab22a_0 
  libasprintf-devel                       0.25.1-ha6c9436_1 --> 0.25.1-hf2ab22a_0 
  libgettextpo                            0.25.1-h64fc44f_1 --> 0.25.1-hf2ab22a_0 
  libgettextpo-devel                      0.25.1-h64fc44f_1 --> 0.25.1-hf2ab22a_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: done                                                                                                                                     
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ python --version                                                             
Python 3.14.7                                                                                                                                                   
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda install -c conda-forge manim                                                               
Channels:             
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - manim


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    alsa-lib-1.2.16.1          |       h7cc23a3_1         581 KB  conda-forge
    audioop-lts-0.2.2          |  py314h0f05182_2          39 KB  conda-forge
    av-18.0.0                  |  py314hb413b2f_0         1.3 MB  conda-forge
    backports-1.0              |     pyhd8ed1ab_5           7 KB  conda-forge
    backports.tarfile-1.2.0    |     pyhcf101f3_2          35 KB  conda-forge
    cachecontrol-0.14.4        |     pyha770c72_0          24 KB  conda-forge
    cachecontrol-with-filecache-0.14.4|     pyhd8ed1ab_0           8 KB  conda-forge
    cleo-2.1.0                 |     pyhd8ed1ab_1          60 KB  conda-forge
    click-8.4.2                |     pyhc90fa1f_0         105 KB  conda-forge
    cloup-3.0.9                |     pyhd8ed1ab_0          48 KB  conda-forge
    colorama-0.4.6             |     pyhd8ed1ab_1          26 KB  conda-forge
    crashtest-0.4.1            |     pyhd8ed1ab_1          11 KB  conda-forge
    cryptography-50.0.1        |  py314hcc0303b_0         1.8 MB  conda-forge
    dbus-1.16.2                |       he8c428d_2         439 KB  conda-forge
    distlib-0.4.3              |     pyhcf101f3_0         297 KB  conda-forge
    dulwich-1.2.10             |  py314h7e8cd81_3         2.9 MB  conda-forge
    ffmpeg-8.1.2               |       h5758e9d_0        11.3 MB
    fftw-3.3.11                |nompi_h3b011a4_100         2.1 MB  conda-forge
    filelock-3.32.5            |     pyhd8ed1ab_0          77 KB  conda-forge
    findpython-0.8.0           |     pyhcf101f3_1          23 KB  conda-forge
    font-ttf-dejavu-sans-mono-2.37|       hab24e00_0         388 KB  conda-forge
    font-ttf-inconsolata-3.000 |       h77eed37_0          94 KB  conda-forge
    font-ttf-source-code-pro-2.038|       h77eed37_0         684 KB  conda-forge
    font-ttf-ubuntu-0.83       |       h77eed37_3         1.5 MB  conda-forge
    fontconfig-2.18.3          |       h4db4eae_1         289 KB  conda-forge
    fonts-conda-ecosystem-1    |                0           4 KB  conda-forge
    fonts-conda-forge-1        |       hc364b38_1           4 KB  conda-forge
    freetype-2.14.3            |       ha770c72_2         171 KB  conda-forge
    gdk-pixbuf-2.44.6          |       h8a2e0e6_0         511 KB
    giflib-5.2.2               |       ha257d8a_1          76 KB  conda-forge
    glcontext-3.0.0            |  py314hc75f4c6_4          24 KB  conda-forge
    glib-2.88.3                |       h617169b_0         506 KB
    glib-tools-2.88.3          |       h9fad118_0         114 KB
    glslang-16.5.0             |       h980caa0_2         1.4 MB  conda-forge
    gstreamer-orc-0.4.43       |       he11a670_0         408 KB  conda-forge
    harfbuzz-12.3.2            |       h6083320_0         1.9 MB  conda-forge
    icu-78.3                   |  py310h44b86e0_2        13.8 MB  conda-forge
    importlib-metadata-9.0.1   |     pyhcf101f3_0          34 KB  conda-forge
    importlib_resources-7.1.0  |     pyhd8ed1ab_0          34 KB  conda-forge
    intel-gmmlib-22.10.0       |       hb700be7_0         990 KB  conda-forge
    intel-media-driver-25.3.4  |       hecca717_0         8.0 MB  conda-forge
    isosurfaces-0.1.2          |     pyhd8ed1ab_0          16 KB  conda-forge
    jack-1.9.22                |       hf4617a5_3         450 KB  conda-forge
    jaraco.classes-3.4.0       |     pyhcf101f3_3          14 KB  conda-forge
    jaraco.context-6.1.2       |     pyhcf101f3_0          16 KB  conda-forge
    jaraco.functools-4.6.0     |     pyhcf101f3_0          19 KB  conda-forge
    jeepney-0.9.0              |     pyhd8ed1ab_0          39 KB  conda-forge
    keyring-25.7.0             |     pyha804496_0          37 KB  conda-forge
    lame-3.100                 |    h166bdaf_1003         496 KB  conda-forge
    leptonica-1.87.0           |       h3b8441c_0         1.9 MB
    libarchive-3.8.7           |       hb3cce40_0         867 KB
    libass-0.17.4              |       h96ad9f0_0         149 KB  conda-forge
    libcap-2.77                |       hd0affe5_1         122 KB  conda-forge
    libflac-1.5.0              |       he200343_1         415 KB  conda-forge
    libfreetype-2.14.3         |       ha770c72_2           8 KB  conda-forge
    libfreetype6-2.14.3        |       h5e6c136_2         379 KB  conda-forge
    libgd-2.3.3                |       h798115a_5         216 KB
    libharfbuzz-14.4.0         |       h23af247_1         1.3 MB  conda-forge
    libhwloc-2.12.1            |default_hafda6a7_1003         2.3 MB  conda-forge
    libllvm22-22.1.8           |       hf7376ad_1        42.3 MB  conda-forge
    libltdl-2.4.3a             |       h5888daf_0          38 KB  conda-forge
    liblzma-5.8.2              |       hb03c661_0         111 KB  conda-forge
    libogg-1.3.5               |       hd0c01bc_1         213 KB  conda-forge
    libopus-1.6.1              |       hebe6cf0_1         322 KB  conda-forge
    libpng-1.6.58              |       h922cc85_1         309 KB  conda-forge
    librsvg-2.62.1             |       h4367520_0         3.3 MB
    libsndfile-1.2.2           |       hc7d488a_2         347 KB  conda-forge
    libsystemd0-260.2          |       h6569c3e_0         519 KB  conda-forge
    libtheora-1.2.0            |       h85c0a6d_0         170 KB  conda-forge
    libtool-2.5.4              |       h5888daf_0         405 KB  conda-forge
    libudev1-260.2             |       h6569c3e_0         168 KB  conda-forge
    libuuid-2.42.3             |       hcfc3c73_0          39 KB  conda-forge
    libva-2.24.1               |       he1eb515_0         217 KB  conda-forge
    libvorbis-1.3.7            |       h54a6638_2         279 KB  conda-forge
    libvpl-2.15.0              |       h54a6638_1         281 KB  conda-forge
    libwebp-1.6.0              |       h089d785_0          90 KB
    libxkbcommon-1.13.2        |       h51789e4_1         920 KB  conda-forge
    libxml2-2.14.6             |       he237659_3          46 KB  conda-forge
    libxml2-16-2.14.6          |       hca6bf5a_3         555 KB  conda-forge
    libxslt-1.1.43             |       h711ed8c_1         240 KB  conda-forge
    lxml-6.1.2                 |  py314h78220e7_0         1.5 MB  conda-forge
    manim-0.20.1               |     pyhc364b38_0         470 KB  conda-forge
    manimpango-0.6.1           |  py314h1d171c9_2         118 KB  conda-forge
    mapbox_earcut-1.0.3        |  py314h3a4f467_2          91 KB  conda-forge
    moderngl-5.12.0            |  py314ha0b5721_0         135 KB  conda-forge
    moderngl-window-3.1.1      |     pyhcf101f3_2         357 KB  conda-forge
    more-itertools-11.1.0      |     pyhcf101f3_0          70 KB  conda-forge
    mpg123-1.32.9              |       h8142553_0         476 KB  conda-forge
    msgpack-python-1.2.2       |  py314h5383ef5_2         113 KB  conda-forge
    networkx-3.6.1             |     pyhcf101f3_0         1.5 MB  conda-forge
    openh264-2.6.0             |       h8c49934_2         720 KB  conda-forge
    openjpeg-2.5.4             |       h55fea9a_0         347 KB  conda-forge
    openssl-3.6.4              |       h781a0a9_0         3.1 MB  conda-forge
    pango-1.58.2               |       h7bb47b9_1         461 KB  conda-forge
    pbs-installer-2026.9.1     |     pyhd8ed1ab_0          70 KB  conda-forge
    pkginfo-1.12.1.2           |     pyhd8ed1ab_0          30 KB  conda-forge
    poetry-2.4.3               |     pyhc9edb4d_0         200 KB  conda-forge
    poetry-core-2.4.0          |     pyhcf101f3_0         282 KB  conda-forge
    pulseaudio-17.0            |       haebf07f_3          18 KB  conda-forge
    pulseaudio-client-17.0     |       h9a6aba3_3         733 KB  conda-forge
    pulseaudio-daemon-17.0     |       h33dcb6b_3         856 KB  conda-forge
    pycairo-1.29.1             |  py314hb1bbd57_1         118 KB  conda-forge
    pydub-0.25.1               |     pyhd8ed1ab_1          33 KB  conda-forge
    pyglet-2.1.15              |     pyhd8ed1ab_0         713 KB  conda-forge
    pyglm-2.8.3                |  py314h5383ef5_3         1.6 MB  conda-forge
    pyproject_hooks-1.2.0      |     pyhd8ed1ab_1          15 KB  conda-forge
    python-3.14.0              |h5989046_101_cp314        35.0 MB  conda-forge
    python-build-1.6.0         |     pyhc364b38_0          33 KB  conda-forge
    python-discovery-1.6.0     |     pyhcf101f3_0          38 KB  conda-forge
    python-installer-1.0.1     |     pyh332efcf_0         234 KB  conda-forge
    qtbase-6.11.0              |       h68dfb5d_1        12.2 MB
    rapidfuzz-3.14.6           |  py314hc75f4c6_0         2.1 MB  conda-forge
    requests-toolbelt-1.0.0    |     pyhd8ed1ab_1          43 KB  conda-forge
    screeninfo-0.8.1           |  py314hdafbbf9_3          33 KB  conda-forge
    secretstorage-3.5.0        |  py314hdafbbf9_1          34 KB  conda-forge
    shaderc-2025.5             |       h718be3e_1         111 KB  conda-forge
    shellingham-1.5.4          |     pyhd8ed1ab_2          15 KB  conda-forge
    skia-pathops-0.9.2         |  py314h5383ef5_2         409 KB  conda-forge
    soxr-0.1.3                 |       h0b41bf4_3         128 KB  conda-forge
    srt-3.5.3                  |     pyhd8ed1ab_1          24 KB  conda-forge
    svgelements-1.9.6          |     pyhcf101f3_1         121 KB  conda-forge
    svt-av1-3.1.2              |       hecca717_0         2.6 MB  conda-forge
    tesseract-5.2.0            |       hc7272f1_5       168.1 MB
    tk-8.6.13                  | noxft_h1df4ec4_4         3.4 MB  conda-forge
    tomli-2.4.1                |     pyhcf101f3_0          21 KB  conda-forge
    tomlkit-0.15.1             |     pyhcf101f3_0          48 KB  conda-forge
    tqdm-4.70.0                |     pyh8f84b5b_0          96 KB  conda-forge
    trove-classifiers-2026.6.1.19|     pyhcf101f3_0          24 KB  conda-forge
    virtualenv-21.7.8          |     pyh5ded981_0         3.7 MB  conda-forge
    watchdog-6.0.0             |  py314h9e666f3_4         159 KB  conda-forge
    wayland-protocols-1.49     |       hd8ed1ab_0         144 KB  conda-forge
    xorg-libsm-1.2.6           |       h0d788c3_1          30 KB  conda-forge
    xorg-libxi-1.8.3           |       h7cc23a3_1          48 KB  conda-forge
    xorg-libxtst-1.2.5         |       h7cc23a3_4          34 KB  conda-forge
    xorg-xextproto-7.3.0       |    hb9d3cd8_1004          30 KB  conda-forge
    xorg-xorgproto-2025.1      |       hebe6cf0_2         581 KB  conda-forge
    zipp-4.1.0                 |     pyhcf101f3_0          24 KB  conda-forge
    zstandard-0.25.0           |  py314hfe1a184_4         462 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       355.5 MB

The following NEW packages will be INSTALLED:

  alsa-lib           conda-forge/linux-64::alsa-lib-1.2.16.1-h7cc23a3_1 
  audioop-lts        conda-forge/linux-64::audioop-lts-0.2.2-py314h0f05182_2 
  av                 conda-forge/linux-64::av-18.0.0-py314hb413b2f_0 
  backports          conda-forge/noarch::backports-1.0-pyhd8ed1ab_5 
  backports.tarfile  conda-forge/noarch::backports.tarfile-1.2.0-pyhcf101f3_2 
  cachecontrol       conda-forge/noarch::cachecontrol-0.14.4-pyha770c72_0 
  cachecontrol-with~ conda-forge/noarch::cachecontrol-with-filecache-0.14.4-pyhd8ed1ab_0 
  cleo               conda-forge/noarch::cleo-2.1.0-pyhd8ed1ab_1 
  click              conda-forge/noarch::click-8.4.2-pyhc90fa1f_0 
  cloup              conda-forge/noarch::cloup-3.0.9-pyhd8ed1ab_0 
  colorama           conda-forge/noarch::colorama-0.4.6-pyhd8ed1ab_1 
  crashtest          conda-forge/noarch::crashtest-0.4.1-pyhd8ed1ab_1 
  cryptography       conda-forge/linux-64::cryptography-50.0.1-py314hcc0303b_0 
  dbus               conda-forge/linux-64::dbus-1.16.2-he8c428d_2 
  distlib            conda-forge/noarch::distlib-0.4.3-pyhcf101f3_0 
  dulwich            conda-forge/linux-64::dulwich-1.2.10-py314h7e8cd81_3 
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
  gdk-pixbuf         pkgs/main/linux-64::gdk-pixbuf-2.44.6-h8a2e0e6_0 
  giflib             conda-forge/linux-64::giflib-5.2.2-ha257d8a_1 
  glcontext          conda-forge/linux-64::glcontext-3.0.0-py314hc75f4c6_4 
  glib               pkgs/main/linux-64::glib-2.88.3-h617169b_0 
  glib-tools         pkgs/main/linux-64::glib-tools-2.88.3-h9fad118_0 
  glslang            conda-forge/linux-64::glslang-16.5.0-h980caa0_2 
  gstreamer-orc      conda-forge/linux-64::gstreamer-orc-0.4.43-he11a670_0 
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
  leptonica          pkgs/main/linux-64::leptonica-1.87.0-h3b8441c_0 
  libarchive         pkgs/main/linux-64::libarchive-3.8.7-hb3cce40_0 
  libass             conda-forge/linux-64::libass-0.17.4-h96ad9f0_0 
  libcap             conda-forge/linux-64::libcap-2.77-hd0affe5_1 
  libflac            conda-forge/linux-64::libflac-1.5.0-he200343_1 
  libfreetype        conda-forge/linux-64::libfreetype-2.14.3-ha770c72_2 
  libfreetype6       conda-forge/linux-64::libfreetype6-2.14.3-h5e6c136_2 
  libgd              pkgs/main/linux-64::libgd-2.3.3-h798115a_5 
  libgomp            pkgs/main/linux-64::libgomp-15.2.0-h4751f2c_8 
  libharfbuzz        conda-forge/linux-64::libharfbuzz-14.4.0-h23af247_1 
  libltdl            conda-forge/linux-64::libltdl-2.4.3a-h5888daf_0 
  liblzma            conda-forge/linux-64::liblzma-5.8.2-hb03c661_0 
  libogg             conda-forge/linux-64::libogg-1.3.5-hd0c01bc_1 
  libopus            conda-forge/linux-64::libopus-1.6.1-hebe6cf0_1 
  librsvg            pkgs/main/linux-64::librsvg-2.62.1-h4367520_0 
  libsndfile         conda-forge/linux-64::libsndfile-1.2.2-hc7d488a_2 
  libsystemd0        conda-forge/linux-64::libsystemd0-260.2-h6569c3e_0 
  libtheora          conda-forge/linux-64::libtheora-1.2.0-h85c0a6d_0 
  libtool            conda-forge/linux-64::libtool-2.5.4-h5888daf_0 
  libudev1           conda-forge/linux-64::libudev1-260.2-h6569c3e_0 
  libva              conda-forge/linux-64::libva-2.24.1-he1eb515_0 
  libvorbis          conda-forge/linux-64::libvorbis-1.3.7-h54a6638_2 
  libvpl             conda-forge/linux-64::libvpl-2.15.0-h54a6638_1 
  libvpx             pkgs/main/linux-64::libvpx-1.16.0-h4b463fa_0 
  libwebp            pkgs/main/linux-64::libwebp-1.6.0-h089d785_0 
  libxml2-16         conda-forge/linux-64::libxml2-16-2.14.6-hca6bf5a_3 
  manim              conda-forge/noarch::manim-0.20.1-pyhc364b38_0 
  manimpango         conda-forge/linux-64::manimpango-0.6.1-py314h1d171c9_2 
  mapbox_earcut      conda-forge/linux-64::mapbox_earcut-1.0.3-py314h3a4f467_2 
  moderngl           conda-forge/linux-64::moderngl-5.12.0-py314ha0b5721_0 
  moderngl-window    conda-forge/noarch::moderngl-window-3.1.1-pyhcf101f3_2 
  more-itertools     conda-forge/noarch::more-itertools-11.1.0-pyhcf101f3_0 
  mpg123             conda-forge/linux-64::mpg123-1.32.9-h8142553_0 
  msgpack-python     conda-forge/linux-64::msgpack-python-1.2.2-py314h5383ef5_2 
  networkx           conda-forge/noarch::networkx-3.6.1-pyhcf101f3_0 
  openh264           conda-forge/linux-64::openh264-2.6.0-h8c49934_2 
  openjpeg           conda-forge/linux-64::openjpeg-2.5.4-h55fea9a_0 
  pango              conda-forge/linux-64::pango-1.58.2-h7bb47b9_1 
  pbs-installer      conda-forge/noarch::pbs-installer-2026.9.1-pyhd8ed1ab_0 
  pkginfo            conda-forge/noarch::pkginfo-1.12.1.2-pyhd8ed1ab_0 
  poetry             conda-forge/noarch::poetry-2.4.3-pyhc9edb4d_0 
  poetry-core        conda-forge/noarch::poetry-core-2.4.0-pyhcf101f3_0 
  pulseaudio         conda-forge/linux-64::pulseaudio-17.0-haebf07f_3 
  pulseaudio-client  conda-forge/linux-64::pulseaudio-client-17.0-h9a6aba3_3 
  pulseaudio-daemon  conda-forge/linux-64::pulseaudio-daemon-17.0-h33dcb6b_3 
  pycairo            conda-forge/linux-64::pycairo-1.29.1-py314hb1bbd57_1 
  pydub              conda-forge/noarch::pydub-0.25.1-pyhd8ed1ab_1 
  pyglet             conda-forge/noarch::pyglet-2.1.15-pyhd8ed1ab_0 
  pyglm              conda-forge/linux-64::pyglm-2.8.3-py314h5383ef5_3 
  pyproject_hooks    conda-forge/noarch::pyproject_hooks-1.2.0-pyhd8ed1ab_1 
  python-build       conda-forge/noarch::python-build-1.6.0-pyhc364b38_0 
  python-discovery   conda-forge/noarch::python-discovery-1.6.0-pyhcf101f3_0 
  python-installer   conda-forge/noarch::python-installer-1.0.1-pyh332efcf_0 
  rapidfuzz          conda-forge/linux-64::rapidfuzz-3.14.6-py314hc75f4c6_0 
  requests-toolbelt  conda-forge/noarch::requests-toolbelt-1.0.0-pyhd8ed1ab_1 
  screeninfo         conda-forge/linux-64::screeninfo-0.8.1-py314hdafbbf9_3 
  secretstorage      conda-forge/linux-64::secretstorage-3.5.0-py314hdafbbf9_1 
  shaderc            conda-forge/linux-64::shaderc-2025.5-h718be3e_1 
  shellingham        conda-forge/noarch::shellingham-1.5.4-pyhd8ed1ab_2 
  skia-pathops       conda-forge/linux-64::skia-pathops-0.9.2-py314h5383ef5_2 
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
  watchdog           conda-forge/linux-64::watchdog-6.0.0-py314h9e666f3_4 
  wayland-protocols  conda-forge/noarch::wayland-protocols-1.49-hd8ed1ab_0 
  xorg-libxi         conda-forge/linux-64::xorg-libxi-1.8.3-h7cc23a3_1 
  xorg-libxtst       conda-forge/linux-64::xorg-libxtst-1.2.5-h7cc23a3_4 
  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-hb9d3cd8_1004 
  zipp               conda-forge/noarch::zipp-4.1.0-pyhcf101f3_0 
  zstandard          conda-forge/linux-64::zstandard-0.25.0-py314hfe1a184_4 

The following packages will be UPDATED:

  fontconfig         pkgs/main::fontconfig-2.15.0-h2c49b7f~ --> conda-forge::fontconfig-2.18.3-h4db4eae_1 
  freetype            pkgs/main::freetype-2.14.1-hf5b9546_0 --> conda-forge::freetype-2.14.3-ha770c72_2 
  harfbuzz            pkgs/main::harfbuzz-12.3.0-h79d275a_1 --> conda-forge::harfbuzz-12.3.2-h6083320_0 
  icu                        pkgs/main::icu-73.1-h6a678d5_0 --> conda-forge::icu-78.3-py310h44b86e0_2 
  libhwloc           pkgs/main::libhwloc-2.12.1-default_hf~ --> conda-forge::libhwloc-2.12.1-default_hafda6a7_1003 
  libllvm22          pkgs/main::libllvm22-22.1.2-hfb1d434_0 --> conda-forge::libllvm22-22.1.8-hf7376ad_1 
  libpng                pkgs/main::libpng-1.6.56-h22898a0_0 --> conda-forge::libpng-1.6.58-h922cc85_1 
  libuuid              pkgs/main::libuuid-1.41.5-h5eee18b_0 --> conda-forge::libuuid-2.42.3-hcfc3c73_0 
  libxkbcommon                            1.11.0-he8b52b9_0 --> 1.13.2-h51789e4_1 
  libxml2              pkgs/main::libxml2-2.13.9-h2c43086_0 --> conda-forge::libxml2-2.14.6-he237659_3 
  libxslt                                 1.1.43-h7a3aeb2_0 --> 1.1.43-h711ed8c_1 
  lxml                                6.0.2-py314hd59e8af_0 --> 6.1.2-py314h78220e7_0 
  openssl                                  3.6.2-h35e630c_0 --> 3.6.4-h781a0a9_0 
  qtbase                                  6.11.0-h9201cad_0 --> 6.11.0-h68dfb5d_1 
  xorg-xorgproto     pkgs/main::xorg-xorgproto-2025.1-h47b~ --> conda-forge::xorg-xorgproto-2025.1-hebe6cf0_2 

The following packages will be SUPERSEDED by a higher-priority channel:

  python             pkgs/main::python-3.14.7-h2bd7c14_101~ --> conda-forge::python-3.14.0-h5989046_101_cp314 
  tk                         pkgs/main::tk-9.0.4-h3840b71_1 --> conda-forge::tk-8.6.13-noxft_h1df4ec4_4 
  xorg-libsm         pkgs/main::xorg-libsm-1.2.6-h984eb1c_1 --> conda-forge::xorg-libsm-1.2.6-h0d788c3_1 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done                                                                                                                                     
Verifying transaction: done                                                                                                                                     
Executing transaction: done                                                                                                                                     
WARNING conda.conda_pypi.main:notify_externally_managed_future(156):                                                                                            
  Did you know? You can install many PyPI packages with conda                                                                                                   
  using the conda-pypi beta. Get started:                                                                                                                       
    https://docs.conda.io/projects/conda/en/stable/new-features.html                                                                                            
                      
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ 
```