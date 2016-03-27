import re

with open('process2.txt') as f:
    
    for line in f:

        #print(line)
        pat1=re.findall(r'\w*/DT\s*\w*/NN',line)
        pat2=re.findall(r'\w*/DT\s*\w*(/JJ|/JJ*)\s*\w*/NN',line)
        
        
        print(pat2)

        
        
        
        #for line1 in pat1:
            
        #    pat2=re.search(r'"(\w\w\w|\w\w\w[-]\w\w\w)"',line1)
        #    pat3=re.search(r'>(.*)<',line1)
        #    print(pat2.group(1),pat3.group(1))
            
        
            


    
        
        
            
        
        

    
