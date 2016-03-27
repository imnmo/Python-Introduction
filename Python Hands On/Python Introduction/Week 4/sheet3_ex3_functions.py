"""
Introduction to Python Programming
EXERCISE SHEET 3

Exercise 3:

(a) Iterative Fibonacci (4 Points)

Implement a non-recursive version of the function fib(n) from the lecture.
(Reminder: 0, 1, 1, 2, 3, 5, 8, 13, 21,...)
Compare runtimes for inputs 10, 20, 30, 35.
"""

def fibit(n):
    """ Returns the nth fib number.
    >>> fibit(0)
    0
    >>> fibit(1)
    1
    >>> fibit(2)
    1
    >>> fibit(3)
    2
    >>> fibit(10)
    55
    """
    seq = [0,1]
    i = 2
    while i<=n:
        seq.append(seq[i-1]+seq[i-2])
        i = i+1
    return seq[n]
    


"""
(b) Permutations (Bonus - not required, but a really good exercise)

Hints: 

perm('a') = ['a']
perm(string) = insert string[0] into all possible positions of all
permutations of rest of string

Helper functions see below.

"""

def perm(strng):
    """
    Implement a recursive function perm that computes all permutations of an input string,
    and output a list that contains the permutations sorted alphabetically.
    
    >>> perm('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    pass


# Some helper functions
def insert(strng, ch, i):
    """Returns a copy of strng with character ch inserted at index i"""
    return strng[:i] + ch + strng[i:]

def rest(strng):
    """
    Returns a copy of strng with the first character removed.
    rest("Hello") => 'ello'
    """
    return strng[1:]


if __name__ == "__main__":
    # This executes the tests
    # Comment out if you find the test output confusing
    import doctest
    doctest.testmod(verbose=True)
