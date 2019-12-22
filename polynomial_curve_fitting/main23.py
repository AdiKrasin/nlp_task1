import numpy as np
from polynomial_curve_fitting.main21 import f
import matplotlib.pyplot as plt


def optimizePLS(x, t, M, lambdaa):
    phi = np.zeros((len(x), M + 1))
    ones = np.ones((len(x) + 1, M + 1))
    for n in range(len(x)):
        for m in range(M + 1):
            phi[n][m] = pow(x[n], m)
    wls = np.dot(np.dot(np.linalg.inv(np.dot(phi.T, phi) + np.dot(lambdaa, ones)), phi.T), t)
    return wls


def compute(cs, x):
    ans = 0
    for i in range(len(cs)):
        ans += cs[i] + pow(x, i)
    return ans


def generateDataset3(N, f, sigma):
    N = 3*N
    mu = 0.0
    x_before_split = list(i / (N - 1) for i in range(N))
    np.random.shuffle(x_before_split)
    x1 = x_before_split[0:int(N/3)]
    x2 = x_before_split[int(N/3):int(2*N/3)]
    x3 = x_before_split[int(2*N/3):]
    t1 = list(f(x_i) + np.random.normal(mu, sigma) for x_i in x1)
    t2 = list(f(x_i) + np.random.normal(mu, sigma) for x_i in x2)
    t3 = list(f(x_i) + np.random.normal(mu, sigma) for x_i in x3)
    return tuple([np.array(x1), np.array(t1), np.array(x2), np.array(t2), np.array(x3), np.array(t3)])


def optimizePLS2(xt, tt, xv, tv, M):
    log_lambdas = range(-40, -20)
    possible_lambdas = [pow(2, x) for x in log_lambdas]
    chosen_lambda = 0
    error = False
    for my_lambda in possible_lambdas:
        coefficients_t = optimizePLS(xt, tt, M, my_lambda)
        approx_values_t = [compute(coefficients_t, x) for x in xt]
        values_t = [f(x) for x in xt]
        coefficients_v = optimizePLS(xv, tv, M, my_lambda)
        approx_values_v = [compute(coefficients_v, x) for x in xv]
        values_v = [f(x) for x in xv]
        # TODO NEED TO MAKE THESE TWO CALCULATIONS OF THE ERROR
        first_error = 0
        second_error = 0
        this_iter_error = max(first_error, second_error)
        if error is not False:
            if this_iter_error < error:
                error = this_iter_error
                chosen_lambda = my_lambda
        else:
            error = this_iter_error
    return chosen_lambda


if __name__ == "__main__":
    ms = [10, 100]
    for m in ms:
        x_test, t_test, x_valid, t_valid, x_train, t_train = generateDataset3(m, f, 0.03)
        my_lambda = optimizePLS2(x_train, t_train, x_valid, t_valid, m)
        coefficients = optimizePLS(x_test, t_test, m, my_lambda)
        approx_values = [compute(coefficients, x) for x in x_test]
        values = [f(x) for x in x_test]
        area = np.pi * 3
        plt.scatter(x_test, values, s=area, c='red', alpha=0.5)
        plt.scatter(x_test, approx_values, s=area, c='blue', alpha=0.5)
        plt.title('Scatter plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
