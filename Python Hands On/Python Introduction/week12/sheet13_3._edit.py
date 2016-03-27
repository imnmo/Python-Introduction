#########################################
# Introduction to Python Programming    #
# Exercise Sheet 13                     #
# List Comprehensions                   #
#########################################

# Exercise 3


''' (2 Points)

Rewrite the function f1 in function f2 using a single
list comprehension.

'''

def f1(words):
    result = []
    for word in words:
        wordlenpair = (word, len(word))
        result.append(wordlenpair)
    return result

x=f1(['Python', 'is', 'great'])
print(x)

def f2(words):

    l=[(i,len(i)) for i in words]

    return l


x=f2(['Python', 'is', 'great'])
print(x)
