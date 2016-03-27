def selection(a):
#To do the selection sort
    b=[]
    a=a[:]
#Finding minimum in the list:

    while (len(a) > 0):
        minimum = 0   
        for i in range (1,len(a)):
            if a[i] < minimum:

                minimum = i
#append & pop
    b.append(a.pop(minimum))
    return b
