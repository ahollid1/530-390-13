#!/usr/bin/env python
import numpy as np 
import time
import helper 
import matplotlib.pyplot as plt
#Code is ugly but functional 
#Comparing run times for n=100
n = 100
A = np.random.rand(n)
A2 = np.array(A)
t0 = time.time()
helper.selectionsort(A,n)
t1 = time.time()
helper.mergesort(A2,n)
t2 = time.time()
print((t1-t0)/(t2-t1))
T1=t1-t0
T2=t2-t1
#Comparing run times for n=1000
n = 1000
A = np.random.rand(n)
A2 = np.array(A)
t0 = time.time()
helper.selectionsort(A,n)
t1 = time.time()
helper.mergesort(A2,n)
t2 = time.time()
print((t1-t0)/(t2-t1))

T3=t1-t0
T4=t2-t1
#Comparing run times for n=10000
n = 10000
A = np.random.rand(n)
A2 = np.array(A)
t0 = time.time()
helper.selectionsort(A,n)
t1 = time.time()
helper.mergesort(A2,n)
t2 = time.time()
print((t1-t0)/(t2-t1))

T5=t1-t0
T6=t2-t1

plt.plot([100,1000,10000],[T1,T3,T5])
plt.plot([100,1000,10000],[T2,T4,T6])

# Question 2  - Fibonacci
print(helper.fibonacci(24))

#Question 3 

PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(4.*x[i])
  y[2*i+1] = 0

helper.plot_c(x,y)
y = helper.fft_slow(y,1.)
helper.plot_c(f[:0.5*N],y[:N])


PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(13.*x[i])
  y[2*i+1] = 0

helper.plot_c(x,y)
y = helper.fft_slow(y,1.)
helper.plot_c(f[:0.5*N],y[:N])

PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(28.*x[i])
  y[2*i+1] = 0

helper.plot_c(x,y)
y = helper.fft_slow(y,1.)
helper.plot_c(f[:0.5*N],y[:N])

PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(39.*x[i])
  y[2*i+1] = 0

helper.plot_c(x,y)
y = helper.fft_slow(y,1.)
helper.plot_c(f[:0.5*N],y[:N])

PI = 2*np.arcsin(1)
N = 64
L = 2*PI
dx = L / (N-1)
x = np.zeros(N)
f = np.zeros(N)
y = np.zeros(2*N)

for i in range(N):
  x[i] = i*dx
  f[i] = i
  y[2*i] = np.sin(x[i]) + np.sin(50.*x[i])
  y[2*i+1] = 0

helper.plot_c(x,y)
y = helper.fft_slow(y,1.)
helper.plot_c(f[:0.5*N],y[:N])
plt.show()
