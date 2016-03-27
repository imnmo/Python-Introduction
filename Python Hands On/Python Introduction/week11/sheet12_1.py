######################################
# Introduction to Python Programming #
# WS 2012/2013                       #
# Exercise Sheet 12                  #
# Iterators & Generators             #
######################################

''' Hint: If you are not sure yet how iterators and generators
work, how they differ and what they have in common, we suggest
you have a look at the following article:
http://zetcode.com/lang/python/itergener/'''


'''
EXERCISE 1

Reimplement the builtin function enumerate as a generator function.
The function returns an iterator such that each call of "next" returns
a pair (tuple) containing the count (starting from 0) and the value
obtained from iterating over the sequence the function is applied to.
(3 points)
'''

def myEnumerate(iterable):
     for i in range(len(iterable)):
        yield i, iterable[i]
    


for (i, ch) in myEnumerate("Python"):
    print(i, ch)

# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

