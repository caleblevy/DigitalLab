#!/usr/bin/env python
import numpy as np 
from numpy.fft import *
from matplotlib import pyplot as plt
import radiolab

N = 8
Window = 5 # Centered window

Fir = np.zeros(N)
Fir[N/2+1:N/2+1+(Window-1)/2] = 1.0
Fir[N/2-(Window-1)/2:N/2+1] = 1.0

FirShift = fftshift(Fir)
FirPhys = ifft(FirShift)

FirCoeffs = fftshift(FirPhys)
FirCoeffs = np.real(FirCoeffs)

plt.figure(1)
plt.plot(FirCoeffs)

# Demonstration of "padding with zeros to achieve higer resolution
N_Extend = 128 # Extend to 2*Extend
FirEx = np.zeros(N_Extend)
FirEx[N_Extend/2+1:N_Extend/2+1+(Window-1)/2] = 1.0
FirEx[N_Extend/2-(Window-1)/2:N_Extend/2+1] = 1.0

FirShiftEx = fftshift(FirEx)
FirPhysEx = ifft(FirShiftEx)

FirCoeffsEx = fftshift(FirPhysEx)
FirCoeffsEx = np.real(FirCoeffsEx)

plt.figure(0)
plt.plot(FirCoeffsEx)
plt.show()


