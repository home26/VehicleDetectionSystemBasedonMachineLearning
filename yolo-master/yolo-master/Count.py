import numpy as np
import matplotlib.pyplot as plt
import time
a= \
    [2,2,2,2,2,2,2,2,3,2,2,1,2,2,2,2,3,2,4,1,7,1,5,3,6,4,5,5,5,3,5,3,2,0,2,1,2,1,3,0,4,2,4,2,2,1,8,4,6,4,3,0,2,1,5,1,5,1,5,3,5,3,3,1,4,2,5,2,4,3,7,2,5,2,4,2,4,3,2,1,5,5,5,3,3,2,4,2,3,1,3,1,5,3,7,4,5,5,4,4,4,3,4,4,4,4,4,4,3,2,3,3,3,3,4,3,3,3,5,3,4,4,3,3,3,2,2,2,2,2,1,1,1,1,1,1,2,2,3,1,3,0,4,1,5,4,4,2,4,4,5,5,4,3,4,2,4,3,3,3,6,6,5,3,3,3,4,3,2,2,1,1,0,0,0,0,2,2,3,2,3,1,4,1,3,2,3,1,3,1,5,5,6,6,6,5,5,4,3,2,3,3,3,3,5,3,6,4,5,3,8,3,7,6,5,5,5,4,7,7,8,6,8,6,8,5,7,4,7,2,5,5,5,5,5,5,5,4,5,5,5,5,6,6,5,5,6,6,6,6,4,4,4,4,3,3,4,4,4,4,4,4,4,4,3,3,2,2,4,4,3,3,3,1,3,3,5,5,4,4,7,6,4,3,5,3,5,3,4,3,4,4,5,5,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,4,1,4,2,4,2,4,2,3,2,6,5,4,4,4,4,4,4,3,2,4,3,5,3,4,3,4,4,5,5,4,3,4,4,4,4,4,4,3,1,2,2,2,2,2,2,3,3,2,2,2,2,1,1,1,1,4,4,5,5,5,5,3,3,3,2,5,3,3,3,5,5,4,4,4,3,4,4,5,4,3,3,4,4,5,4,5,4,4,2,3,2,2,2,3,3,3,3,2,2,3,3,2,2,4,4,3,3,2,2,2,2,0,0,1,1,4,2,5,4]
data = np.array([[2,2,2,2,2,2,2,2,3,2,2,1,2,2,2,2,3,2,4,1,7,1,5,3,6,4,5,5,5,3,5,3,2,0,2,1,2,1,3,0,4,2,4,2,2,1,8,4,6,4,3,0,2,1,5,1,5,1,5,3,5,3,3,1,4,2,5,2,4,3,7,2,5,2,4,2,4,3,2,1,5,5,5,3,3,2,4,2,3,1,3,1,5,3,7,4,5,5,4,4,4,3,4,4,4,4,4,4,3,2,3,3,3,3,4,3,3,3,5,3,4,4,3,3,3,2,2,2,2,2,1,1,1,1,1,1,2,2,3,1,3,0,4,1,5,4,4,2,4,4,5,5,4,3,4,2,4,3,3,3,6,6,5,3,3,3,4,3,2,2,1,1,0,0,0,0,2,2,3,2,3,1,4,1,3,2,3,1,3,1,5,5,6,6,6,5,5,4,3,2,3,3,3,3,5,3,6,4,5,3,8,3,7,6,5,5,5,4,7,7,8,6,8,6,8,5,7,4,7,2,5,5,5,5,5,5,5,4,5,5,5,5,6,6,5,5,6,6,6,6,4,4,4,4,3,3,4,4,4,4,4,4,4,4,3,3,2,2,4,4,3,3,3,1,3,3,5,5,4,4,7,6,4,3,5,3,5,3,4,3,4,4,5,5,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,4,1,4,2,4,2,4,2,3,2,6,5,4,4,4,4,4,4,3,2,4,3,5,3,4,3,4,4,5,5,4,3,4,4,4,4,4,4,3,1,2,2,2,2,2,2,3,3,2,2,2,2,1,1,1,1,4,4,5,5,5,5,3,3,3,2,5,3,3,3,5,5,4,4,4,3,4,4,5,4,3,3,4,4,5,4,5,4,4,2,3,2,2,2,3,3,3,3,2,2,3,3,2,2,4,4,3,3,2,2,2,2,0,0,1,1,4,2,5,4]],dtype=float)
print(data.shape)
fact = np.zeros([1,216],dtype=float)
detect = np.zeros([1,216],dtype=float)
ratio = np.zeros([1,216],dtype=float)
m = 0
n = 0
total = float(0)
for i in range(0,431):
    if i%2 == 0:
        fact[0,m] = data[0,i]
        m += 1
    if i%2 == 1:
        detect[0,n] = data[0,i]
        n += 1
print(fact.shape)
print(detect.shape)
for i in range(0,215):
    if fact[0,i] != 0:
        ratio[0,i] = detect[0,i] / fact[0,i]
    if fact[0,i] == 0:
        ratio[0,i] == 0.0
    total = total + ratio[0,i]
average = total / 216
print(fact.shape,detect.shape,ratio.shape)
print(fact,detect,ratio)

'''
fact_dynamic = np.zeros([1,219],dtype=float)
detect_dynamic = np.zeros([1,219],dtype=float)
ratio_dynamic = np.zeros([1,219],dtype=float)
x_dynamic = np.zeros([1,219],dtype=float)

fact_dynamic[0,0] = 0
detect_dynamic[0,0] = 0
x_dynamic[0,0] = 0
ratio_dynamic[0,0] = 0

for i in range(0,216):
    fact_dynamic[0,1+i] = fact[0,i]
    detect_dynamic[0,1+i] = detect[0,i]
    ratio_dynamic[0,1+i] = ratio[0,i]
    x_dynamic[0,1+i] = i

x_dynamic[0,217] = 216
x_dynamic[0,218] = 217
fact_dynamic[0,217] = 8
fact_dynamic[0,218] = 8
detect_dynamic[0,217] = 8
detect_dynamic[0,218] = 8
ratio_dynamic[0,217] = 1
ratio_dynamic[0,218] = 1


plt.axis([0, 220, 0, 8])
plt.xlabel('Time/S')
plt.ylabel('Number of Vehicles')
plt.ion()


for i in range(0,216):
    #print('success',i)
    plt.plot(x_dynamic[0,i:i+2],detect_dynamic[0,i:i+2],color='r',label = 'Car Detected')
    plt.plot(x_dynamic[0,i:i+2],fact_dynamic[0,i:i+2],color='b',label = 'Real Situation')
    plt.plot(x_dynamic[0,i:i+2],ratio_dynamic[0,i:i+2],color='g',label = 'Detection Ratio')
    #t1 = time.time()
    plt.pause(1)
    #t2 = time.time()
    #print(t2-t1)
'''

'''
x = range(0,216)
plt.figure()
plt.plot(x,detect[0,0:],'r',label = 'Car Detected')
plt.plot(x,fact[0,0:],'b',label = 'Real Situation')
plt.plot(x,ratio[0,0:],'g',label = 'Detection Ratio')
plt.xlabel('Time/S')
plt.ylabel('Number of Vehicles')
plt.legend()
plt.show()
'''