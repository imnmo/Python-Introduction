a=[1,7,6,25,17]

a.sort()

b= int(len(a))


if(b%2 == 0):
    median1 = (a[int(b/2)]+a[int(b/2-1)])/2
    print (median1)
else:
    median2 = a[int(b/2)]
    print (median2)









