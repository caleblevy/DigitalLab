#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *
from subprocess import call
import radiolab
import os

Collect = False
RoachGet = True

f_sig = 20.e6 # Local oscillator
PLev = -3.0 #DBM

lo_nums = [1,2,4,8]
BaseDir = os.getcwd()

# Plus Part

if Collect:
	radiolab.set_srs(1,freq=f_lo,dbm=PLev,off=0.0,pha=0.0)

def PermRes():
	os.system("ssh root@roach 'chmod -f 777 ~/*'") # Reset Permissions

# I have reached a developmental milestone: I have made my first hack code
if RoachGet:
	os.system('rm -rf lo_*')
	os.system('mkdir -p Data_Temp_lo')

	PermRes()
	os.system("ssh root@roach 'rm -rf ~/*'")
	os.system("scp Roach_lo.sh root@roach:~/")
	PermRes()
	os.system("ssh root@roach './Roach_lo.sh'")
	os.chdir('Data_Temp_lo')
	os.system("scp -r root@roach:~/* ./")
	os.system("ssh root@roach 'rm -rf ~/*'")
	
	os.system("mv lo_* ../")
	os.chdir(BaseDir)
	os.system("rm -rf Data_Temp_lo")
	

N_samp = 2048 # Set by adc
f_samp = 200e6 # 200 MHz
dt = 1./f_samp
t = [I*dt for I in range(N_samp)]

FreqAx = fftfreq(N_samp,dt)
FreqAx = fftshift(FreqAx)

for I in lo_nums:
	lo_freq = I
	lo_F = 1.0*(I/256)*f_samp
	
	os.chdir('lo_mix_'+str(I))
	Data_Sin = np.fromfile('sin_bram','>i4')
	Data_Cos = np.fromfile('cos_bram','>i4')
	
	plt.figure(3*I)
	plt.plot(t,Data_Sin)
	plt.figure(3*I+1)
	plt.plot(t,Data_Cos)

	Data_Exp = Data_Sin + 1j*Data_Cos
	Data_Four = fft(Data_Exp)
	Data_Four = fftshift(abs(Data_Four))
	plt.figure(3*I+3)
	plt.plot(FreqAx,Data_Four)
	
	os.chdir(BaseDir)



plt.show()
