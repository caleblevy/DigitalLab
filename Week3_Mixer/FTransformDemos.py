#!/usr/bin/env python
import numpy as np 
from numpy.fft import *
from matplotlib import pyplot as plt
import radiolab

N = 18
Window = 15 # Centered window

Fir = np.zeros(N)
Fir[N/2+1:N/2+1+(Window-1)/2] = 1.0
Fir[N/2-(Window-1)/2:N/2+1] = 1.0
print Fir

plt.figure(0)
Fir = fftshift(Fir)
Fir = ifft(Fir)
plt.plot(Fir)
plt.plot(fftshift(Fir))



print Fir


plt.figure(1)

Fir2 = np.zeros(15)
Fir2[7] = 1
Fir2[8] = 1
Fir2[9] = 1
Fir2[6] = 1
Fir2[5] = 1

print Fir2

Fir2 = fftshift(Fir2)
Fir2 = ifft(Fir2)
Fir2 = np.real(Fir2)
plt.plot(Fir2)
plt.show()
