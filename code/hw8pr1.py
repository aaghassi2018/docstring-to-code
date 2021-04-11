# hw8pr1.py
# Lab 8
#
# Name: Ashkon Aghassi
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:   
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#


def mult(c, n):
    """Mult uses only a loop and addition
       to multiply c by the positive integer n
    """
    result = 0
    for i in range(n):
        result += c

    return result

assert mult(3, 5) == 15

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    i = 0
    while(i < n):
        z = z**2 + c
        i += 1
    return z

def inMSet(c, n):

    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
       Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0
    i = 0
    while(i < n):
        z = z**2 + c
        i += 1
        if(abs(z) > 2.0):
            return False
    return True


def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  and  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """

    # The original code creates the point when both the column and row are divisible by 10.
    # the alternative if statement creates a piont when either the column or the row is divisible by 10,
    # it ends up creating lines...

    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row)
           pixMax, the total # of pixel columns
           floatMin, the min floating-point value
           floatMax, the max floating-point value
       scale returns the floating-point value that
           corresponds to pix
    """
   
    return (pix/pixMax)*(floatMax-floatMin) + floatMin

def mset():
    """Creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    NUMITER = 50  # of updates, from above
    XMIN = -1.2   # the smallest real coordinate value
    XMAX =  -.6   # the largest real coordinate value
    YMIN = .5   # the smallest imag coordinate value
    YMAX = .1   # the largest imag coordinate value
        # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            # x = scale( ..., ..., ..., ...)
            #   once to create the imaginary part of c (y)
            # y = scale( ..., ..., ..., ...)
            # THEN, create c, choose n, and test:

            x = scale(col, width, XMIN, XMAX)
            y = scale(row, height, YMIN, YMAX)

            c = x + y*1j
            n = NUMITER
            if inMSet(c, n):
                image.plotPoint(col, row, (255,255,0))
            else:
                image.plotPoint(col,row, (0, 0, 0))

    # we looped through every image pixel; we now write the file
    image.saveFile()