"""
Introduction to Python Programming
EXERCISE SHEET 3

Exercise 1: Lists (4 points)

a) Write a function countElements(myList) that takes a list
   as its parameter and that counts for each element of the
   list how often it occurs in the list. The return value of
   the function is supposed to be a dictionary whose keys are
   the elements of the list and whose values are integers
   indicating how often each element occurs in the list. 
"""

def countElements(myList):
    """
    Remove the 'pass' statement (which stands for 'do nothing')
    and write your own code.

    Example code:
    >>> countElements([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
    {1: 2, 2: 3, 3: 4, 4: 1}
   """
   
    n = mylist.count(1)
    m = mylist.count(2)
    o = mylist.count(3)
    p = mylist.count(4)


    
    mylist[1] = n
    mylist[2]=m
    mylist[3] = o
    mylist[4]=p
    return mylist
"""
b) Implement the above function such that it returns a list of tuples
   (key, value). The returned list of tuples is supposed to be sorted
   by the second element of the tuples (= by how often the values
   occur in the dictionary).
"""

#def countElements2(myList):
#    """
#    Remove the 'pass' statement and write your own code.

#    >>> countElements2([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
#    [(3, 4), (2, 3), (1, 2), (4, 1)]
#    """
#    pass


if __name__ == "__main__":
    # This executes the tests
    # Comment out if you find the test output confusing
    import doctest
    doctest.testmod(verbose=True)
