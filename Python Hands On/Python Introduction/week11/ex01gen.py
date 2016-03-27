def myEnumerate(ints):
    for i in range(len(ints)):
        yield i, ints[i]

for (i,ch) in myEnumerate("Python"):
    print (i,ch)
    
