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

# Conda `ds314` environment update @mint-22 on 20260905

## Context
Direct reason was that we would like to install The **Manim** Community Edition on the environment

## Steps for general updates of the `base` and the `ds314` environments
1. `(base) $ conda update -n base -c defaults conda --repodata-fn=repodata.json`
2. `(base) $ conda update -n base --all`
3. `(base) $ conda activate ds314`
4. `(ds314) $ python --version` (reveals `Python 3.14.4`)
5. `(ds314) $ conda update -n ds314 --all --no-pin`
6. `(ds314) $ python --version` (reveals `Python 3.14.7`)

## Adding `Manim CE`
- [https://docs.manim.community/en/stable/installation/conda.html](https://docs.manim.community/en/stable/installation/conda.html)
- `(ds314) $ conda install -c conda-forge manim`
- `(ds314) $ conda activate ds314`

## Testing the installation
```bash
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark$ cd src/manim_test/
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.20.1

╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/cli/render/commands.py:125  │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:259 in       │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:1194 in play │
│                                                                                                  │
│   1191 │   │   │   return                                                                        │
│   1192 │   │                                                                                     │
│   1193 │   │   start_time = self.time                                                            │
│ ❱ 1194 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1195 │   │   run_time = self.time - start_time                                                 │
│   1196 │   │   if subcaption:                                                                    │
│   1197 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/renderer/cairo_renderer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
```
Dit is een bekend probleem dat specifiek optreedt wanneer Manim wordt geïnstalleerd via Conda (vaak in combinatie met 
een erg nieuwe Python-versie zoals Python 3.14).

De foutmelding UnknownCodecError: libx264 betekent dat de Python-bibliotheek PyAV (gebruikt om video's te schrijven) de
H.264 video codec niet kan vinden. Conda heeft de ffmpeg-bibliotheken wel geïnstalleerd, maar de koppeling naar de 
x264-encoder mist.

Je kunt dit probleem snel oplossen door de codecs binnen je Conda-omgeving handmatig te herstellen of aan te vullen.

### De Oplossing
Voer de volgende commando's uit in je terminal (zorg dat je omgeving ds314 actief is):
```bash
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -c conda-forge x264
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - x264


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    x264-1!164.3095            |       h166bdaf_2         877 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         877 KB

The following NEW packages will be INSTALLED:

  x264               conda-forge/linux-64::x264-1!164.3095-h166bdaf_2 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                                                
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -c conda-forge ffmpeg pyav --force-reinstall
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundInChannelsError: The following packages are not available from current channels:

  - pyav

Current channels:

  - https://conda.anaconda.org/conda-forge
  - https://repo.anaconda.com/pkgs/main
  - https://repo.anaconda.com/pkgs/r

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.


(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.20.1

╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/cli/render/commands.py:125  │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:259 in       │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:1194 in play │
│                                                                                                  │
│   1191 │   │   │   return                                                                        │
│   1192 │   │                                                                                     │
│   1193 │   │   start_time = self.time                                                            │
│ ❱ 1194 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1195 │   │   run_time = self.time - start_time                                                 │
│   1196 │   │   if subcaption:                                                                    │
│   1197 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/renderer/cairo_renderer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
```
De reden dat Conda de bibliotheek niet kan vinden, is een kleine naamswijziging in de repositories. In de Python-wereld heet de library pyav, maar in de Conda-forge kanalen is het pakket opgeslagen onder de naam av.

Als we in je meegestuurde pakketlijst kijken, zien we hem daar inderdaad ook tussen staan: av | 16.1.0 | doc | dev | BSD-3-Clause.

Laten we het commando aanpassen met de juiste naam om de x264-codec werkend te krijgen.

```bash
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda install -c conda-forge ffmpeg av --force-reinstall
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/willem/anaconda3/envs/ds314

  added / updated specs:
    - av
    - ffmpeg



Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda activate ds314
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ manim -pql main.py CreateCircle
Manim Community v0.20.1

╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/cli/render/commands.py:125  │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:259 in       │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene.py:1194 in play │
│                                                                                                  │
│   1191 │   │   │   return                                                                        │
│   1192 │   │                                                                                     │
│   1193 │   │   start_time = self.time                                                            │
│ ❱ 1194 │   │   self.renderer.play(self, *args, **kwargs)                                         │
│   1195 │   │   run_time = self.time - start_time                                                 │
│   1196 │   │   if subcaption:                                                                    │
│   1197 │   │   │   if subcaption_duration is None:                                               │
│                                                                                                  │
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/renderer/cairo_renderer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
│ /home/willem/anaconda3/envs/ds314/lib/python3.14/site-packages/manim/scene/scene_file_writer.py: │
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
(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ conda update -c conda-forge av manim
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

# All requested packages already installed.

(ds314) willem@mint-22:~/git/DataAnalysisWithPythonAndPySpark/src/manim_test$ 
```

Dit probleem wordt veroorzaat door een compatibiliteitsprobleem tussen de bibliotheek PyAV (de av module) en Python 3.14.

De traceback breekt af in de C-extensie van PyAV (av.codec.codec.Codec._init), wat er meestal op wijst dat de 
geïnstalleerde versie van PyAV niet volledig is gecompileerd voor of compatibel is met de interne wijzigingen (de C-API)
van Python 3.14. Aangezien Python 3.14 momenteel een gloednieuwe/experimentele versie is, lopen veel binaire pakketten 
(zoals die in Anaconda of PyPI) hier nog tegenaan.