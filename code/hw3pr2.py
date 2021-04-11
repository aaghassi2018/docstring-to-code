# CS5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name: Ashkon Aghassi
# Problem description: Sleepwalking student

import random  
import time
import sys

sys.setrecursionlimit(50000)

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    """Arguments: An integer, start, representing the starting position of our sleepwalker, and
                  A nonnegative integer, nsteps, representing the number of random steps to take from this starting position. 
        Return Value: the position of the sleepwalker after nsteps randoms teps where each step moves accroding to rs() (either plus 1 ore minus 1 from the previous position)
    """

    if(nsteps == 0):
        print('start is ' , start)
        return start
    else:
        print('start is ' , start)
        return rwpos(start+rs(), nsteps-1)

def rwsteps(start, low, hi):
    """Arguments: An integer, start, representing the starting position of our sleepwalker
                  An integer, low, which will always be nonnegative, representing the smallest value our sleepwalker will be allowed to wander to, and
                  An integer, hi, representing the highest value our sleepwalker will be allowed to wander to.
        Return value: the number of steps that the sleepwalker took in order to finally reach the lower or upper bound.
    """

    sys.stdout.flush()   # forces Python to print everything _now_
    time.sleep(0.15)      # and then sleep for 0.1 seconds

    if(start < low):
        return 0
    elif(start > hi):
        return 0
    else:
        step = rs()
        if(step == 1):
            print('|',(start-low)*'_','>-<-0',(hi-start)*'_','|')
            return 1 + rwsteps(start+step,low,hi)
        else:
            print('|',(start-low)*'_','0->-<',(hi-start)*'_','|')
            return 1 + rwsteps(start+step,low,hi)

""" Check out the extra credit on the ASCII emoji I created AND the 
    fact that it changes depending on whether it's moving left or right.
"""


def rwposPlain(start, nsteps):
    """Arguments: An integer, start, representing the starting position of our sleepwalker, and
                  A nonnegative integer, nsteps, representing the number of random steps to take from this starting position. 
        Return Value: the difference in position of the sleepwalker after nsteps random steps where each step moves accroding to rs() (either plus 1 ore minus 1 from the previous position)
    """
    step = rs()
    if(nsteps == 0):
        return 0
    else:
        return step + rwposPlain(start+step, nsteps-1)


def ave_signed_displacement(numtrials):
    """Arguments: number of times we  run rwposPlain(0,100)
        Return Value: the average of the result of rwposPlain(0,100)
    """

    LC = [rwposPlain(0, 100) for x in range(numtrials)]
    return sum(LC)/len(LC)

def ave_squared_displacement(numtrials):
    """Arguments: number of times we should run rwposPlain(0,100)
        Return Value: the squared average of the result of rwposPlain(0,100)
    """

    LC = [rwposPlain(0, 100) for x in range(numtrials)]
    LC2 = [2**x for x in LC]

    return sum(LC2)/len(LC2)

"""
     To compute the average signed displacement for
     a random walker after 100 random steps, I wrote
     a list comprehension for every x in range(numtrials)
     which would be sure that it runs what I put in the first
     part of the list comprehension numtrials times. For the 
     first part of the list comprehension, I called rwposPlain(0,100)
     which would return the difference in position of the sleepwalker 
     after 100 random steps where each step moves accroding to rs() 
     (either plus 1 ore minus 1 from the previous position).

     Then I divided the sum of all the items in LC and divided that by the length,
     giving the average average final signed displacement for a random walker after 
     making 100 random steps.


    On one ocasion, ave_signed_displacement(1000) returned 0.636, 
    while on one ocasion, ave_squared_displacement(1000) returned 218231.549.

    Every time the average displacement was run, the number resulted was 
    somewhere around 0, but the squared average displacement was much much larger
    and a lot more varied. 
"""
