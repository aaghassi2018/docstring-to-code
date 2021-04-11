#
# hw9pr2.py
#
# Name: Ashkon Aghassi
#

# here is a function for printing 2D arrays
#  (lists-of-lists) of data

def print2d(A):
    """print2d prints a 2D array, A
       as rows and columns
       Argument: A, a 2D list of lists
       Result: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR):      # NR = =numrows
        for c in range(NC):  # NC == numcols
            print(A[r][c], end = ' ')
        print()

    return None  # this is implied anyway,
    # when no return statement is present

# some tests for print2d
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
print("2-row, 3-col A is")
print2d(A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
print("4-row, 2-col A is")
print2d(A)


# create a 2D array from a 1D string
def createA(NR, NC, s):
    """Returns a 2D array with
       NR rows (numrows) and
       NC cols (numcols)
       using the data from s: across the
       first row, then the second, etc.
       We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [s[0]] # add that char
            s = s[1:]        # get rid of that first char
        A += [newrow]
    return A

# a couple of tests for createA:
A = [['X', ' ', 'O'], ['O', 'X', 'O']]
newA = createA(2, 3, 'X OOXO')
assert newA == A
print("Is newA == A? Should be True:", newA == A)

A = [['X', 'O'], [' ', 'X'], ['O', 'O'], ['O', 'X']]
newA = createA(4, 2, 'XO XOOOX')
assert newA == A

def inarow_3east(ch, r_start, c_start, A):
    """
    start from r_start and c_start and check for 
    three-in-a-row eastward of element ch, returning 
    True or False, as appropriate
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - 3:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(3):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_3south(ch, r_start, c_start, A):
    """
    start from r_start and c_start and check for three-in-a-row southward of 
    element ch, returning True or False, as appropriate
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - 3:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(3):                  # loop index i as needed
        if A[r_start+i][c_start] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_3southeast(ch, r_start, c_start, A):
    """
    start from r_start and c_start and check for three-in-a-row southeastward 
    of element ch, returning True or False, as appropriate
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - 3:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(3):                  # loop index i as needed
        if A[r_start+i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_3northeast(ch, r_start, c_start, A):
    """
    start from r_start and c_start and check for three-in-a-row 
    northeastward of element ch, returning True or False, as appropriate
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - 3:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(3):                  # loop index i as needed
        if A[r_start-i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_Neast(ch, r_start, c_start, A, N):
    """
    start from r_start and c_start and check for N-in-a-row eastward of 
    element ch, returning True or False, as appropriate.
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """
    start from r_start and c_start and check for N-in-a-row southward of 
    element ch, returning True or False, as appropriate.
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """
    start from r_start and c_start and check for N-in-a-row 
    southeastward of element ch, returning True or False, as appropriate.
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start+i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """
    start from r_start and c_start and check for N-in-a-row 
    northeastward of element ch, returning True or False, as appropriate.
    """

    NR = len(A)      # number of rows is len(A)
    NC = len(A[0])   # number of cols is len(A[0])

    if r_start >= NR:
        return False # out of bounds in rows

    # other out-of-bounds checks...
    if c_start > NC - N:
        return False # out of bounds in cols

    # are all of the data elements correct?
    for i in range(N):                  # loop index i as needed
        if A[r_start-i][c_start+i] != ch: # check for mismatches
            return False                # mismatch found--return False

    return True                         # loop found no mismatches--return True

