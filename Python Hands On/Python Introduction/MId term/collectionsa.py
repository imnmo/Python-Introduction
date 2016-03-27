import copy
list1=[1,[5,7],6]
a=list1[:]
a[0]=9
a[1][1]=4
print(a,list1)
