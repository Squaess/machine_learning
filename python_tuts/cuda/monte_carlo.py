import numpy as np
import random
from timeit import default_timer as time

#function to count 
def function(x):
    return -x**2+1

ts = time()
#number of iteration
N = 10000000

#number of correct guessed values
k = 0

values = [(random.random(), random.random()) for i in range(N)]

for x, y in values:
    if(function(x) > y):
        k = k + 1
P = 1*k/N
te = time()
total_time = (te - ts)
print("For the function -x**2 + 1 we shoot {0} and {1} where correct".format(N, k))
print("Area is equal to {0}".format(P))
print("It took: {second}".format(second=total_time))