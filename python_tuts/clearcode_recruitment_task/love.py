import sys

def initialize(array):
    print(len(array))

def drawHeart(arguments):
    width = arguments[0]
    top_height = arguments[1]
    mid_height = arguments[2]
    bottom_height = arguments[3]

    array = [[0 for x in range(9*width)] for y in range(7*top_height + 1*mid_height + 7*bottom_height)]

    for i in array:
        print(i)

    initialize(array)

'''
Check if the arguments are properly passed to compute 
'''
arguments = []

if len(sys.argv) != 5:    
    sys.exit('Arguments are not sufficient')

for s in range(1, len(sys.argv)):
    try: 
        arg = int(sys.argv[s])
        arguments.append(arg)
    except ValueError:
        sys.exit('Arguments ' + sys.argv[s] + ' is not a natural number')

drawHeart(arguments)