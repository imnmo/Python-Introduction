######################################
# Introduction to Python Programming #
# WS 2012/2013                       #
# Exercise Sheet 12                  #
# Iterators & Generators             #
######################################

'''
EXERCISE 2:

As we have seen in the lecture, len() cannot be applied to iterators, as
they return one value at a time, not knowing how many will follow. This is
actually an advantage when working with large data files, as it saves
memory (the file can be loaded in to memory just line by line, not all
at once).

However, we cannot ask Python for the length of an iterator (try out the
following counter-example using the shell):

myIter = iter([1, 2, 3]) # creating an iterator for the sequence (list)
len(myIter) # will give you an error
sum(myIter) # will give you an error

The following function computes the average of a sequence of numbers:

def avg(sequence):
    return sum(sequence) / len(sequence)

It doesn't work for iterators.

Reimplement the avg function so that it can be applied to iterators.

(3 points)

'''


def avg(iterable):
    l=[]
    s=[]
    for (i,ele) in enumerate(iterable):
        l.append(i)
        s.append(ele)
    sumit=sum(s)
    lenit=len(l)
    return (sumit/lenit)
    


# Testing

myIter = iter([32, 5, 2, 75])
print(avg(myIter))
