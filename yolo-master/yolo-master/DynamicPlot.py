import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 10])
plt.ion()

x=[0.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.]
y=[0.,0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,8.]
y1=[0.,9.,8.,7.,6.,5.,4.,3.,2.,1.,0.,0.]

for i in range(0,10):
    plt.plot(x[i:i+2],y[i:i+2],color='r')
    plt.plot(x[i:i+2],y1[i:i+2],color='b')
    plt.pause(1)