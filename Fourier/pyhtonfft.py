from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt


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
X = fft(gen_sig(sr))
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T
t = np.arange(0, 1, 1/sr)


plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.stem(freq, np.abs(X), "b", markerfmt=" ", basefmt="-b")
plt.xlabel("Freq (Hz)")
plt.ylabel("FFT Amplitude |X(freq)|")
plt.xlim(0, 10)
plt.subplot(122)
plt.plot(t, ifft(X), "r")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
