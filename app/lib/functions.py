from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile
# from client.chorus import app_abs
# import client.chorus
# from ..chorus import app_abs
# from kivy.core.audio import 

import pyaudio
import wave
import sys

import time
from kivy.core.audio import SoundLoader
import numpy as np

chorus = Chorus()
pa = pyaudio.PyAudio()
# board = Pedalboard([chorus, Reverb(room_size=0.25)])
board = Pedalboard([chorus])

WAV_FILE_WRITE = 'app/data/output.wav'
WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_32-2.wav'
OUTPUT_DEVICE_INDEX= 9
BUFFER_FRAME_SIZE = int(1024 / 2) #controls rate of playback
sound = SoundLoader.load(WAV_FILE_READ)
# stream = 

p = pyaudio.PyAudio()

    # define callback (2)
def callback(in_data, frame_count, time_info, status):
    with AudioFile(WAV_FILE_READ) as f:
        # data = wf.readframes(frame_count)
        # data = f.readframes(frame_count)
        data = f.read(frame_count)
        # data = f.read(int(f.samplerate * 10))
        
    # with AudioFile(WAV_FILE_READ) as f:
    # with ReadableAudioFile(WAV_FILE_READ) as f:
        data = board(np.array(data, dtype=float), f.samplerate, reset=False)
        # effected = board(data, p.get_format_from_width(wf.getsampwidth()), reset=False)
        # print('--------------------------------------------------------------------------------------------------')
        # print(f.samplerate)
        # print(wf.getsampwidth())
        # print(f.bit_depth)
    return (data, pyaudio.paContinue)

# # # open stream using callback (3)
# with AudioFile(WAV_FILE_READ) as f:
#     print('--------------------------------------------------------------------------------------------------')
#     print(f)
#     # print(p.__format__)
#     print('--------------------------------------------------------------------------------------------------')
#     stream = p.open(format=p.get_format_from_width(2), channels=f.num_channels, rate=44100, \
#         output=True, input_device_index=OUTPUT_DEVICE_INDEX, stream_callback=callback)

def test_one():

    # wf = wave.open('client/' + WAV_FILE_READ, 'rb')
    # stream_out = pa.open(format = pa.get_format_from_width(wf.getsampwidth()),
    #                 channels = wf.getnchannels(),
    #                 # channels = pa.get_device_info_by_index(OUTPUT_DEVICE_INDEX).get('maxInputChannels'),
    #                 rate = wf.getframerate(),
    #                 outputBoxLayout:

    with AudioFile( WAV_FILE_READ) as f:

        # Open an audio file to write to:
        with AudioFile(WAV_FILE_WRITE, 'w', f.samplerate, f.num_channels) as o:

            # Read one second of audio at a time, until the file is empty:
            while f.tell() < f.frames:
                chunk = f.read(int(f.samplerate))

                # Run the audio through our pedalboard:
                effected = board(chunk, f.samplerate, reset=False)

                # Write the output to our output file:
                o.write(effected)
                # stream_out.
                # stream_out.write(effected)

    # stop stream (4)
    # stream_out.stop_stream()
    # stream_out.close()

def play_wav():
    # sound = SoundLoader.load(WAV_FILE)
    # wave.open()
    # wf = wave.open(WAV_FILE_READ, 'rb')
    # print('--------------------------------------------------------------------------------------------------')
    # with AudioFile( WAV_FILE_READ) as f:
    #     print(f.samplerate)
    #         # print(wf.getsampwidth())
    #     print(f.bitdepth)

    # with AudioFile( WAV_FILE_READ) as f:
        
    #     print("sample RATE:" + str(int(f.samplerate)))

    

    # instantiate PyAudio (1)
    

                        # format=pyaudio.paFloat32,
                        # format=pyaudio.paInt32,
                    # format=p.get_format_from_width(wf.getsampwidth(),
                    # channels=wf.getnchannels(),
                    # rate=wf.getframerate(),

    # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
    #                 channels=wf.getnchannels(),
    #                 rate=wf.getframerate(),
    #                 output=True,
    #                 input_device_index=OUTPUT_DEVICE_INDEX,
    #                 stream_callback=callback)

    # start the stream (4)
    # stream.start_stream()
    # stream.

    # wait for stream to finish (5)
    # while stream.is_active():
    #     time.sleep(0.1)

    global sound
    if sound:
        print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        
        sound.play()
    # test_one()

def stop_wav():
    global sound
    if sound:
        sound.stop()

    # stream.stop_stream()
    # stream.close()
    # p.terminate()

def seek_wav(value):
    global sound
    if sound:
        sound.seek(value)

def reload_wav():
    global sound
    # if not sound:
        # sound = SoundLoader.load('client/' + WAV_FILE)
    if sound:
        sound.stop()
        sound.unload()
    test_one()
    sound = SoundLoader.load(WAV_FILE_WRITE)

def audio_devices():
    result = []
    for i in range(pa.get_device_count()):
        result.append(str(pa.get_device_info_by_index(i).get('name') + " - " + \
            str(pa.get_device_info_by_index(i).get('index')) + "-" + \
            str(pa.get_device_info_by_index(i).get('maxOutputChannels')) + "-" + \
            str(pa.get_device_info_by_index(i).get('maxInputChannels')) + "-" \
        ))
        # result.append(str(pa.get_device_info_by_index(i)))
    return result

def update_active_audio_device(self, value):
    OUTPUT_DEVICE_INDEX = value

def update_chorus(rate, depth, delay, feedback, mix):
    global board
    chorus = Chorus(
        rate_hz=rate,
        depth=depth,
        centre_delay_ms=delay,
        feedback=feedback,
        mix=mix
    )
    board = Pedalboard([chorus, Reverb(room_size=0.25)])