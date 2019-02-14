from __future__ import print_function
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft,ifft

# 1. Get the file path to the included audio example
filename = './data/archive/_caustic_-20170306-smy/wav/en-0185.wav'
sample_rate, audio = wavfile.read(filename)
N = 320
print(audio.shape)

result = np.zeros((int(len(audio)/N),int(N/2)))

for i in range(int(len(audio)/N)):
    transformed = fft(audio[i:(i+1)*N])
    freq = np.fft.fftfreq(transformed.size, 1/sample_rate)[:int(N/2)]
    result[i] = np.abs(transformed[:int(N/2)])

print(result)


