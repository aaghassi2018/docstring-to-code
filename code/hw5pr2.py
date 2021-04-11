# CS5 Gold, hw5pr2
# Filename: hw5pr2.py
# Name: Ashkon Aghassi

def numToBaseB(N, B):
    """ 
    arguments: non-negative integer N and a base B (between 2 and 10 inclusive)
    returns: a string representing the number N in base B.
    """

    if N == 0:
        return ''
    else:
        return numToBaseB(N//B, B) + str(N%B)

assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'

def  baseBToNum(S, B):
    """
    arguemnts: a string S and a base B where S represents a number in base B where 
                B is between 2 and 10 inclusive
    returns: an integer in base 10 representing the same number as S.
    """

    if S == '':
        return 0
    else: 
        return B*(baseBToNum(S[0:len(S)-1],B)) + int(S[-1])

def baseToBase(B1, B2, s_in_B1):
    """
    three arguments: a base B1, a base B2 (both of which are between 2 and 10, inclusive)
                     and s_in_B1, which is a string representing a number in base B1.
    returns: a string representing the same number in base B2.
    """

    x = baseBToNum(s_in_B1, B1)

    return numToBaseB(x, B2)

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'

def  add(S, T):
    """
    arguments:  two binary strings S and T 
    returns:    their sum, also in binary.
    """

    x = baseBToNum(S, 2)
    y = baseBToNum(T, 2)

    return numToBaseB(x+y, 2)

def addB(S, T):
    """
    arguments:  two binary strings S and T 
    returns:    their sum, also in binary.
    """

    if S=='':
        return T
    elif T=='':
        return S
    elif S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'
    elif S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    elif S[-1] == '1' and T[-1] == '1':
        return addB(addB(S[:-1], '1') , T[:-1]) + '0'

assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'

def compress(S):
    """
    argument: a binary string S of length less than or equal to 64
    returns: another binary string that is a run-length encoding of the original
    """

    if len(S) == 0:
        return ''
    else:
        nums = str(numToBinary(frontNum(S)))
        x = (7-len(str(nums)))*'0' + nums

        return S[0] + x + compress(S[frontNum(S):])

def frontNum(S):
    """
    argument: a string S
    returns: the number of times the first element of the input S appears
             consecutively at the start of S
    """
    if len(S) <= 1:
        return 1
    elif S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1

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


def uncompress(S):
    """
    argument: a binary string S  that is a run-length encoding
    returns: another binary string that is a decompressed version of S
    """

    if len(S) == 0:
        return ''
    else:
        return S[0] * binaryToNum(S[1:8]) + uncompress(S[8:])


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


assert compress(64*'0') == '01000000'
assert compress('11111') == '10000101'
Stripes = '0'*16 + '1'*16 + '0'*16 + '1'*16
assert compress(Stripes) == '00010000100100000001000010010000'

assert uncompress(compress(64*'0')) == 64*'0'
assert uncompress('10000101') == '11111'
assert uncompress('00010000100100000001000010010000') == '0000000000000000111111111111111100000000000000001111111111111111'