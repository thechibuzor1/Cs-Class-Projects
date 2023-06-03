''' from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn-poster")

x = [0, 1, 2]
y = [1, 3, 2]

# use bc_type = "natural" adds the constraints
f = CubicSpline(x, y, bc_type="natural")

x_new = np.linspace(0, 2, 100)
y_new = f(x_new)

plt.figure(figsize=(10, 8))
plt.plot(x_new, y_new, "b")
plt.plot(x, y, "ro")
plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
 '''

import numpy as np
import matplotlib.pyplot as plt


def my_cubic_spline(x, y, X):
    # compute the cubic spline coefficients
    n = len(x)
    h = np.diff(x)
    b = np.zeros(n)
    u = np.zeros(n)
    v = np.zeros(n)
    z = np.zeros(n)
    for i in range(1, n-1):
        b[i] = 2 * (h[i-1] + h[i])
        u[i] = 6 * ((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])
        z[i] = (u[i] - h[i-1]*z[i-1])/b[i]
    for i in range(n-2, 0, -1):
        z[i] = (u[i] - h[i]*z[i+1])/b[i]
    # compute the cubic spline coefficients for each segment
    a = np.zeros(n-1)
    c = np.zeros(n-1)
    for i in range(n-1):
        a[i] = y[i]
        c[i] = (z[i+1] - z[i])/(6*h[i])
    b = np.diff(z)/(2*h)
    # interpolate at the query points
    Y = np.zeros_like(X)
    for i, xq in enumerate(X):
        j = np.searchsorted(x, xq) - 1
        if j < 0:
            j = 0
        elif j >= n-1:
            j = n-2
        dx = xq - x[j]
        Y[i] = a[j] + b[j]*dx + c[j]*dx**2 + z[j]*dx**3/h[j]
    return Y


# generate some random data
x = np.linspace(0, 10, 11)
y = np.sin(x)

# interpolate with cubic spline
X = np.linspace(0, 10, 101)
Y = my_cubic_spline(x, y, X)

# plot the results
plt.plot(x, y, 'o', label='data')
plt.plot(X, np.sin(X), '-', label='true')
plt.plot(X, Y, '--', label='cubic spline')
plt.legend()
plt.show()
