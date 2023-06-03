import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
df = pd.read_csv('C:/Users/DELL/Desktop/Cs Class Projects/Fourier/data/930-data-export.csv',
                 delimiter=',', parse_dates=[1])
df.rename(columns={"Selected Hour Timestamp (Hour Ending)": "hour",
                   "Prior Hour Demand (MWh)": "demand"},
          inplace=True)


X = fft(df["demand"])
N = len(X)
n = np.arange(N)

# get the sampling rate
sr = 1/(60*60)  # since its hourly

T = N/sr
freq = n/T

# Get the one-sided spectrum
n_oneside = N//2

# get the one side frequency
f_oneside = freq[:n_oneside]

plt.figure(figsize=(12, 6))
plt.plot(f_oneside, np.abs(X[:n_oneside]), "b")
plt.xlabel("Freq (Hz)")
plt.ylabel("FFT Amplitude |X(freq)|")
plt.show()
