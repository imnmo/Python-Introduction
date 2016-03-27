from __future__ import division

#####################################################
# Introduction to Python Programming WS 2012/2013   #
# Exercise Sheet NLTK                               #
#####################################################

"""
Name: <your-name-here>
"""


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Exercise 5: POS Tagging (5 points)                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

'''
In this exercise, we are going to evaluate the accuracy of a
part-of-speech (POS) tagger.

a) The function nltk.pos_tag(list-of-words) assigns pos tags
    to a list of words using the currently recommended POS
    tagger. You need to install maxent_treebank_pos_tagger:
    Either by using nltk.download() or by downloading number 73
    from http://nltk.googlecode.com/svn/trunk/nltk_data/index.xml
    and then unzipping it into nltk_data/taggers. You also need
    to unzip the file inside the maxent_treebank_pos_tagger
    folder.
    
b) Also install the dependency_treebank (= a subset of the
    Penn Treebank corpus) and the conll2000 corpora. Both corpora
    have been POS-tagged manually. You can retrieve the tuples
    containing the words and POS tags using someCorpus.tagged_words().
    Make yourself familiar with the data structure returned by this
    function by looking at a few examples.
    
c) Tag the first 25,000 words of each corpus automatically and then
    compare the automatically assigned tags to the manually assigned
    POS tags. What is the accuracy of the automatic tagger?
    (Hint: The automatic tagging takes around 90 seconds per corpus
    on my machine - so be patient!)

    Answers here:
        Accuracy for conll2000:
        Accuracy for dependency_treebank:
    
d) If you did everything correctly, you will see that the tagger does
    a lot better on one of the corpora. Do you have any idea why that
    is?

'''

# write your code here
