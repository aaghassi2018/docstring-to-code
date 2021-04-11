#coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
#
# Name: Ashkon Aghassi
#
#


# function #1
#

import fileinput
import random

def createDictionary(filename):
    """
     It should return a dictionary whose keys are words encountered in the 
     text file and whose entries are a list of words that may legally follow
    the key word
    """
    f = open(filename)
    text = f.read()
    f.close()

    LoW = text.split()

    d = {}
    pw = '$'


    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]

        pw = nw
        if pw[-1] == '.' or pw[-1] == '?' or pw[-1] == '!':
            pw = '$'
    
    return d




# function #2
#
def generateText(d, N):
    """ 
        will take in a dictionary of word transitions d (generated in your 
        createDictionary function, above) and a positive integer, n. Then, 
        generateText should print a string of n words
    """

    text = random.choice(d['$'])
    pw = text

    for i in range(N):
        word = random.choice(d[pw])
        text += ' ' + word
        pw = word
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
                pw = '$'


    return text




#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
"""

An essay I'm working on for a writing class... Author: Ashkon Aghassi

There are unable to comprehend a story is once again awfully unusual. Settings establish a particular setting raises questions for this fundamental 
component to be interested or city, they will be omitted. For example, the the crime ahead of any story is discussed a large part in literature. This 
makes each reader’s comprehension of specific setting for the general setting is without a great deal. The Glass Key where the reader is another reader
will say that of any story because their previous experiences with it. The Glass Key, it because they may be interested or engaged with it. When the story.
The Glass Key takes place into the story because of its residents are unfamiliar with. To begin to visualize the city’s government of its familiarity. In The
implications of omitting a small town like Claremont, California may believe that the general purpose of the city and its familiarity. In a setting in 
literature. In a couple. Many will be omitted. In a setting of the plot takes place, heavily discussed, the reader’s comprehension of any story like the 
same setting or city, they will say that the novel, and regulations. Fundamentally, a name. By naming a setting of omitting a great deal. These are able 
to its familiarity. New York is in the setting plays a great deal. This makes each reader’s comprehension of rules and not the government of a setting, 
though, is clear that vary from reader to have a setting works alongside the novel, one reader to identify one. Because readers may allow certain initiatives 
that it effectively forces the government while another reason for this fundamental elements to insert their story’s characters are unable to visualize the 
plot. There are unable to comprehend a big government is unknown, In a variety of omitting a story is inefficient due to interpret the city like Claremont, 
California. In a setting in a variety of large city in his readers may believe that a novel is unknown, In a setting is impossible to visualize the novel. 
In a name. Because readers to Hammett’s desire to have a setting works alongside the government of a variety of the novel, one discussing the novel. One of
the novel in the same setting raises questions for the reader is forced to be a specific setting or city, they are able to make judgements on organizations 
like Claremont, California. There are able to the reader to solve the story. Each reader to the government from reader to identify one. These are heavily 
discussed, the novel, one reader to the reader’s understanding of having a large city in his novel, the story is a novel in government of the novel. Many will 
say that there is clear that vary from having a setting establishes context by sometimes providing a setting raises questions for the reader will become more
engaged with the other hand, a couple. Although not having a relatively bureaucratic government: one must be a setting or city, they aren’t forced to

"""
#
#