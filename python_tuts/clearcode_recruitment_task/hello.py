import sys

def drawTop( width, height):
    for x in range(0, height):
        for i in range (0, width):
            sys.stdout.write('..')
        for i in range(0, width):
            sys.stdout.write('#'),
        for i in range(0, width):
            sys.stdout.write('...'),
        for i in range(0, width):
            sys.stdout.write('#'),
        for i in range(0, width):
            sys.stdout.write('..')
        sys.stdout.write('\n')
    
    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('###')
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('###')
        for i in range(0, width):
            sys.stdout.write('.')
        sys.stdout.write('\n')

    for j in range(0,3):
        for x in range(0, height):
            for i in range(0, width):
                sys.stdout.write("#########")
            sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('##')
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('###')
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('##')
        sys.stdout.write('\n')

    for x in range(0,height):
        for i in range(0,width):
            sys.stdout.write('##')
        for i in range(0, width):
            sys.stdout.write('..')
        for i in range(0,width):
            sys.stdout.write('#')
        for i in range(0, width):
            sys.stdout.write('..')
        for i in range(0,width):
            sys.stdout.write('##')
        sys.stdout.write('\n')
    
    for x in range(0,height):
        for i in range(0,width):
            sys.stdout.write('##')
        for i in range(0, width):
            sys.stdout.write('.....')
        for i in range(0,width):
            sys.stdout.write('##')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('###')
        for i in range(0, width):
            sys.stdout.write('...')
        for i in range(0, width):
            sys.stdout.write('###')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('####')
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('####')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('#########')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('.')
        for i in range(0, width):
            sys.stdout.write('#######')
        for i in range(0, width):
            sys.stdout.write('.')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('..')
        for i in range(0, width):
            sys.stdout.write('#####')
        for i in range(0, width):
            sys.stdout.write('..')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('...')
        for i in range(0, width):
            sys.stdout.write('###')
        for i in range(0, width):
            sys.stdout.write('...')
        sys.stdout.write('\n')

    for x in range(0, height):
        for i in range(0, width):
            sys.stdout.write('....')
        for i in range(0, width):
            sys.stdout.write('#')
        for i in range(0, width):
            sys.stdout.write('....')
        sys.stdout.write('\n')

def drawMiddle( width, height):
    pass

def drawBottom( width, height):
    pass

def drawHeart( argument_list ):
    drawTop(argument_list[0], argument_list[1])
    drawMiddle(argument_list[0], argument_list[2])
    drawBottom(argument_list[0], argument_list[3])


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