a = [3,1,6,7,5]
b = []

min=0
while(len(a)>0):
    
    for i in a:
        for j in a[1:]:
        
            if (i < j):
                min = i
                b.append(a.pop(i))
    
            else:
            
                min = j
                b.append(a.pop(j))
            

print (a,b)
