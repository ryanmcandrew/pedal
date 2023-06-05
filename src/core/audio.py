import threading
import multiprocessing
import logging

from pedalboard import Pedalboard, Chorus, Reverb, Delay, Bitcrush
from pedalboard import Compressor, Convolution, Gain, HighpassFilter, HighShelfFilter, Distortion, IIRFilter
from pedalboard import Invert, Limiter, LowpassFilter, LadderFilter, LowShelfFilter, MP3Compressor, NoiseGate, PeakFilter
from pedalboard import Resample, Reverb
from pedalboard import VST3Plugin
from pedalboard.io import AudioFile
import pedalboard.version as pedalv

import pyaudio as pya
import wave
import sys
import os 
import time
from kivy.core.audio import SoundLoader
import numpy as np

WAV_FILE_WRITE = 'src/data/output.wav'
WAV_FILE_READ = 'src/data/ENDOFTHEYEAR_32-2.wav'
# WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_24.wav'
# WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_16.wav'
OUTPUT_DEVICE_INDEX= 9
BUFFER_FRAME_SIZE = int(1024 ) #controls rate of playback

class AudioManager():
    
    def __init__(self):
        self.in_streams = []
        self.out_streams = []
        self.pya = pya.PyAudio()
        
    def play_stream(stream:str):
        pass

class AudioStream():
    
    def __init__(self):
        self.id = 0
        self.input_device_index = 0 #the os managed device id of the speaker playing the audio
        self.bpm = 70
        self.midiOut = None
        self.effect_chain = []
        self.file = None
        self.sample_width = 0
        self.sample_rate = 0
        self.chunk_size = 0
        self.stream = None
        self.pya = pya.PyAudio()
        
    def setup(self, filePath):
        # self.file = wave.open(filePath, 'rb')
        self.pedalFile = AudioFile(filePath)
        # self.channels = self.file.getnchannels()
        self.channels = self.pedalFile.num_channels
        # self.sample_rate = self.file.getframerate()
        self.sample_rate = self.pedalFile.samplerate
        
        match self.pedalFile.file_dtype:
            case float32: 
                self.sample_width = pya.paFloat32
        
        self.chunk_size = 1024

        logging.info('channels:' + str(self.channels))
        logging.info('sample_rate:' + str(self.sample_rate))
        logging.info('sample width:' + str(self.sample_width))

    def play(self):
        # logging.info(self.__dict__)
        self.stream = self.pya.open(
                format=self.sample_width, 
                channels=1, #self.pedalFile.num_channels -- don't really know why, but fixes whitenoise issue when played in mono
                rate=int(self.pedalFile.samplerate), 
                output=True,
                input_device_index=OUTPUT_DEVICE_INDEX, 
                stream_callback=self.__callback
        )
        # self.stream.start_stream()
        return self.stream

    def __callback(self, in_data, frame_count, time_info, status):

        try:
            data = in_data #in_data used for recording
            data = self.pedalFile.read(frame_count)
            board = Pedalboard([x for x in self.effect_chain])
            data = board(np.array(data), self.sample_rate, reset=False)
        except Exception as e:
            logging.info(e)

        return (data, pya.paContinue)
    
    def stop(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()

    def __del__(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()

    def __str__(self):
        return str(self.__dict__)