#!/usr/bin/env python
import numpy as np
from numpy.fft import *
from matplotlib import pyplot as plt
import radiolab, pylab, os

ShowPlot = True

N = 256
samp_freq = 10*4 # 10 kHz sampling frequency
VppLev = 1 # 1 Volt
NPer = 5 # Number of periods (Points to display)

N_an = 1024

DataN = np.genfromtxt('data_10')

dt = 1./samp_freq
t = dt*np.arange(N)
t = t[0:(NPer+1)]

OffPhase = np.arcsin(DataN[0]/VppLev)
t_an = np.arange(N_an)*(dt*NPer/N_an)
Sig_an = np.sin(NPer*2*np.pi*t_an/t_an[N_an-1] + OffPhase)

freqAx = fftfreq(N,dt)
freqAx = fftshift(freqAx)

DataN = np.genfromtxt('data_10')

plt.figure()
plt.plot(t,DataN[0:(NPer+1)],marker='o',markerfacecolor='k',linewidth=2.5)
pylab.ylim([-1,1])
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(b=True,which='major',color='g')
plt.grid(b=True,which='minor',color='g')
plt.plot(t_an,Sig_an,linestyle='--')
plt.xlabel('Time (seconds)')
plt.ylabel('$V(t)$ (Volts)')
plt.title('Signal Sampled at Nyquist Frequency')


if ShowPlot:
	plt.show()
