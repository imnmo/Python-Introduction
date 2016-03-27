
def avg(it):
    
    l=[]
    s=[]
    for (i,ele) in enumerate(it):
        l.append(i)
        s.append(ele)
    sumit=sum(s)
    lenit=len(l)
    return (sumit/lenit)
    
    
    




myIter = iter([5,10,15])
print(avg(myIter))
