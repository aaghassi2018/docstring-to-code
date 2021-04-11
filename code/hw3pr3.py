# CS 5 Gold, hw3pr3
# filename: hw3pr3.py
# Name: Ashkon Aghassi
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x//2) for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]
# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    """returns a list of evenly-spaced 
        left-hand endpoints (fractions) 
        in the unit interval [0, 1) given N number of times to 
        slice the interval[0,1)
    """
    return [x/N for x in range(N)]

assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(4) == [0.0, 0.25, 0.5, 0.75]
assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]

def scaledfracs(low, hi, N):
    """returns N left endpoints uniformly
        through the interval [low, hi)
    """

    return [low + (hi-low)*x for x in unitfracs(N)]

assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]

def sqfracs(low, hi, N):
    """sqfracs is very similar to scaledfracs except that each value is squared.
    """
    return [x**2 for x in scaledfracs(low,hi,N)]

assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]
assert sqfracs(0,20,4) == [0.0, 25.0, 100.0, 225.0]

def f_of_fracs(f, low, hi, N):
    """takes a function, low, hi, and N, and does the function
     on the result of scaledfracs
     """

    return [f(x) for x in scaledfracs(low,hi,N)]

assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0]

def integrate(f, low, hi, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """

    H = f_of_fracs(f, low, hi, N)


    return (sum(H))*((hi-low)/N)

assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])
assert integrate(sq, 0, 10, 2) == 125.0


def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5


"""
Q1.
The call integrate(dbl, 0, 10, 1000) will always underestimate the correct value
for that integral due to the fact that the number of times we slice the widths
a.k.a when we give N is not infininty. There is bound the be an overestimate or
underestimate of the integral due to the fact that we do not have infinite rectangles
to calculate the areas for.


Q2. 

integrate(c, 0 , 2, 200) = 3.151

integrate(c, 0, 2, 2000) = 3.142

As N goes to infinity integrate(c, 0, 2, 2000) the value becomes the value of pi.
This happens because just like Q1, the more number of times we slice the problem up,
the more accurate our answer will become. 

"""