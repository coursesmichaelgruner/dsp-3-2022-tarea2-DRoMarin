import numpy as np
import wave
import matplotlib.pyplot as plt
from playsound import playsound

Fs = 8000

n = np.linspace(0,1,Fs)
y = (2**15-1)*np.sin(2*np.pi*440.0*n)
y = y.astype("<h")
with wave.open('note.wav', 'w') as sound:
    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(Fs)
    sound.writeframesraw(y)

playsound('note.wav')
