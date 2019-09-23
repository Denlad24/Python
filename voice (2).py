import pyaudio
import numpy as np
import time

flag = True
timer = 0
start_time = time.time()
while flag == True:
    maxvalue = 2 ** 16
    p = pyaudio.PyAudio()
    print("Таймер простоя=", timer)
    stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100,
                    input=True, frames_per_buffer=1024)
    data = np.fromstring(stream.read(1024), dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL) - np.min(dataL)) / maxvalue
    peakR = np.abs(np.max(dataR) - np.min(dataR)) / maxvalue
    timer = timer + time.time() - start_time
    if peakL > 0.3:
        print(peakL)
        print("test")
        timer = 0
    if timer > 500:
        flag = False
