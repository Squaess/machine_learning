import random
import time
import matplotlib.pyplot as plt
import numpy as np

S = [(1,96),(2,84),(3,70),(4,78),(5,52),(6,11),(7,1)]

# X2 = np.matrix([[1., x, x**2] for x,_ in S])
# y2 = np.matrix([[y] for _,y in S])
# theta2 = np.matrix([[random.randint(-100,100)],[random.randint(-100,100)],[random.randint(-100,100)]])
X = [x for x,_ in S ]
y = [x for _,x in S ]

# def hyp(theta, X):
#     return np.transpose(theta) * np.transpose(X)

# result = hyp(theta2, X2)
# print(X2, X2.shape)
# print(y2, y2.shape)
# print(theta2, theta2.shape)
# print(result)
# print(result.shape)

# def loss2(theta, X, y):
#     hypot = hyp(theta, X)
#     return 1/X.shape[0] * np.square((np.transpose(hypot) - y )).sum()

# strata = loss2(theta2, X2, y2)
# print(strata)

# def alg2():
#     learning_rate = 0.001
#     theta2 = np.matrix([[random.randint(-100,100)],[random.randint(-100,100)],[random.randint(-100,100)]])
#     loss_history = []
#     m = X2.shape[0]
#     for itera in range(50):
#         tmp_theta = np.zeros(theta2.shape)
#         hypothesis = hyp(theta2, X2)
#         different = hypothesis - np.transpose(y2)
#         tmp_theta[0] = theta2[0] - 1/m * np.multiply(np.transpose(different), X2[:,0]).sum() * learning_rate
#         tmp_theta[1] = theta2[1] - 1/m * np.multiply(np.transpose(different), X2[:,1]).sum() * learning_rate
#         tmp_theta[2] = theta2[2] - 1/m * np.multiply(np.transpose(different), X2[:,2]).sum() * learning_rate
#         print(tmp_theta, loss2(tmp_theta, X2, y2))
#         # time.sleep(1)
#         theta2 = tmp_theta.copy()
#         loss_history.append(loss2(theta2, X2, y2))
#         if len(loss_history) > 2:
#             if loss_history[itera-1] - loss_history[itera] < 1:
#                 break

#     plt.plot(range(len(loss_history)), loss_history)
#     plt.xlabel('iteration')
#     plt.ylabel('loss')
#     plt.show()
#     plt.clf()
#     return theta2
# theta2 = alg2()
# def f(x):
#     return theta2[0] + theta2[1] * x + theta2[2]*x*x

# plt.plot(X,y, X, [f(x) for x in X])
# plt.show()

X = [x for x,_ in S ]
y = [x for _,x in S ]

print(X,y)

plt.plot(X,y)
plt.xlabel('year')
plt.ylabel('activity')
plt.savefig('initial_data.png')
plt.clf()

def loss(theta, X, y):
    m = len(X)
    sum_loss = 0
    for i in range(m):
        hypothesis = theta[0] + theta[1] * X[i]
        sq_diff = (hypothesis - y[i])**2
        sum_loss += sq_diff
    return 1/(2*m) * sum_loss

def alg():
    m = len(X)
    theta = [random.randrange(-10,10,1), random.randrange(-10,10,1)]
    learning_rate = 0.03
    loss_history = []
    for itera in range(5000):
        d_dt0 = 0
        d_dt1 = 0
        for i in range(m):
            sum0 = (theta[0] + (theta[1] * X[i] )) - y[i]
            sum1 = ((theta[0] + (theta[1] * X[i] )) - y[i]) * X[i]
            d_dt0 += sum0
            d_dt1 += sum1

        d_dt0 *= 1/m 
        d_dt1 *= 1/m
        theta[0] = theta[0] - learning_rate * d_dt0
        theta[1] = theta[1] - learning_rate * d_dt1
        los = loss(theta, X, y)
        loss_history.append(los)
        if len(loss_history) > 2:
            if loss_history[itera-1] - loss_history[itera] < 0.001:
                break
    plt.plot(range(len(loss_history)), loss_history)
    plt.xlabel('iteration')
    plt.ylabel('loss')
    plt.savefig('loss_over_iteration.png')
    plt.clf()
    return loss_history, theta

loss_history, theta = alg()
def f(x):
    return theta[0] + theta[1]*x

plt.plot(X,y,X,[f(x) for x in X])
plt.xlabel('year')
plt.ylabel('acticity')
plt.savefig('hypothesis.png')

print(theta)
print(f"Strata w ostatnim kroku: {loss_history[-1]}")
