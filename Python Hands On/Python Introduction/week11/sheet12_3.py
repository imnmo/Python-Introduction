######################################
# Introduction to Python Programming #
# WS 2012/2013                       #
# Exercise Sheet 12                  #
# Iterators & Generators             #
######################################


'''
EXERCISE 3:

Implement an iterator that iterates over a file by paragraph.
By "paragraph" we mean all lines in the file which are not separated
by blank lines. (3 Points)'''

#class ByParagraph:
    #pass # your code
    

#with open("example.txt") as f:
    #for par in ByParagraph(f):
        #pass
        #print(par)


''' Implement the "ByParagraph" iterator as a generator function
(2 Points) '''

def byParagraph_generator(fileobject):
    for line in fileobject:
            line = line.rstrip()
            if line != '':
                    yield line

with open("example.txt") as f:
    for par in byParagraph_generator(f):
        print(par)
