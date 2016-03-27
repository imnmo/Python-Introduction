# -*- coding: utf-8 -*-
from __future__ import division

#####################################################
# Introduction to Python Programming WS 2012/2013   #
# Exercise Sheet NLTK                               #
#####################################################

"""
Name: <Mohamed Imran>
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Exercise 3: Dispersion Plot (3 points)            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
a) Produce a dispersion plot of the four main protagonists in
Sense and Sensibility (open 'austen-sense.txt' from the
Gutenberg corpus): Elinor, Marianne, Edward, Willoughby.
The plot has to be submitted as exercise3.png.
(2 points)

b) What can you observe about the different roles played by
the males and females in this novel? Can you identify couples?
(1 point)

Hints:
http://nltk.googlecode.com/svn/trunk/doc/api/nltk.text.Text-class.html
http://nltk.googlecode.com/svn/trunk/doc/book/ch01.html (search for
dispersion plot on this page)
'''


from nltk.corpus import gutenberg
from dispersion import dispersion_plot
words = ['Elinor', 'Marianne', 'Edward', 'Willoughby']
dispersion_plot(gutenberg.words('austen-sense.txt'), words)

'''
b.The chracters Elinor(f) and Marianne(f) comes constantly(uniformly) throughout the novel but Edward(m)
and Willoughby(m) appear almost seperately.Marianne and Willoughby appear as couple.
'''
