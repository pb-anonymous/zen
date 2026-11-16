from scipy import integrate
import numpy as np
x = np.linspace(0, 10, 100)
def f(x):
    return x**2
result, error = integrate.quad(f, 0, 10)
print(result)