import sys
import numpy as np
import pandas as pd

'''
Check if the arguments are properly passed to compute 
'''
if len(sys.argv) != 3:    
    sys.exit('Arguments are not sufficient')

'''
Try to cast velocity to integer and get the path to file
'''
try: 
    file_name = sys.argv[1]
    velocity = int(sys.argv[2])
except ValueError:
    sys.exit('Argument ' + sys.argv[2] + ' is not a natural number')


'''
Read the data from file as csv format.
We're useing pandas wich is great madule for 
managing data. We take only story_points and KSP
'''
df = pd.read_csv(file_name)
Data = df.iloc[:, 1:3].values

'''
n - quantity of tickets in the file
'''
n = len(Data)

'''
Array needed to computations.
We're using dynamic programming. 
The problem for finding the most
efficient tickets, can be divided into smaller one.
'''
K = np.zeros((velocity+1,n+1))

for j in range(1, n+1):
    for w in range(1,velocity+1):
        if Data[j-1][0] > w:
            K[w][j] = K[w][j-1]
        else:
            K[w][j] = max(K[w][j-1], K[w - Data[j-1][0] ][j-1] + Data[j-1][1] )


'''
We need to find the way back!!!
We look at the most right column, and the lowest row
If on the left is the same number, that means that we didn't add 
this particular ticket, if not we add this ticket, and we re looking 
for the previus one.
'''
result = []
row = velocity
for j in range(n, 0, -1):
    if K[row][j-1] !=  K[row][j]:
        result.append(j-1)
        row = row - Data[j-1][0]
result  = list(reversed(result))

'''
To be clear we print in the same format as asked.
'''
for i in range(len(result)-1):
    sys.stdout.write("{0}, ".format(result[i]))

sys.stdout.write(str(result[len(result)-1]))
