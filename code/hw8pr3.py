#hw8pr3.py
#
#Name: Ashkon Aghassi

import random
import math

def throwDart():
    """
        Generates a random x and a random y coordinate between -1 and 1
        Determines whether that dart is within the circle of radius 1 centered at the origin
        Returns True if the dart hits the circle and False if the dart misses the circle
    """

    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    d = math.sqrt(x**2 + y**2)
    
    if d<1:
        return True
    else:
        return False

# def tester():
#     LC = [throwDart() for i in range(100)]
#     result = 0

#     for i in LC:
#         result += i
    
#     return result/100

def forPi(n):
    """
        Throw" n darts at the square.
        Each time a dart is thrown, the function should print:
            The number of darts thrown so far.
            The number of darts thrown so far that have hit the circle.
            The resulting estimate of π
        Returns: the final resulting estimate of π after n throws
    """
    attempts = 0
    hits = 0
    for i in range(n):
        attempts += 1
        if(throwDart()):
            hits += 1
        print(hits, 'hits out of' , attempts , 'thorws so that pi is ' , ((hits/attempts)*4))
    
    return ((hits/attempts) *4)

def whilePi(error):
    """
        Accepts: a positive floating-point value, error
        Throw darts at the dartboard (the square) until the absolute difference between 
        the function's estimate of π and the real value of π is less than error
        Returns: the number of darts thrown in order to reach the requested accuracy
    """

    actual = math.pi
    estimate = 0

    attempts = 0
    hits = 0
    while(abs(actual-estimate) > error):
        attempts += 1
        if(throwDart()):
            hits += 1
        estimate = (hits/attempts)*4
        print(hits, 'hits out of' , attempts , 'thorws so that pi is ' , ((hits/attempts)*4))
    return attempts
