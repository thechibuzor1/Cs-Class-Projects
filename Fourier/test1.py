import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-poster")

x = np.linspace(0, 20, 201)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b')
plt.ylabel("Amplitude")
plt.xlabel("Location (x)")
plt.show()
