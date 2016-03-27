def quik(a):
    b=[]
    c=[]

pivot=a[0]
a=[pivot]
  
    
    

    for i in a[1:]:
        if (a[i] < pivot):
            b.append(i)
            
        else:
            c.append(i)

     return quik(b)+q[0:1]+quik(a)        
            

