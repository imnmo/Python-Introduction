def quik(a):
    b=[]
    c=[]

#    pivot=a[0]
    
    if len(a) <= 1:
        return a
    
    
    for i in a[1:]:
        if (i < a[0]):
            
            b.append(i)
            
        else:
            
            c.append(i)

    return quik(b)+a[0:1]+ quik(c)        
            
