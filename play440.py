import numpy as np
import wave
import matplotlib.pyplot as plt
from playsound import playsound
import argparse

#Parse Sampling Frequency
parser = argparse.ArgumentParser()
parser.add_argument("Fs",help = "Sampling Frequency")
args = parser.parse_args()

Fs = int(args.Fs)

#Note function
n = np.linspace(0,1,Fs) #1 period discrete linespace
y = (2**15-1)*np.sin(2*np.pi*440.0*n) #discrete function
y = y.astype("<h") #change integer type for WAV format


#save as WAV file
with wave.open('note.wav', 'w') as sound:
    sound.setnchannels(1)
    sound.setsampwidth(2)
    sound.setframerate(Fs)
    sound.writeframesraw(y)

#playback
playsound('note.wav')
