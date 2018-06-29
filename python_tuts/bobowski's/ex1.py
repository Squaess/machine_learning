import time
from memory_profiler import memory_usage


def rec_factorial(n):
    """ This function will return the n-th value of factorial using
    recursion"""
    if n == 1:
        return 1
    return rec_factorial(n-1) * n


def iter_factorial(n):
    """This function will return value of n! using iteration"""
    score = 1
    for i in range(1, n+1):
        score *= i
    return score


def list_factorial(n):
    """Return the list containing the first n'th elements"""
    l1 = [1]
    for i in range (1, n+1):
        l1.append(l1[i-1] * i)
    l1.pop(0)
    return l1


def gen_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result


size = 10

usage = memory_usage((iter_factorial, (size,)))
print(max(usage))

usage = memory_usage((rec_factorial, (size,)))
print(max(usage))

for i in gen_factorial(size):
    print(i)

