import time
import numpy as np
import random 

ts = time.time()

W = 13
n = 15000
K = np.zeros((W+1,n+1))

Data = np.zeros((n, 2))
Data = np.array([[ random.randrange(1, 7, 1), random.randrange(1, 20, 1) ] for _ in range(n)])


for j in range(1, n+1):
    for w in range(1,W+1):
        if Data[j-1][0] > w:
            K[w][j] = K[w][j-1]
        else:
            K[w][j] = max(K[w][j-1], K[w - Data[j-1][0] ][j-1] + Data[j-1][1] )

print(Data)
print(K)
te = time.time()
print(te-ts)

#printing the solution
result = []
row = W
for j in range(n, 0, -1):
    if K[row][j-1] !=  K[row][j]:
        result.append(j-1)
        row = row - Data[j-1][0]
result  = list(reversed(result))
print(result)
suma1 = 0
suma2 = 0
for i in result:
    print("{0} ticket zabiera {1} siły a zyskujemy {2} wiedzy.".format(i, Data[i][0], Data[i][1]))
    suma1 += Data[i][1]
    suma2 += Data[i][0]

print("Wykorzystaliśmy {0} siły, a zyskaliśmy {1} wiedzy".format(suma2, suma1))


