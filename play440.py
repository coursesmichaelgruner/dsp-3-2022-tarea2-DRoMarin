import numpy as np
import wave
import matplotlib.pyplot as plt
n = np.linspace(0,1,44100)
y = (2**15-1)*np.sin(2*np.pi*440.0*n)

sound = wave.open('note.wav', 'w')
print(len(y))
print(y)
plt.plot(n,y)
plt.show()
y = y.astype("<h")
sound.setnchannels(1)
sound.setsampwidth(2)
sound.setframerate(44100)
sound.writeframesraw(y)
