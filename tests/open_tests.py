import pedalboard
import pyaudio
import wave
import sys
import os
import time

#Test functions that read available audio inputs,
# and attempt to record from the inputs (1, 2, 3, 4)
WAVE_OUTPUT_FILENAME = "./data/audio_file.wav"

def run():
    # test_configs()
    # test_one()
    # test_two()
    # test_three()
    test_four()

def test_configs():
    pa = pyaudio.PyAudio()

    for i in range(pa.get_device_count()):
        print(pa.get_device_info_by_index(i))
    
    # for id in range(pa.get_host_api_count()):
    #     print(pa.get_host_api_info_by_index(id))
    #     print('----------------------------')
    # print(pa.get_default_host_api_info())
    # print('----------------------------')
    # print(pa.get_default_input_device_info())
    # print(pa.get)
    # print('----------------------------')
    # print(pa.get_default_output_device_info())
    # print('----------------------------')

def test_one():
    print('instantiating pyaudio')
    
    CHUNK = 1024

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    print('Opening file:' + sys.argv[1])
    wf = wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()
    # pedalboard

def test_two():
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    # input_device_index=2,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()
    pass

def test_three():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=2,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    out_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    out_file.setnchannels(2)        # number of channels
    out_file.setsampwidth(2)        # sample width in bytes
    out_file.setframerate(44100)    # sampling rate in Hz
    out_file.writeframes(frames)
    # for i in frames:
        # out_file.write(i)

    out_file.close()

    stream.stop_stream()
    stream.close()
    p.terminate()

def test_four():

    print('recording')
    RATE = 44100 #48000
    pa = pyaudio.PyAudio()
    stream_in = pa.open(
        rate=RATE,
        channels=2,
        format=pyaudio.paInt16,
        input=True,                   # input stream flag
        input_device_index=14,         # input device index
        frames_per_buffer=1024
    )

    # read 5 seconds of the input stream
    buffer = stream_in.read(5 * RATE)

    wav_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

    # define audio stream properties
    wav_file.setnchannels(2)        # number of channels
    wav_file.setsampwidth(2)        # sample width in bytes
    wav_file.setframerate(RATE)    # sampling rate in Hz

    # write samples to the file
    wav_file.writeframes(buffer)

    wav_file.close()
    pa.terminate()

    pya = pyaudio.PyAudio()

    print('playing')

    # Open the sound file 
    wf = wave.open('audio-recording.wav', 'rb')

        # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream_out = pya.open(format = pya.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True,
                    output_device_index=15)

    # Read data in chunks
    data = wf.readframes(1024)

    # Play the sound by writing the audio data to the stream
    while data != b'':
        # print(data)
        stream_out.write(data)
        data = wf.readframes(1024)

    # Close and terminate the stream
    stream_out.close()
    pya.terminate()