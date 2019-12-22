import numpy as np
from polynomial_curve_fitting.main21 import generateDataset, f
import matplotlib.pyplot as plt


def OptimizeLS(x, t, M):
    phi = np.zeros((len(x), M+1))
    for n in range(len(x)):
        for m in range(M+1):
            phi[n][m] = pow(x[n], m)
    wls = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)), phi.T), t)
    return wls


def compute(cs, x):
    ans = 0
    for i in range(len(cs)):
        ans += cs[i] + pow(x, i)
    return ans


if __name__ == "__main__":
    ns = [1, 3, 5, 10]
    for n in ns:
        (vector1, vector2) = generateDataset(10, f, 0.03)
        coefficients = OptimizeLS(vector1, vector2, n)
        approx_values = [compute(coefficients, x) for x in vector1]
        values = [f(x) for x in vector1]
        area = np.pi * 3
        plt.scatter(vector1, values, s=area, c='red', alpha=0.5)
        plt.scatter(vector1, approx_values, s=area, c='blue', alpha=0.5)
        plt.title('Scatter plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
