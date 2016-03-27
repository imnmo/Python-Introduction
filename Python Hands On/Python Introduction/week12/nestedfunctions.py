
#Map and Nested Function:
'''
def a(x):
    total =sum(x)
    
    def b(x):
        return (x/total)
       
        
    
    return (list(map(b,x)))
'''

#Nested and Lambda
'''
def a(x):
    total =sum(x)


    return (list(map(lambda x: x/total,x)))


x=a([1,2,3])
print(x)
'''

#More on Nested Fuction:
def add1(n):
    def add(m):
        return m+n
    return add

x=add(7)


print(x)

