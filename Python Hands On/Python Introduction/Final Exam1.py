def squaress(n):
    x=0
    while x<n:
        yield x
        yield x * x
        x+=1

for i in squaress(10):
    print(i)
