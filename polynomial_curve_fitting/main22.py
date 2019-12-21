import numpy as np
from polynomial_curve_fitting.main21 import generateDataset, f


def OptimizeLS(x, t, M):
    phi = np.zeros((len(x), M))
    for n in range(len(x)):
        for m in range(M):
            # TODO I AM NOT SURE THAT THIS IS THE MEANING HERE - NEED TO CHECK WITH ELHADAD
            phi[n][m] = pow(x[n], m)
    wls = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi)), phi.T), t)
    return wls


def compute(cs, x):
    ans = 0
    for i in range(len(cs)):
        ans += cs[i] + pow(x, i)
    return ans


if __name__ == "__main__":
    (vector1, vector2) = generateDataset(10, f, 0.03)
    coefficients = OptimizeLS(vector1, vector2, 10)
    approx_values = [compute(coefficients, x) for x in vector1]
    values = [f(x) for x in vector1]
    print(approx_values)
    print(values)
