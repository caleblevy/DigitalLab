mport numpy as np
import radiolab as rdo
import matplotlib.pyplot as plt
from numpy.fft import *

Collect = False

nu_sig = 10**6 # Local Oscillator frequency at 10 kHz
d_nu = 0.25*nu_lo # Delta nu is 5%
Pad = 5 # Safety factor

nu_lo = nu_lo - d_nu
P_lo = -7.0
P_sig = -3.0

# 

