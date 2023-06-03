


''' sr = 100.0
# sampling interval
ts = 1.0/sr
t = np.arange(0, 1, ts)

# frequency of the signal
freq = 5
amplitude = 5
phase = 0
y = amplitude * np.sin(2*np.pi*freq*t + phase)

plt.figure(figsize=(8, 8))

plt.subplot(211)
plt.plot(t, y, "b")
plt.ylabel("Amplitude")

freq = 5
amplitude = 10
phase = 10
y = amplitude * np.sin(2*np.pi*freq*t + phase)

plt.subplot(212)
plt.plot(t, y, 'b')
plt.ylabel("Amplitude")
plt.xlabel("Time (s)")
plt.show()
 '''


''' sr = 100.0
tr = 1/sr
t = np.arange(0, 1, tr)

plt.figure(figsize=(8, 8))

freq = 1
amplitude = 3
phase = 0
x = amplitude*np.sin(2*np.pi*freq*t + phase)


freq = 4
amplitude = 1
phase = 0

x += amplitude*np.sin(2*np.pi*freq*t + phase)


freq = 7
amplitude = 0.5
phase = 0
x += amplitude*np.sin(2*np.pi*freq*t + phase) '''

''' plt.plot(t, x, "r")
plt.ylabel("Amplitude")
plt.show()
 '''


''' def DFT(x):
    """
    Function to calculate the
    discrete Fourier Transform
    of a 1D
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(e, x)

    return X


X = DFT(x)

# calculate frequency
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T
plt.figure(figsize=(8, 6))
plt.stem(freq, abs(X), "b", markerfmt=" ", basefmt="-b")
plt.xlabel("Freq (Hz)")
plt.ylabel("DFT Amplitude |X(freq)|")
plt.show()
 '''


''' Write a function to generate a simple signal with a different sampling rate, and see the
difference in computing time by varying the sampling rate. '''


''' def gen_sig(sr):
    ts = 1/sr
    t = np.arange(0, 1, ts)

    freq = 1
    amp = 3
    phase = 0
    x = amp * np.sin(2*np.pi*freq*t + phase)

    return x


sr = 2000
gen_sig(sr)
 '''


''' plt.style.use("seaborn-poster")


def FFT(x):
    """
    A recursive implementation of
    the 1D Cooley-Tukey FFT, the
    input should have a length of
    power of 2.
    """
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N)/N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X


sr = 128
ts = 1/sr
t = np.arange(0, 1, ts)

freq = 1
x = 3*np.sin(2*np.pi*freq*t)
freq = 4
x += np.sin(2*np.pi*freq*t)
freq = 7
x += 0.5 * np.sin(2*np.pi*freq*t)
plt.figure(figsize=(8, 6))
plt.plot(t, x, "r")
plt.ylabel("Amplitude")
plt.show()
 '''


import time
import matplotlib.pyplot as plt
import numpy as np

def DFT(x):
    """
    Function to calculate the
    discrete Fourier Transform
    of a 1D
    """
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(e, x)

    return X


def FFT(x):
    """
    A recursive implementation of
    the 1D Cooley-Tukey FFT, the
    input should have a length of
    power of 2.
    """
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N)/N)
        X = np.concatenate(
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X


def gen_sig(sr):
    """
function to generate
a simple 1D signal with
different sampling rate
"""
    ts = 1.0/sr
    t = np.arange(0, 1, ts)
    freq = 1.
    x = 3*np.sin(2*np.pi*freq*t)
    return x


sr = 2048
start_time = time.time()
DFT(gen_sig(sr))
print("--- %s DTF runtime in seconds ---" % (time.time() - start_time))
start_time = time.time()
FFT(gen_sig(sr))
print("--- %s FFT runtime in seconds ---" % (time.time() - start_time))
