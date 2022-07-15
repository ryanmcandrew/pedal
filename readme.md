# Details

contains pyaudio/matplotlib/pedalboard experiments - trying to make sense of something by mashing more mashings together..

- draw tests: draw a wav with streamlit/matplotlib/librosa
  - requires a streamlit launch currently
- open tests: attempt opening audio input and recording
  - requires python interpretter

# References

[pyaudio](https://people.csail.mit.edu/hubert/pyaudio/docs/)

# so far

- played a file
- recorded a file
  - recording did not completely work. audio recorded was nearly inaudible. determining device id undetermined.
- plot wav from file

# to do

now:
- f
- refactor
- display wav outside streamlit and remove streamlit
- refactor
- find solution to picking audio input
- find solution to playing back a recording that is in progress
- find solution to drawing a recording in progress
- refactor

goals:
- plot wav from active input
- feed input through the pedalboard package with modular design to account for varying effects in the signal chain
- frame some basic controls in a window from some gui lib for:
  - playback
  - volume
  - effect chain with minimal controls mapped to effect class attributes

# Program execution

- python3
- install depends by requirements.txt in conda environment
- from app root, pass app.py to python interpretter `streamlit run app.py`

# Run tests
No official unit tests just played around with matplotlib, opening and recording audio files
- from app root, `python app.py` currently just runs the test functions in tests/open_tests.py and tests/draw_tests.py. For draw tests streamlit is currently required. Streamlit test functions and imports must be commented out when running nonstreamlit tests. The methods perform wav drawing, and recording, and audio device id lookups through pyaudio streamlit and matplotlib.

git commit -m "updated structure, filled out a readme, merged a related playground codebase to here"