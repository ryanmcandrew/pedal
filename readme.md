# Details

This software contains a simple kivy application with an intention to reveal a few aspects of the spotify pedalboard interface on a gui. Currently contains a "functioning" kivy application with the ability to play back a hard-coded wav recording and add effects from the spotify pedalboard package. Implemented audio streaming to provide a callback when playing chunks that can modify the stream by sending it through the spotify pedalboard effects modules. Attributes of the effects modules are mapped to kivy slider componenets. Mostly experimental, bad, spaghetti code and a basic framework for kivy atm.

Nothing is tested in mac/windows. 99% chance will not work. Although, both kivy and pyAudio claim to be highly portable.

# To do

- fix bugs / refactor into a reasonable pipeline
- draw wavform on window
- record audio
- open mic and hear playback
- make window layout look like designs
- export / render effected wavform to a file

# Bugs

- 001 - audio chops up when moving controls and the window
  - I believe the GIL is screwing me for this. Might need to base the root app in C++, though possibly can run separate processes and implement messaging from the kivy gui to command audio controls. Only tried threading the audio playback, could try threading the kvApp.run() routine in addition to audio. Proper pipeline would likely help.
- 003 - streamed 32bit wav file is sped up by doubling the framerate to cover up a bug that causes normal frame rate to sound bit crushed on playback
- 004 - audio device ID no longer hard coded, but changing the device ID after the first play of audio will not change the device used due to null check in play_wav_thread()
- 005 - tried to fill out delay widget class with more attributes for the pedalboard effects. on_move_update isn't properly updating the delay module despite mapping the pedalboard.Delay attribute seemingly correctly to corresponding gui control attributes of the widget.

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
- source /path/to/venv/pedal/bin/activate
- cd /path/to/app 
- pip install -r requirements.txt
- python app/app.py

# Run tests
No official unit tests yet. 

- Past notes:
  - just played around with matplotlib, opening and recording audio files
  - test functions in tests/open_tests.py and tests/draw_tests.py. The methods perform wav drawing, and recording, and audio device id lookups through pyaudio streamlit and matplotlib.
