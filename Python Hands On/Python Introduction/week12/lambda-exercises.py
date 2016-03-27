a = [-2, 0, 1, -5, 23, 17]
b = [2, 0, 2, 4, 10, -2]

def placeHolderFunction(*args):
    return None

# placeHolderFunction is used in the code below to make it compilable.
# Replace it with your lambda expressions.

# (a) Write a lambda expression that returns the absolute value of the argument.
c =  map(placeHolderFunction, a)
c = list(c) # use the returned iterator to create a list
print(c)
# Should print: [2, 0, 1, 5, 23, 17]

# (b) Write a lambda expression that returns the sum of its two arguments.
d = map(placeHolderFunction, a, b)
d = list(d)
print(d)
# Should print: [0, 0, 3, -1, 33, 15]

# (c) Write a lambda expression that returns the argument to the power of 3.
# Hint: power in Python: math.pow(x, y) --> x to the power of y
# or x**y
e = map(placeHolderFunction, b)
e = list(e)
print(e)
# Should print [8, 0, 8, 64, 1000, -8]

# (e) Write a lambda expression that returns True if the argument is greater
# than zero, and False otherwise
f = map(placeHolderFunction, a)
f = list(f)
print(f)
# Should print [False, False, True, False, True, True]
