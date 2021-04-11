# CS5, hw2pr3
# Filename: hw2pr3.py
# Name: Ashkon Aghassi
# Problem description: Function Frenzy!
# Date Due: 2/4/19

#
# leng example from class
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])

def mult(n, m):
    """mult returns the product of its two arguments
       Arguments: n and m are both integers
       Return value: the result of multiplying n and m
    """
    if(m == 0):
        return 0
    elif m < 0:
        return - (n - mult(n, m+1))
    else:
        return n + mult(n, m-1)

def dot(L, K):
    """ dot returns the dot product of the lists L and K
        Arguments: Lists contain only numeric values.
        Return value:  the sum of the products of the elements in the same position
    """
    if(len(L) != len(K)):
        return 0.0
    elif(len(L) == 0 and len(K) == 0):
        return 0.0
    else:
        return (L[0] * K[0]) + dot(L[1:],K[1:])

def ind(e, L):
    """ ind will return the index at which e is first found in L
        Arguments: a sequence L and an element, L can be a string or list.
        Return value: return the index at which e is first found in L.
                       If e is NOT an element of L, ind(e,L) returns the length of L.
    """
    if(e not in L):
        return len(L)
    elif (e == L[0]):
        return 0
    else:
        return 1 + ind(e,L[1:])

def letterScore(let):
    """ letterScore will return the value of that character as a Scrabble tile.
        Arguments: a single-character string
        Return value: the value of that character as a Scrabble tile
    """
 
    if(let in 'aeilnorstu'):
        return 1
    elif(let in 'dg'):
        return 2
    elif(let in 'bcmp'):
        return 3
    elif(let in 'fhvyw'):
        return 4
    elif(let in 'k'):
        return 5
    elif(let in 'xj'):
        return 8
    elif(let in 'qz'):
        return 10
    else:
        return 0

def scrabbleScore(S):
    """ scrabbleScore will return the value of string S
        Arguments: a string argument S, which will have only lowercase letters
        Return value: the Scrabble score of string S
    """

    if(len(S) == 0):
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])


def one_dna_to_rna(c):
        """Converts a single-character c from DNA
           nucleotide to complementary RNA nucleotide 
        """
        if c == 'A':
            return 'U'
        elif c == 'C':
            return 'G'
        elif c == 'G':
            return 'C'
        elif c == 'T':
            return 'A'
        else: 
            return ''


def transcribe(S):
    """ Argument: a string S, which will have DNA nucleotides (capital letter As, Cs, Gs, and Ts)
        Return: the messenger RNA that would be produced from that string S
    """

    if(len(S) == 0):
        return ''
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])

# EXTRA CREDIT

#
# I finished all of the CodingBat STRING problems.
#

#
# I finished all of the CodingBat LIST problems.
#

