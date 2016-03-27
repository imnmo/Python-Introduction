
def bubblesort(numbers,ascending):


    for i in range(len(numbers)):
    
        for j in range(i+1,len(numbers)):
        
        
            if(numbers[i] <  numbers[j]):



                 t = numbers[i]
                 numbers[i]=numbers[j]
                 numbers[j]=t
    if ascending:             
        numbers.reverse()
        return(numbers)
    else:
        return(numbers)
            
             
