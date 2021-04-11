#
# hw9pr1.py - Game of Life lab
#
# Name: Ashkon Aghassi
#

import random
from copy import deepcopy

def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]        # use the above function so that SOMETHING is one row!!
    return A

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:               # row is the whole row
        print()
        for col in row:         # col is the individual element
            print(col, end='')  # print that element


def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(width, height):
    """
    returns a 2D array that has all live cells—with a value of 
    1—except for a one-cell-wide border of empty cells (with the 
    value of 0) around the edge of the 2D array
    """

    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if col == width or row == height:
                A[row][col] = 0
            else:
                A[row][col] = 1

    return A

def randomCells(width, height):
    """
     returns an array of randomly-assigned 1's and 0's except that the 
     outer edge of the array is still completely empty (all 0's) as in 
     the case of innerCells
    """

    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if col == width or row == height:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0, 1])

    return A

def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = A[row][col]

    return newA

def innerReverse(A):
    """should return the "opposite" of A's cells everywhere except on the 
    outer edge.
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if col == width or row == height:
                A[row][col] = 0
            elif A[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = 0
                
    return newA

def countNeighbors(row, col, A):
    """
    should return the number of live neighbors for a 
    cell in the board A at a particular row and col
    """
    sum  = 0
    if A[row-1][col] == 1:
        sum += 1
    if A[row-1][col+1] == 1:
        sum += 1
    if A[row][col+1] == 1:
        sum += 1
    if A[row+1][col+1] == 1:
        sum += 1
    if A[row+1][col] == 1:
        sum += 1
    if A[row+1][col-1] == 1:
        sum += 1
    if A[row][col-1] == 1:
        sum += 1
    if A[row-1][col-1] == 1:
        sum += 1
    
    return sum

def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """

    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if col == width or row == height:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif (countNeighbors(row, col, A) > 3):
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]

                
    return newA