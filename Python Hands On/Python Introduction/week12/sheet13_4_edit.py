#########################################
# Introduction to Python Programming    #
# Exercise Sheet 13                     #
# List Comprehensions                   #
#########################################

# Exercise 4

''' (2 Points) Implement two versions of a function myfilter
that takes a function and a list as arguments, and returns
an iterator over all items in the list for which the function
returns True. 

'''

def isOdd(x):
    if x % 2 == 1:
        return True
    else:
        return False

def myfilter1(someFunction, iterable):

    for i in iterable:
        if isOdd(i)== True:
            yield i
            

k=list(myfilter1(isOdd, [1, 2, 3, 4, 5, 6, 7]))
print(k)

    





'''
    This function should be implemented as a generator function
    (i.e., using yield) 

    >>> list(myfilter1(isOdd, [1, 2, 3, 4, 5, 6, 7]))
    [1, 3, 5, 7]
    '''
    

def myfilter2(someFunction, iterable):

    x = ( i for i in iterable if someFunction(i) == True)
    return x


k=list(myfilter2(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]))
print(k)    


    
'''This function should be implemented using a generator expression.

    >>> list(myfilter2(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]))
    [2, 4, 6]
    '''
    
    

'''
# This automatically tests your code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True
    '''
