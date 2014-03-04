#!/usr/bin/env python
import numpy as np 
from numpy.fft import *
from matplotlib import pyplot as plt
import radiolab
import os

N = 8
Window = 5 # Centered window

Fir = np.zeros(N)
Fir[N/2+1:N/2+1+(Window-1)/2] = 1.0
Fir[N/2-(Window-1)/2:N/2+1] = 1.0

FirShift = fftshift(Fir)
FirPhys = ifft(FirShift)

FirCoeffs = fftshift(FirPhys)
FirCoeffs = np.real(FirCoeffs)

