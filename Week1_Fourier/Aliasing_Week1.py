#! /usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import *
import DFEC

DoLoop = True

N = 256
samp_freq = 10**4 # 10 kHz sampling frequency
N_Pics = 10
sig_freq = samp_freq*(1./N_Pics) # (1,2,...,10)kHz


if DoLoop:
	for f in range(1,N_Pics+1):
		DFEC.set_srs(1,freq=1.0*f*sig_freq,off=0.0,pha=0.0,vpp=1.0)
		a = DFEC.sampler(N,samp_freq,fileName='data_'+str(f),dual=False,low=False,integer=False,timeWarn=True)

    DFEC.set_srs(1,freq=10**7,off=0.0,pha=0.0,vpp=1.0)
    a = DFEC.sampler(N,samp_freq,fileName='data_low_freq',dual=False,low=False,integer=False,timeWarn=True)


    
    
    
    

    
