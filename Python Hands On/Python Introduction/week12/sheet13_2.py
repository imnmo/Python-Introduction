#########################################
# Introduction to Python Programming    #
# Exercise Sheet 13                     #
# List Comprehensions                   #
#########################################

# Exercise 2

''' (2 Points) Write function "count" that takes a list of words as argument
and returns a list of word-frequency pairs. The function should use a list
comprehension.

Hint: Lists have a method count that returns the number of occurrences of the
argument in the list: [1, 1, 2, 1, 3].count(1) => 3
'''

def count(words):
    '''
    >>> count("Wenn Fliegen hinter fliegen fliegen fliegen Fliegen Fliegen nach".split())
    [('Wenn', 1), ('Fliegen', 3), ('hinter', 1), ('fliegen', 3), ('fliegen', 3), ('fliegen', 3), ('Fliegen', 3), ('Fliegen', 3), ('nach', 1)]
    '''
    m=[(i,words.count(i))for i in words]
    return m


# This automatically tests your code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
