from pylab import *
import matplotlib.pyplot as plt


def phi(x):
    return np.array([pow(x, i) for i in range(M + 1)]).reshape((M + 1, 1))


def m(x, x_train, y_train, S):
    def ans():
        sum = np.array(zeros((M + 1, 1)))
        for n in range(len(x_train)):
            sum += np.dot(phi(x_train[n]), y_train[n])
        return sigma2 * phi(x).T.dot(S).dot(sum)
    return ans


def s2(x, S):
    def ans():
        return 1.0 / sigma2 + phi(x).T.dot(S).dot(phi(x))
    return ans



def bayesianEstimator(x, t, M, alpha, sigma2):

    def S(x_train):
        I = np.identity(M + 1)
        Sigma = np.zeros((M + 1, M + 1))
        for n in range(len(x_train)):
            Sigma += np.dot(phi(x_train[n]), phi(x_train[n]).T)
        S_inv = alpha * I + sigma2 * Sigma
        S = inv(S_inv)
        return S

    S = S(x)

    mean = [m(x_i, x, t, S)()[0, 0] for x_i in actual_x_values]
    variance = [s2(x_i, S)()[0, 0] for x_i in actual_x_values]

    area = np.pi * 3
    plt.scatter(x_train, y_train, s=area, c='red', alpha=0.5)
    plt.scatter(actual_x_values, actual_y_values, s=area, c='blue', alpha=0.5)
    plt.scatter(actual_x_values, mean, s=area, c='green', alpha=0.5)
    plt.show()

    area = np.pi * 3
    plt.scatter(x_train, y_train, s=area, c='red', alpha=0.5)
    plt.scatter(actual_x_values, actual_y_values, s=area, c='blue', alpha=0.5)
    plt.scatter(actual_x_values, variance, s=area, c='green', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    alpha = 0.005
    sigma2 = 1/11.1
    M = 9
    ns = [10, 100]

    for N in ns:

        actual_x_values = np.arange(0, 1, 0.01)
        actual_y_values = np.sin(np.pi * actual_x_values)

        x_train = np.linspace(0, 1, N)

        loc = 0
        scale = 0.3
        y_train = np.sin(np.pi * x_train) + np.random.normal(loc, scale, N)

        bayesianEstimator(x_train, y_train, M, alpha, sigma2)

