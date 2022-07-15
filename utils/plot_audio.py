import pyaudio
import struct
import matplotlib.pyplot as plt
import numpy as np
import wave

plt.title('Test')
x = [0, 1, 2]
y = [2, 1, 0]
plt.plot(x, y)
plt.show()

# CHUNK = 1024
# RATE = 44100

# pa = pyaudio.PyAudio()
# stream_in = pa.open(
#     rate=44100,
#     channels=2,
#     format=pyaudio.paInt16,
#     input=True,                   # input stream flag
#     # input_device_index=10,         # input device index
#     frames_per_buffer=CHUNK
# )

# for i in range(pa.get_device_count()):
#     print(pa.get_device_info_by_index(i))

#  # read 5 seconds of the input stream
# buffer = stream_in.read(5 * 44100)

# output_filename = 'audio-recording.wav'
# wav_file = wave.open(output_filename, 'wb')

# # define audio stream properties
# wav_file.setnchannels(2)        # number of channels
# wav_file.setsampwidth(2)        # sample width in bytes
# wav_file.setframerate(44100)    # sampling rate in Hz

# # write samples to the file
# wav_file.writeframes(buffer)
# plt.title('Something')
# fig, ax = plt.subplots(figsize=(14,6))
# x = np.arange(0, 2 * CHUNK, 2)
# ax.set_ylim(-200, 200)
# ax.set_xlim(0, CHUNK) #make sure our x axis matched our chunk size
# line, = ax.plot(x, np.random.rand(CHUNK))

# while True:
#     data = stream_in.read(CHUNK)
#     data = np.frombuffer(data, np.int16)
#     line.set_ydata(data)
#     fig.canvas.draw()
#     fig.canvas.flush_events()
#     plt.pause(0.01)