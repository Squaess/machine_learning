import random
import time
import matplotlib.pyplot as plt
import numpy as np

S = [(1,96),(2,84),(3,70),(4,78),(5,52),(6,11),(7,1)]

X = np.matrix([[x, x**2] for x,_ in S])
y = np.matrix([[y] for _,y in S])
print(X,y)

theta = np.matrix('0.; 0.; 0.')

def h(theta, x):
    return theta[0,0] + theta[1,0] * x[0,0] + theta[2,0] * x[0,1]


def loss(theta, X, y):
    m = len(X)
    sum_loss = 0
    for i in range(m):
        hypothesis = h(theta, X[i])
        sq_diff = (hypothesis - y[i,0])**2
        sum_loss += sq_diff
    return 1/(2*m) * sum_loss

def alg(X, y):
    theta = np.matrix('0.; 0.; 0.')
    m = len(X)
    alpha = 0.002
    loss_history = []
    iteration = 100000
    for _ in range(iteration):
        los = loss(theta, X, y)
        # print(los)
        # print(theta)
        # print("*****************")
        loss_history.append(los)
        d_dt0 = 0
        d_dt1 = 0
        d_dt2 = 0
        for i in range(m):
            d_dt0 += h(theta,X[i]) - y[i,0]
            d_dt1 += (h(theta,X[i]) - y[i,0]) * X[i,0]
            d_dt2 += (h(theta,X[i]) - y[i,0]) * X[i,1]
        d_dt0 = 1/m * d_dt0
        d_dt1 = 1/m * d_dt1
        d_dt2 = 1/m * d_dt2
        theta[0, 0] = theta[0, 0] - alpha * d_dt0
        theta[1, 0] = theta[1, 0] - alpha * d_dt1
        theta[2, 0] = theta[2, 0] - alpha * d_dt2

    plt.plot(range(len(loss_history)), loss_history)
    plt.xlabel('iteration')
    plt.ylabel('loss')
    plt.show()
    plt.clf()
    return loss_history, theta

loss_history, theta = alg(X, y)
print(theta)
print(loss_history[-1])
plt.clf()
plt.plot(range(len(X)), [[i[0,0]]for i in y], range(len(X)), [h(theta, x) for x in X])
plt.savefig('hypothesis2.png')

