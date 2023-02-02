# Details

contains pyaudio/matplotlib/pedalboard experiments - trying to make sense of something by mashing more mashings together..

# References

Documentation for open source modules
- [kivy](https://kivy.org/doc/stable/)
- [pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)

- [pyside gui](https://pypi.org/project/PySide/#introduction)

- [pedalboard](https://spotify.github.io/pedalboard/)

- [python-sounddevice](https://readthedocs.org/projects/python-sounddevice/downloads/pdf/latest/)

Similar open source examples

- [stefanobazzi/guitarboard](https://github.com/stefanobazzi/guitarboard)

Helpful articles

- [realtime wave project](https://medium.com/geekculture/real-time-audio-wave-visualization-in-python-b1c5b96e2d39)
- [by domonic feeney](https://morioh.com/p/848d9c9a22b1)

# Dependencies

- See requirements.txt
- May need to install apt packages - ffpyplayer


# Program execution

- python -m venv pedal
- source /path/to/venv/pedal/bin/activate
- pip install -r requirements.txt
- python app/app.py

# Run tests
No official unit tests yet. 

- Past notes:
  - just played around with matplotlib, opening and recording audio files
  - from app root, `python app.py` currently just runs the test functions in tests/open_tests.py and tests/draw_tests.py. For draw tests streamlit is currently required. Streamlit test functions and imports must be commented out when running nonstreamlit tests. The methods perform wav drawing, and recording, and audio device id lookups through pyaudio streamlit and matplotlib.
