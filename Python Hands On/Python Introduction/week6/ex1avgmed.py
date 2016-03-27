with open('input.txt') as f:
    file= f.readlines()
              
    c = [int(e) for e in file]
    c.sort()
    print (c)
    sum = 0
    for line in file:
        in_line= int(line)
        sum = sum + in_line
        average = sum/len(file)


       

    
    len_in_line=int(len(c))
    if(len_in_line%2 == 0):
        
        median1 = (c[int(len_in_line/2)]+c[int(len_in_line/2)-1])/2
        print (median1)
            
    else:
        
        median2 = c[int(len_in_line/2)]
        
        print (median2)
            
    print (average)    
    
    
    
    


 









