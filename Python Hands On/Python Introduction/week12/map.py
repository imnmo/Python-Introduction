
#Map:

def fil(x):#Gets odd function:
    return x % 2 == 1


def add(x):
    return x+ x
    






#lambda:

#print(list(map(lambda x,y: x+y,[1,4,5],[3,4,5])))

#filter:
#All in one Shot Map,Lamba,Filter:

x=(list(filter(fil,[1,2,3])))

print(x)

print(list(map(add,x)))

print(list(map(lambda x: x+x,x)))



