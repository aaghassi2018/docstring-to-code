#hw4pr2
#Name: Ashkon Aghassi


def encipher(S, n):
    """ first argument: S is a string S
        second argument: n is a non-negative integer between 0 and 25

        encipher should return a new string in which the letters in S 
        have been "rotated" by n characters forward in the alphabet, 
        wrapping around as needed.
    """

    if(len(S) == 0):
        return S
    else:
        return rot(S[0],n) + encipher(S[1:], n)

def rot(c, n):
    """rotates c, a single character, forward by n spots in the alphabet
    """
    if 'a' <= c <= 'z':
        if ord(c)+n <= ord('z'):
            return chr(ord(c)+n)
        else:
            return chr(ord(c)+n-26)
    elif 'A' <= c <= 'Z':
        if ord(c)+n <= ord('Z'):
            return chr(ord(c)+n)
        else:
            return chr(ord(c)+n-26)
    else:
        return c


#I checked the probabilities of each of the letters in each of the possible encoding
#then found the one with the maximum probabilitiy and returned it. 
def decipher(S):
    """decipher returns, to the best of its ability, the original English string, 
        which will be some rotation (possibly 0) of the argument S
    """
    L = [encipher(S, n) for n in range(26)]
    LoL = [ [score(n), n] for n in L]

    bestPair = max(LoL)
    return bestPair[1]

def score(S):
    """score takes a string and returns a score using probability of each letter
    """

    X = [letProb(c) for c in S]
    Y = sum(X)
    return Y

def letProb(c):
    """If c is the space character or an alphabetic character,
       we return its monogram probability (for english),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

def blsort(L):
    """accept a list L and should return a list 
        with the same elements as L, but in ascending order
    """
    num0 = count(0,L)
    num1 = count(1,L)

    return num0*[0] + num1*[1]

def count(e,L):
    """return the number of times e occurs in L
    """

    LC = [1 for x in L if x == e]
    return sum(LC)

def gensort(L):
    """ accepts a list L and returns a list with the same 
        elements as L, but in ascending order
    """
    if(len(L) == 0):
        return L
    else:
        X = min(L)
        L1 = remOne(X, L)
        return [X] + gensort(L1)

def remOne (e,L):
    """removes the first e encountered in L
    """

    if len(L) == 0:
        return L
    elif L[0] != e:
        return L[0:1] + remOne(e, L[1:])
    else:
        return L[1:]

def jscore(S, T):
    """ accept two strings, S and T. Then, jscore returns the 
        "jotto score" of S compared with T
    """
    if(S == '' or T == ''):
        return 0
    elif (S[0] in T):
        x = remOne(S[0], T)
        return 1 + jscore(S[1:], x)
    else:
        return jscore(S[1:], T)

def exact_change(target_amount, L):
    """  argument target_amount is a single non-negative integer 
        and the argument L is a list of positive integers

        Returns either True or False: it should return True if it's possible to 
        create target_amount by adding up some—or all—of the values in L. It should 
        return False if it's not possible to create target_amount by adding up some 
         all of the values in L.
    """

    if target_amount == 0:
        return True
    elif target_amount < 0 or L ==[]:
        return False
    else:
        useIt = exact_change(target_amount- L[0], L[1:])

        if useIt == False:
            loseIt = exact_change(target_amount, L[1:])
        return  useIt or loseIt

def LCS(S, T):
    """ accept two strings, S and T
         return the longest common subsequence (LCS) that S and T share
    """
    if(S == '' or T == ''):
        return ''
    elif(len(S) == 0):
        return ''
    elif(S[0] == T[0]):
        return S[0] + LCS(S[1:], T[1:])
    else:
        x = len(LCS(S[0:], T[1:]))
        y = len(LCS(S[1:], T[0:]))

        if(x>y):
            return LCS(S[0:], T[1:])
        else: 
            return LCS(S[1:], T[0:])