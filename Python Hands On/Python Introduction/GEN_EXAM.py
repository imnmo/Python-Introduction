def squaress(n):
    x=0
    while x<n:
        yield x* x
        x+=1


for i in squaress(10):
    print(i)
'''Without FOr loops dont ever dare to use the for looops'''
