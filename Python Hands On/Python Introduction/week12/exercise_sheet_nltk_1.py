from __future__ import division

#####################################################
# Introduction to Python Programming WS 2012/2013   #
# Exercise Sheet NLTK                               #
#####################################################

"""
Some of these exercises are taken from the NLTK book:
Bird, Steven, Edward Loper and Ewan Klein (2009).
Natural Language Processing with Python. O'Reilly Media Inc.
(But don't even try looking, the solutions are not in there. =D)

!!! IMPORTANT !!!
Please submit the 5 Python files including your solutions,
as well as additional files if required.
>>> Please don't change the filenames. <<<

Name: <Mohamed IMran>

"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Introduction: Installing NLTK Corpora             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
If you are working on your own computer, you can install
the corpora using nltk.download() in your Python Shell. A
window pops up and you can select the corpora you need.

However, if you are working on one of the Coli machines,
you need to copy the corpora you want to use into your
home directory manually.
See: http://wiki.coli.uni-saarland.de/wiki/index.php/NLTK
(only accessible from within Coli).
'''


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Exercise 1: Zipf's Law (3 points)                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
Read all the text of the genres "humor", "romance" and "adventure"
of the Brown corpus into ONE Text object. (See slides, or
NLTK API Documentation online.)

The code for this exercise is to be submitted (write
your code into THIS file). The same goes for all NLTK exercises.

Then, create a frequency distribution of the words occurring in
the corpus and create a plot with the 50 most frequent words.
For this task, check out the documentation at
http://nltk.github.com/api/nltk.html?highlight=freqdist#nltk.probability.FreqDist
You will need to look at the constructor and at the plot() function
of FreqDist.

Save the plot as exercise1.png (which is to be submitted).

Looking at the plot, answer the following questions (write your answers here):

a) How often does the word 'the' occur?
    The word 'the' has approximately 2200 times in these genre

b) How does the overall graph look like, and how is this explained?
    (Hint: Search for Zipf's Law on the web.)
    <your-answer>   
    
c) What kind of words are the most frequent ones?
    the,of,and,to


'''
from nltk.corpus import brown

from nltk import FreqDist


genres=['humor','romance','adventure']



for g in genres:
    words=brown.words(categories = g) #Contains all categories in a  single shot
    fdist=FreqDist([w for w in words])
    print (g,fdist)
    fdist.plot(50,cumulative=True)

