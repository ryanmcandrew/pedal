import os
import sys
import streamlit
import matplotlib as mpl
import librosa
import librosa.display
# from librosa import display


chunk = 1024

SAMPLE_DIR = '/data/'

# had errors related to subject "overflow error" in 
# matplotlib found below but did not work

# increase limit in number of data points in matplotlib
# mpl.rcParams['agg.path.chunksize'] = 500000000

class AudioStruct:
    def __init__(self, name, sample):
        self.name = name
        self.sample = sample

def main():
    
    # scan through samples and load each one.
    fileList = []
    for filestr in os.listdir(os.getcwd() + SAMPLE_DIR):
        with open(os.path.join(os.getcwd() + SAMPLE_DIR + filestr), 'rb') as data:

            fileListItem = AudioStruct(filestr, data.read())
            fileList.append(fileListItem)

    #plot each file using data collected previously
    for i in fileList:
        fig, ax = mpl.pyplot.subplots(1, 1)
        mpl.pyplot.ylabel('Amplitude')
        mpl.pyplot.title(i.name)
        
        filename = os.getcwd() + SAMPLE_DIR + i.name
        
        y, samplingRate = librosa.load(filename, sr=22050)
        # librosa.display.waveplot(y, sr, ax=ax, x_axis='time')
        librosa.display.waveshow(y, sr=samplingRate, ax=ax, x_axis='time') #deprecated
        
        streamlit.pyplot(fig)
        streamlit.audio(i.sample, format='audio/wav')

main()