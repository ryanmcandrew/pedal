from pedalboard import Pedalboard, Chorus, Reverb, Delay
from pedalboard.io import AudioFile

import pyaudio
import wave
import sys
import os 
import time
from kivy.core.audio import SoundLoader
import numpy as np

import multiprocessing
import threading

# from app import delay_widget
import lib.widgets.chorus
import lib.widgets.reverb
import lib.widgets.delay
import lib.widgets.toolbar

from app import delay_widget

WAV_FILE_WRITE = 'app/data/output.wav'
WAV_FILE_READ = 'app/data/ENDOFTHEYEAR_32-2.wav'
OUTPUT_DEVICE_INDEX= 9
BUFFER_FRAME_SIZE = int(1024 ) #controls rate of playback

def callback(in_data, frame_count, time_info, status):
    global chorus
    # global delay
    global delay_widget
    global reverb
    global board

    try:
        data = file.read(int(frame_count *2))
        # data = in_data #causes pedalboard to yell about 32bit and 64bit
        board = Pedalboard([chorus, delay_widget.delay_obj, reverb])
        # data = file.read(int(BUFFER_FRAME_SIZE ))
        data = board(np.array(data), 44100, reset=False)
    except Exception as e:
        print('Exception caught:')
        print(e)

    return (data, pyaudio.paContinue)
    
def write_effects_out():

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

def play_wav_thread():
    global stream
    global p
    # global audio_process
    global file
    global OUTPUT_DEVICE_INDEX
    # global sound
         # global sound
    # if sound:
        # print("Sound found at %s" % sound.source)
        # print("Sound is %.3f seconds" % sound.length)
        
        # sound.play()
    # p = pyaudio.PyAudio()
    # print ('master thread:')
    # print(os.getpid())
    # audio_process.daemon = True
    # audio_process.start()   
    print("using device: ", str(OUTPUT_DEVICE_INDEX))
    if not stream:
        stream = p.open(format=p.get_format_from_width(4), channels=2, rate=int(file.samplerate), \
            output=True, input_device_index=OUTPUT_DEVICE_INDEX, stream_callback=callback)

def play_wav():
    global audio_process
    audio_process = threading.Thread(target=play_wav_thread, args=())
    audio_process.start()
       
def stop_wav():
    # global sound
    # global audio_process
    # if sound:
        # sound.stop()
    # audio_process.terminate()
    # audio_process.kill()
    global stream
    global p
    global file
    if stream:
        print('closing stream')
        stream.stop_stream()
        stream.close()
        # p.close()
        p.terminate()
        file = AudioFile(WAV_FILE_READ)
        p = pyaudio.PyAudio()
        stream = None

def seek_wav(value):
    global sound
    if sound:
        sound.seek(value)

def reload_wav():
    global sound
    # if not sound:
        # sound = SoundLoader.load('client/' + WAV_FILE)
    # if sound:
        # sound.stop()
        # sound.unload()
    # stop_wav()
    # test_one()
    # play_wav()
    # sound = SoundLoader.load(WAV_FILE_WRITE)

def audio_devices():
    global p
    result = []
    for i in range(p.get_device_count()):
        result.append("id: \"" + str(p.get_device_info_by_index(i).get('index')) + "\" " + \
            "name: \"" + str(p.get_device_info_by_index(i).get('name')) + "\""
        )
        # result.append(str(pa.get_device_info_by_index(i)))
    return result

def update_active_audio_device(value):
    global OUTPUT_DEVICE_INDEX
    
    value = str(value)
    value = value[value.find('\"'):value.find('name: ')]
    value = value.replace('\"', '')

    OUTPUT_DEVICE_INDEX = int(value)

def update_chorus(rate, depth, delay, feedback, mix):
    global chorus
    # chorus = Chorus(
        # rate_hz=rate,
        # depth=depth,
        # centre_delay_ms=delay,
        # feedback=feedback,
        # mix=mix
    # )
    
    chorus.rate_hz = rate
    chorus.depth = depth
    chorus.centre_delay_ms = delay
    chorus.feedback = feedback 
    chorus.mix = mix

    # board = Pedalboard([chorus])
    print('chorus updated with ' + 'rate: ' + str(rate) + " depth: " + str(depth) + "centre_delay_ms: " + str(delay) + "feedback" + str(feedback) + "mix" + str(mix))

def update_reverb(room_size, damping, wet_level, dry_level, width, freeze_mode):
    global reverb
    # reverb = Reverb(
        # room_size = room_size, 
        # damping = damping, 
        # wet_level = wet_level, 
        # dry_level = dry_level, 
        # width = width, 
        # freeze_mode = freeze_mode
    # )

    reverb.room_size = room_size
    reverb.damping = damping
    reverb.wet_level = wet_level
    reverb.dry_level = dry_level
    reverb.width = width
    reverb.freeze_mode = freeze_mode

    # board = Pedalboard([reverb])
    print('reverb updated with ' + 'room_size: ' + str(room_size) + " damping: " + str(damping) + " wet_level: " + \
        str(wet_level) + " dry_level: " + str(dry_level) + ' width: ' + str(width) + " freeze_mode: " + str(freeze_mode))

def update_delay(delay_seconds, feedback, mix):
    global delay
    
    # delay = Delay(
    #     delay_seconds = delay_seconds, 
    #     feedback = feedback, 
    #     mix = mix
    # )
    delay.delay_seconds = delay_seconds
    delay.feedback = feedback
    delay.mix = mix
    # board = Pedalboard([delay])
    print('delay updated with ' + 'delay_seconds: ' + str(delay_seconds) + " feedback: " + str(feedback) + " mix: " + str(mix))

sound = SoundLoader.load(WAV_FILE_READ)
file = AudioFile(WAV_FILE_READ)
p = pyaudio.PyAudio()
stream = None
chorus = Chorus()
# chorus_widget = ChorusWidget()
reverb = Reverb()

board = Pedalboard([])
# audio_process = multiprocessing.Process(target=play_wav_thread, args=())
audio_process = None

# write_effects_out()