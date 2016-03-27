import re

with open('sheet_10_1_example.txt') as f:
    for line in f:
        pat1=re.findall(r'<W\s*\w\w\w\w.*>',line)
        for line1 in pat1:
            
            pat2=re.search(r'"(\w\w\w|\w\w\w[-]\w\w\w)"',line1)
            pat3=re.search(r'>(.*)<',line1)
            print(pat2.group(1),pat3.group(1))
            
        
            


    
        
        
            
        
        

    
