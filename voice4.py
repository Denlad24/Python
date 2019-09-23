import pyaudio
import wave
from array import array
import time

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 15
FILE_NAME = "RECORDING.wav"

audio = pyaudio.PyAudio()  # instantiate the pyaudio

# recording prerequisites
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# starting recording
frames = []
timer = 0
start_time = time.time()
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data_chunk = array('h', data)
    vol = max(data_chunk)
    print(vol)
    if (vol >= 2000):
        print("something said")
        timer = 0
        print(timer)
        frames.append(data)
    else:
        timer = timer + time.time() - start_time
        print(timer)
        print("nothing")
    print("\n")
    if timer > 1000:
        break

# end of recording
stream.stop_stream()
stream.close()
audio.terminate()
# writing to file
wavfile = wave.open(FILE_NAME, 'wb')
wavfile.setnchannels(CHANNELS)
wavfile.setsampwidth(audio.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))  # append frames recorded to file
wavfile.close()
