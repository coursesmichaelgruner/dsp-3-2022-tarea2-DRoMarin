import numpy as np
import wave
import matplotlib.pyplot as plt

Fs = 8000

n = np.linspace(0,1,Fs)
y = (2**15-1)*np.sin(2*np.pi*440.0*n)
y = y.astype("<h")
sound = wave.open('note.wav', 'w')
sound.setnchannels(1)
sound.setsampwidth(2)
sound.setframerate(Fs)
sound.writeframesraw(y)
