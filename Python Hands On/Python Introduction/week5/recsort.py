
a=[3, 9, 6]

def sort():
    
    for j in range(1,len(a)):
        
    
        for i in range(0,j+1):
        
        
            if(a[j] <  a[i]):



                 t = a[i]
                 a[i]=a[j]
                 a[j]=t
                 print (a)            
