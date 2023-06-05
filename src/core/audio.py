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
import os 
import numpy as np

from settings import environment

WAV_FILE_WRITE = 'src/data/samples/output.wav'
WAV_FILE_READ = 'src/data/samples/ENDOFTHEYEAR_32-2.wav'
# WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_24.wav'
# WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_16.wav'

class AudioManager:
    
    def __init__(self):
        self.in_stream_file_paths = []
        self.out_stream_file_paths = []
        self.pya = pya.PyAudio()

        self.logger = logging.getLogger('AudioManager')
        self.logger.setLevel('DEBUG')

    def load_files(self):
        directory = os.getcwd() + environment.pathToWavData + '/'
        for file in os.listdir(directory):
            with open(environment.pathToWavData) as file:
                self.out_stream_file_paths.append(directory + file.name)

        
    def play_stream(stream:str):
        pass

    def audio_devices(self):
        result = []
        for i in range(self.pya.get_device_count()):
            result.append("id: \"" + str(self.pya.get_device_info_by_index(i).get('index')) + "\" " + \
                "name: \"" + str(self.pya.get_device_info_by_index(i).get('name')) + "\""
            )
        return result

    def update_active_output_device(self, deviceIndex):
        self.logger.info('beginning string ops for:' + deviceIndex)        
        logging.info('beginning string ops for:' + deviceIndex)  
        deviceIndex = int(deviceIndex[deviceIndex.find('"')+1:deviceIndex.find('"')+2])
        self.logger.info('updating ' + str(environment['outputDeviceIndex']) + ' to:' + str(deviceIndex))        
        environment['outputDeviceIndex'] = deviceIndex

    def update_active_input_device(self, deviceIndex):
        pass

    def record():
        pass

class AudioOutputStream:
    
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
        self.filePath = None

        self.logger = logging.getLogger(__name__)
        
    def setup(self, filePath):
        self.filePath = filePath
        self.pedalFile = AudioFile(filePath)
        self.channels = self.pedalFile.num_channels
        self.sample_rate = self.pedalFile.samplerate
        self.chunk_size = 1024
        
        match self.pedalFile.file_dtype:
            case float32: 
                self.sample_width = pya.paFloat32
        

        logging.info('channels:' + str(self.channels))
        logging.info('sample_rate:' + str(self.sample_rate))
        logging.info('sample width:' + str(self.sample_width))

    def play(self):
        # logging.info(self.__dict__)
        def open():
            try:
                self.stream = self.pya.open(
                        format=self.sample_width, 
                        channels=1, #self.pedalFile.num_channels -- don't really know why, but fixes whitenoise issue when played in mono
                        rate=int(self.pedalFile.samplerate), 
                        output=True,
                        # input_device_index=environment['outputDeviceIndex'], 
                        output_device_index=environment['outputDeviceIndex'],
                        stream_callback=self.__callback
                )
            except Exception as e:
                self.logger.fatal('failed to open device:' + str(environment['outputDeviceIndex']))
            return self.stream
        
        if self.pya:
            open()
        else:
            self.pya = pya.PyAudio()
            self.setup(self.filePath)
            open()
        
        # self.stream.start_stream()
        return self.stream

    def __callback(self, in_data, frame_count, time_info, status):

        try:
            # data = in_data #in_data used for recording
            data = self.pedalFile.read(frame_count)
            board = Pedalboard([x for x in self.effect_chain])
            data = board(np.array(data), self.sample_rate, reset=False)
        except Exception as e:
            self.logger.error(e)

        return (data, pya.paContinue)
    
    def stop(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            if self.pya is not None:
                self.pya.terminate()
                self.pya = None
            if self.pedalFile is not None:
                self.pedalFile.close()

    def __del__(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close(self.stream)
            self.pya.terminate()
            self.pya = None
            self.pedalFile.close()

    def __str__(self):
        return str(self.__dict__)
    
class AudioInputStream:
    
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
        self.filePath = None

        self.logger = logging.getLogger(__name__)
        
    def setup(self, filePath):
        self.filePath = filePath
        self.pedalFile = AudioFile(filePath)
        self.channels = self.pedalFile.num_channels
        self.sample_rate = self.pedalFile.samplerate
        self.chunk_size = 1024
        
        match self.pedalFile.file_dtype:
            case float32: 
                self.sample_width = pya.paFloat32
        

        self.logger.info('channels:' + str(self.channels))
        self.logger.info('sample_rate:' + str(self.sample_rate))
        self.logger.info('sample width:' + str(self.sample_width))

    def record(self):
        # logging.info(self.__dict__)
        def open():
            try:
                self.stream = self.pya.open(
                        format=self.sample_width, 
                        channels=1, #self.pedalFile.num_channels -- don't really know why, but fixes whitenoise issue when played in mono
                        rate=int(self.pedalFile.samplerate), 
                        input=True,
                        input_device_index=environment['inputDeviceIndex'], 
                        # output_device_index=environment['outputDeviceIndex'],
                        stream_callback=self.__input_callback
                )
            except Exception as e:
                self.logger.fatal('failed to open device:' + str(environment['outputDeviceIndex']))
            return self.stream
        
        if self.pya:
            open()
        else:
            self.pya = pya.PyAudio()
            self.setup(self.filePath)
            open()
        
        # self.stream.start_stream()
        return self.stream
    
    def __input_callback(self, in_data, frame_count, time_info, status):

        try:
            data = in_data #in_data used for recording
            board = Pedalboard([x for x in self.effect_chain])
            data = board(np.array(data), self.sample_rate, reset=False)
        except Exception as e:
            self.logger.error(e)

        return (data, pya.paContinue)
    
    def stop(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
            self.pya.terminate()
            self.pya = None
            self.pedalFile.close()

    def __del__(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close(self.stream)
            self.pya.terminate()
            self.pya = None
            self.pedalFile.close()

    def __str__(self):
        return str(self.__dict__)