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
    

    
    n = a.count(1)
    m = a.count(2)
    o = a.count(3)
    p = a.count(4)


    points = {}
    points[1] = n
    points[2]=m
    points[3] =o
    points[4]=p
    print('hello')
    print(points)
    print (points.items())

"""
b) Implement the above function such that it returns a list of tuples
   (key, value). The returned list of tuples is supposed to be sorted
   by the second element of the tuples (= by how often the values
   occur in the dictionary).
"""

def countElements2(myList):
    """
    Remove the 'pass' statement and write your own code.

    >>> countElements2([4, 1, 3, 2, 1, 2, 2, 3, 3, 3])
    [(3, 4), (2, 3), (1, 2), (4, 1)]
    """
    #This Below usage of sorting was refered 
#    Sorted_countelemnt = tuple(sorted(points.items(), key=lambda item: item[1],reverse=True))#based on item[1] sorting is done#Reverse-do sorting on reverse order.
#    print (Sorted_countelemnt)

if __name__ == "__main__":
    # This executes the tests
    # Comment out if you find the test output confusing
    import doctest
    doctest.testmod(verbose=True)
