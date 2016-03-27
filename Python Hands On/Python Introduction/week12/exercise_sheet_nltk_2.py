from __future__ import division

#####################################################
# Introduction to Python Programming WS 2012/2013   #
# Exercise Sheet NLTK                               #
#####################################################

"""
Name: <Mohamed Imran>
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Exercise 2: Lexical Diversity (4 points)          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
a)  The lexical diversity of a text can be defined as the
    number of tokens of the text divided by the number of
    distinct tokens of the text. Write a function which
    takes a Text object (= which behaves like a list of words
    here) as input and returns a number indicating the
    lexical diversity of the text.
    
b)  If text A has a higher lexical diversity value than
    text B, is it more or less lexically diverse than text B?
    
c)  The function brownLexicalDiversity is supposed to compute
    the lexical diversity value for each category
    of the Brown corpus. It has to return a list of tuples,
    where the first item of each tuple is a genre, and the
    second item of the tuple is its lexical diversity value.
    The returned list has to be sorted such that the most
    lexically diverse genre comes first. You don't need to
    lowercase or preprocess the words in any other way.
    
'''

#Import itemgetter (for sorting dict by values)
from operator import itemgetter
from nltk.corpus import brown

def lexicalDiversity(text):
    return len(text) / len(set(text))

def brownLexicalDiversity():
    genre = brown.categories()
    tup = [ ( i, len(i)/len(set(i)) ) for i in genre]
    sort_tup = tuple(sorted(tup, key=itemgetter(1),reverse=True))
    return sort_tup 
    



if __name__ == '__main__':
    brownLexicalDiversity()
