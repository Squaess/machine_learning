from math import pi
import random

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError('Wrong type.')
    if r < 0:
        raise ValueError('Negative value.')
    return pi*(r**2)

# Szybkie sprawdzenie składanych list
liczby = [ (random.random()*100 - 50) for x in range(0,10)]
print(liczby)
nowa = [ int(round(x)) for x in liczby if not x < 0]
print(nowa)
with open('test_circle.py', 'r') as f:
    print(f.read())