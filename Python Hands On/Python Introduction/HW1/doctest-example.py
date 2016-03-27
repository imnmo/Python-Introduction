# Doctest example

def isEven(x):
    """ This is the docstring of the isEven function.
        The function is supposed to tell whether x is
        even or not. In this case, it's implemented
        correctly. We can just give a few examples here,
        that doctest will use to check our implementation.
        If the output given in the examples is not
        matched by the actual output, doctest will complain.
        
        >>> isEven(6)
        True
        >>> isEven(7)
        False
    """
    if x%2 == 0:
        return True
    else:
        return False


def isOdd(x):
    """ This implementation contains an error.
        Doctest will tell us about it.
        
        >>> isOdd(6)
        False
        >>> isOdd(7)
        True
    """
    if x%2 == 0:
        return False
    else:
        return True



if __name__ == "__main__":
    # This executes the tests
    import doctest
    doctest.testmod(verbose=True)
