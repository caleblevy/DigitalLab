#! /usr/bin/env python
from numpy.fft import *
import numpy as np
from matplotlib import pyplot as plt

pi = np.pi

# Initialization
N = 1024
freqs = [1,2,3,6,10,12,13,20,22,24,26]
Amps = [2,3,4,1,1,4,3,1./2,2,3,3]
P = 2*pi # Period 2*pi

t = np.arange(N,dtype=float)
t = t/N*P

Sig = np.zeros(N)
for I in range(len(freqs)):
    Sig += Amps[I]*np.sin(freqs[I]*t)
    
Tran = fft(Sig)
omega = fftfreq(N,P/N)

Fig = plt.figure(0)
plt.plot(t,Sig)

TFig = plt.figure(1)
plt.plot(sort(omega),np.abs(Tran))


plt.show()



