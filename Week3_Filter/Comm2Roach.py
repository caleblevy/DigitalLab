mport numpy as np
import matplotlib.pyplot as plt
from numpy.fft import *
from subprocess import call
import os

os,system('ssh root@roach rm -rf ~/*')
os.system('scp ./Roach_Simple.sh root@roach:~/')
os.system('ssh root@roach Roach_Simple.sh')
os.system('scp -r root@roach:~/ ./DataFolds/')
os.system('ssh root@roach rm -rf ~/*')
