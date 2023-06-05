# Details

This software contains a simple kivy application with an intention to reveal a few aspects of the spotify pedalboard interface on a gui. Has functions to play back a hard-coded wav recording and add effects from the spotify pedalboard package. Implemented audio streaming with a callback when playing chunks that can modify the stream by sending it through the spotify pedalboard effects modules. Attributes of the effects modules are mapped to kivy slider componenets.

Nothing is tested in mac/windows. 68% chance will not work. Although, both kivy and pyAudio claim to be highly portable. requires python 10

# To do

- record audio
- open mic and hear playback
- add effects scrollview
- add audio channels
- map effects to channels
- add audio channel scrollview
- add channel arm
- add play arrangement from different channels
- make window layout look like designs
- export / render effected wavform to a file

# Bugs

- 001 - audio chops up when moving the window and using scroll wheel on menus/navigating menus
  - I believe the GIL is biting  me for this. Might need to base the root app in C++, though possibly can run separate processes and implement messaging from the kivy gui to command audio controls. Only tried threading the audio playback


# References

Documentation for open source modules
- [kivy](https://kivy.org/doc/stable/)
- [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)

- [pyside gui](https://pypi.org/project/PySide/#introduction)

- [pedalboard](https://spotify.github.io/pedalboard/)

- [python-sounddevice](https://readthedocs.org/projects/python-sounddevice/downloads/pdf/latest/)

- [scipy.io.wavfile](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html)

- [python-for-android](https://python-for-android.readthedocs.io/en/latest/quickstart/)

- [dsp guide](http://www.dspguide.com/pdfbook.htm)

- [making audio plugins](https://www.martin-finke.de/tags/making_audio_plugins.html)

Similar open source examples

- [stefanobazzi/guitarboard](https://github.com/stefanobazzi/guitarboard)

Helpful articles

- [realtime wave project](https://medium.com/geekculture/real-time-audio-wave-visualization-in-python-b1c5b96e2d39)
- [scipy suggestion](https://nateharada.com/wave-files-python/)
- [by domonic feeney](https://morioh.com/p/848d9c9a22b1)

# Dependencies

- See requirements.txt
- May need to install system packages (apt/homebrew/yum/choco/..etc) to support pip modules. such as, ffpyplayer
- may need to fiddle with ALSA/pulseaudio
- still untested on a fresh system - likely more problems.

# Program execution

- python -m venv ~/.venv/pedal
- source ~/.venv/pedal/bin/activate
  - windows: ~/.venv/pedal/bin/Activate.ps1 or ~/.venv/pedal/bin/Activate
- cd /path/to/app
- pip install -r requirements.txt
- python src/main.py

# Run tests
No official unit tests yet. 

# GUI Sample Screenshot

![Screenshot of app](docs/Screenshot%20from%202023-06-05%2002-32-44.png)
