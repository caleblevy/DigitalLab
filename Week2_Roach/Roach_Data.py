#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *
from subprocess import call

a = np.fromfile('abc_bram',count=-1,sep=" ")

