# CS5, Lab2 part 2
# Filename: hw2pr2.py
# Name: Ashkon Aghassi
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Returns the square of its argument
        Argument x: a number (int of float)
    """
    return x*x

def interp(low, hi, fraction):
    """Arguments: three numbers: low, hi, and fraction.
        Return: the floating-point value that is fraction of the way between low and hi
    """
    return fraction*(hi-low) + low

def checkends(s):
    """Arguments: String s
        Returns: boolean, true if the first character of s is the same as the last character in s; false if otherwise. 
    """
    if(s[0:1] == s[len(s)-1:len(s)]):
        return True
    else:
        return False

def flipside(s):
    """Arguments: String, s
        Returns: A string whose first half is s's second half and whose second half is s's first half.
    """

    return s[(len(s))//2:len(s)] + s[0:len(s)//2]

def convertFromSeconds(s):
    """Arguments: Nonnegative integer s
        Returns: List L of four nonnegative integers that represents that number of seconds in more conventional units fo time
    """
    days = s // (24*60*60)  # Number of days
    s = s % (24*60*60)      # The leftover
    hours = s // (60*60)
    s = s % (60*60)
    minutes = s//60
    seconds = s % 60
    return [days, hours, minutes, seconds]