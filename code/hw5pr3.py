#
# hw5pr3.py
# Name: Ashkon Aghassi

from cs5png import *


def testBinaryImage():
    """Run this function to create an 8x8 alien image
       named binary.png
    """
    ALIEN = "0"*8 + "11011011"*2 + "0"*8 + "00001000" + \
            "01000010" + "01111110" + "0"*8
    # this function is imported from cs5png.py
    NUM_ROWS = 8
    NUM_COLS = 8
    binaryIm(ALIEN, NUM_COLS, NUM_ROWS)
    # that should create a file, binary.png, in this
    # directory with the 8x8 image...


def change(p):
    """Change accepts a pixel (an [R,G,B] list)
       and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [255 - red, 255 - green, 255 - blue]


def invert():
    """Run this function to read the in.png image,
       change it, and write the result to out.png.
    """
    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    #
    # Remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    #
    New_pix = [[change(p) for p in row] for row in Im_pix]
    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')
    
def greyscale():
    """Run this function to read the in.png image,
       change it to greyscale, and write the result to out.png.
    """
    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])
    #
    # Remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    #
    New_pix = [[greysclaeHelper(p) for p in row] for row in Im_pix]
    # now, save to the file 'out.png'
    saveRGB(New_pix, 'out.png')

def greysclaeHelper(p):
    """greyscaleHelper accepts a pixel (an [R,G,B] list)
       and returns a new greyscale  pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    
    x = int(0.21*red + 0.72*green + 0.07*blue)
    return [x,x,x]

def binarize(thresh):
    """
        Run this function to read the in.png image,
        change it to black and white (with a 
        threshold of thresh given by the user) and write the result to out.png.
    """

    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    New_pix = [[binarizeHelper(p,thresh) for p in row] for row in Im_pix]


    saveRGB(New_pix, 'out.png')

def binarizeHelper(p,thresh):
    """
        binarizeHelper accepts a pixel (an [R,G,B] list)
        and returns a new black or white  pixel to take its place depending on
        the thresh
    """

    if(p[0]>thresh):
        return [255,255,255]
    else:
        return [0,0,0]

def flipVert():
    """
        Run this function to read the in.png image,
        change it so the image is flipped on its horizontal axis
        and write the result to out.png.
    """

    Im_pix = getRGB('in.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    New_pix = Im_pix[::-1]


    saveRGB(New_pix, 'out.png')


def flipHoriz():
    """
        Run this function to read the in.png image,
        change it so the image is flipped on its vertical axis
        and write the result to out.png.
    """

    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    New_pix = [flipHorizHelper(row) for row in Im_pix]


    saveRGB(New_pix, 'out.png')

def flipHorizHelper(p):
    """
        flipVertHelper accepts a row (list of [R,G,B] lists)
        and returns a new row that has the items reveresed
    """

    return p[::-1]

def mirrorVert():
    """
        Run this function to read the in.png image,
        change it so Mirror the photo across its horizontal axis 
        (i.e., so that the top part is mirrored upside down on the 
        bottom of the image)
        and write the result to out.png.
    """

    Im_pix = getRGB('in.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    x = Im_pix[:len(Im_pix)//2]
    x = x[::-1]

    New_pix = Im_pix[:len(Im_pix)//2] + x

    saveRGB(New_pix, 'out.png')

def mirrorHoriz():
    """
        Run this function to read the in.png image,
        change it so Mirror the photo across its vertical axis 
        (i.e., so that it's the left half of the image plus the reveresed 
        left side of the image)
        and write the result to out.png.
    """

    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    New_pix = [row[:len(row)//2] + row[len(row)//2::-1] for row in Im_pix]

    saveRGB(New_pix, 'out.png')


def scale():
    """
        Run this function to read the in.png image,
        Scale the image to half of each of its original dimensions 
        (this will be a quarter of its original area)
        and write the result to out.png.
    """

    Im_pix = getRGB('spam.png')  # read in the in.png image
    print("The first two pixels of the first row are", Im_pix[0][0:2])

    x = [scaleHelper(row) for row in Im_pix]

    New_pix = scaleHelper2(x)

    saveRGB(New_pix, 'out.png')

def scaleHelper(L):
    """
        scaleHelper accepts a row (list of [R,G,B] lists)
        and returns a new row that eliminates every other list in each row
    """
    if len(L) == 0 :
        return []
    elif len(L)%2 == 0:
        return [L[0]] + scaleHelper(L[1:])
    else:
        return scaleHelper(L[1:])

def scaleHelper2(L):
    """
    scaleHelper accepts the pixels (list of [R,G,B] lists)
    and returns a list of lists that eliminates every other row
    """

    if len(L) == 0 :
        return []
    elif len(L)%2 == 0:
        return [L[0]] + scaleHelper(L[1:])
    else:
        return scaleHelper(L[1:])
