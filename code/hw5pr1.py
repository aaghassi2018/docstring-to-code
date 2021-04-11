# CS5 Gold, hw5pr1
# Filename: hw5pr1.py
# Name: 
# Problem description: Binary <-> decimal conversions

def isOdd(N):
    if(N%2 == 0):
        return False
    else:
        return True

def numToBinary(N):
    """
    argument: a number in base 10
    returns: the same number in base 2 (binary)
    """
    if N == 0:
        return ''
    elif N%2 == 1:
        return   numToBinary(N//2) + '1'
    else:
        return   numToBinary(N//2) + '0'

def binaryToNum(S):
    """
    argument: a number in base 2
    returns: the same number in base 10
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return   2*(binaryToNum(S[0:len(S)-1])) + 1

    else: # last digit must be '0'
        return   2*(binaryToNum(S[0:len(S)-1])) + 0

def increment(S):
    """
    argument: 8-character string S of 0's and 1's 
    returns: the next largest number in base 2
    """

    if('0' in S) == False:
        return len(S)*'0'
    
    n = binaryToNum(S)
    x = n + 1
    y = numToBinary(x)

    return (('0'*(len(S)-len(y))) + y)

def count(S, n):
    """
    arguments: 8 character binary string
    returns: n times upward from S, printing as it goes
    """

    if(n == -1):
        return 
    else:
        print(S)
        return count(increment(S), n-1)

""" 59 is tertiary is 2*27 + 0*9 + 1*3 + 2*1
    so 2012 in base 3
"""

def numToTernary(N):
    """
    argument: a number in base 10
    returns: a ternary string representing the value of the argument N
    """
    if N == 0:
        return ''
    elif N%3 == 2:
        return   numToTernary(N//3) + '2'
    elif N%3 == 1:
        return   numToTernary(N//3) + '1'
    else:
        return   numToTernary(N//3) + '0'

def ternaryToNum(S):
    """
    argument: a number in base 3
    returns: a number in base 10 representing the value of argument S
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        return   3*(ternaryToNum(S[0:len(S)-1])) + 1
    elif S[-1] ==  '2':
        return   3*(ternaryToNum(S[0:len(S)-1])) + 2
    else: # last digit must be '0'
        return   3*(ternaryToNum(S[0:len(S)-1])) + 0

def balancedTernaryToNum(S):
    """
    arguments: the balanced ternary string S
    returns: the decimal value equivalent 
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '+':
        return   3*(balancedTernaryToNum(S[0:len(S)-1])) + 1
    elif S[-1] ==  '-':
        return   3*(balancedTernaryToNum(S[0:len(S)-1])) - 1
    else: # last digit must be '0'
        return   3*(balancedTernaryToNum(S[0:len(S)-1])) + 0

def numToBalancedTernary(N):
    """
    arguments: a number in base 10
    returns: a balanced ternary string representing the value of the argument N
    """

    if N == 0:
        return ''
    elif N%3 == 2:
        return   numToBalancedTernary((N+3)//3) + '-'
    elif N%3 == 1:
        return   numToBalancedTernary(N//3) + '+'
    else:
        return   numToBalancedTernary(N//3) + '0'