import math
import matplotlib.pyplot as plt
import numpy as np


def generateDataset(N, f, sigma):
    mu = 0.0
    x = list(i / (N-1) for i in range(N))
    t = list(f(x_i)+np.random.normal(mu, sigma) for x_i in x)
    return tuple([np.array(x), np.array(t)])


def f(x):
    return math.sin(x*math.pi)


if __name__ == "__main__":
    (vector1, vector2) = generateDataset(100, f, 0.03)
    colors = (0, 0, 0)
    area = np.pi * 3
    plt.scatter(vector1, vector2, s=area, c=colors, alpha=0.5)
    plt.title('Scatter plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
