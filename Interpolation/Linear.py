from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("seaborn-poster")

x = [0, 1, 2]
y = [1, 3, 2]

''' f = interp1d(x, y)
y_hat = f(1.5)
print(y_hat)

plt.figure(figsize=(10, 8))
plt.plot(x, y, "-ob")
plt.plot(1.5, y_hat, "ro")
plt.title("Linear Interpolation at x = 1.5")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
 '''


def my_lin_interp(x, y, X):
    """
    Linear interpolation function.

    Parameters
    ----------
    x : array_like
        The x-coordinates of the data points.
    y : array_like
        The y-coordinates of the data points.
    X : array_like
        The x-coordinates at which to interpolate.

    Returns
    -------
    Y : ndarray
        The interpolated values at the points in X.

    Raises
    ------
    ValueError
        If x and y have different lengths, or if x or X are not in ascending order.

    Examples
    --------
    >>> x = [0, 1, 2, 3]
    >>> y = [1, 3, 2, 4]
    >>> X = [0.5, 1.5, 2.5]
    >>> my_lin_interp(x, y, X)
    array([ 1.5,  2.5,  3. ])
    """

    # Check inputs
    if len(x) != len(y):
        raise ValueError("x and y must have the same length.")
    if not all(x[i] < x[i+1] for i in range(len(x)-1)):
        raise ValueError("x must be in ascending order.")
    if not all(X[i] > x[0] and X[i] < x[-1] for i in range(len(X))):
        raise ValueError("X must be within the range of x.")

    # Initialize output array
    Y = np.zeros(len(X))

    # Interpolate using linear segments
    for i in range(len(X)):
        j = np.searchsorted(x, X[i])
        if j == 0:
            Y[i] = y[0]
        elif j == len(x):
            Y[i] = y[-1]
        else:
            x1, x2 = x[j-1], x[j]
            y1, y2 = y[j-1], y[j]
            Y[i] = y1 + (y2 - y1) * (X[i] - x1) / (x2 - x1)

    return Y


# Generate some sample data
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)

# Generate some query points
X = np.linspace(0, 2*np.pi, 100)

# Interpolate using the custom function
Y = my_lin_interp(x, y, X)

# Plot the results
plt.plot(x, y, 'bo', label='data')
plt.plot(X, np.sin(X), 'k-', label='true function')
plt.plot(X, Y, 'r-', label='interpolation')
plt.legend
