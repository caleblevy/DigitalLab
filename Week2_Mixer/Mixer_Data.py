#! /usr/bin/env python
import numpy as np
import radiolab as rdo
import matplotlib.pyplot as plt
from numpy.fft import *

nu_lo = 10**5 # Local Oscillator frequency at 10 kHz
d_nu = 0.05*nu_lo # Delta nu is 5%
Pad = 20. # Safety factor

nu_sig = nu_lo + d_nu 
PLev = 0.0 # Default power levels in dBm

radiolab.set_srs(2,nu_lo,dbm=PLev,off=0.0,pha=0.0)
radiolab.set_srs(1,nu_sig,dbm=PLev,off=0.0,pha=0.0) # Set to defaults, with additive delta nu this time

f_samp = Pad*2*nu_lo # Five times Nyquist
N_samp = 2*Pad**2*nu_lo/d_nu # Five minimum sampling periods

MixAnData = radiolab.sampler(N_samp,f_samp,fileName='Mixer_Analogue',dual=False,low=False,integer=False,timeWarn=True)
plt.plot(MixAnData)
plt.show()
