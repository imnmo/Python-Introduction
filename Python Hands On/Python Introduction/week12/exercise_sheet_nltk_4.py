from __future__ import division

#####################################################
# Introduction to Python Programming WS 2012/2013   #
# Exercise Sheet NLTK                               #
#####################################################

"""
Name: <your-name-here>

"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Exercise 4: Search the word puzzle (10 points)     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
In the given word puzzle, words are hidden horizontally (also backwards)
and vertically. (There are also words hidden diagonally, but we will
disregard them for now.)

Install the 'words' corpus.
nltk.corpus.words.words() returns a list of English words as they
are used for instance in spell checkers. With the help of this list,
find all words that are comprised of 4 or more characters that are
hidden in the puzzle horizontally or vertically (in any direction, i.e.,
words may be read backwards / bottom to top). Then, only keep
the words that are related to 'friend' (noun) or 'love' (verb or noun)
using the LCH (Leacock-Chodorow) WordNet relatedness measure.
When retrieving the synsets for the word you found, do not give any
POS (all possible POS in WordNet will be considered). You can use the
getMaxSim() function that was presented in the lecture (maybe with some
little modification).

The solvePuzzle() function should return a list of these words.
Copy & paste your solution here:

WORDS FOUND:
<paste your solution here>

Hints:
- A good threshold for LCH in this case is 2.
- Checking whether a word is contained in the list of words is
    probably too slow (Python needs to iterate over the whole
    list). A trick for speeding up your program was presented in
    the lecture.
- You should find 10 words.


'''

import nltk

def solvePuzzle(puzzle):
    '''
    Your code to solve the puzzle goes into this function.
    '''
    pass
    
if __name__ == '__main__':
    
    puzzle = ["DCBCCAMDKCOFASR",
          "NEOOAONYOIRGSDY",
          "ETYNEEMMTINEIHL",
          "IAFFLVRPEINSTML",
          "RMRIAAINAENAHAA",
          "FMIDDMDTSNPIFIE",
          "LOEEBLIORMIFFRP",
          "RONUIPLTYOEOAFT",
          "IRDNECASYCPHNSA",
          "GDELOYALTYSPURR",
          "YSGOODTIMESRUIO",
          "SCHUMHONESTYFSV",
          "ECNATNIAUQCAUEA",
          "YHTAPMESSENDNOF"
          ]

    solvePuzzle(puzzle)
