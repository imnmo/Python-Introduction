f =open('simplepos.txt','r')
file = f.read()
tag_words=[]
    
for pair in file.rsplit(","):
    for x  in pair.rsplit("/",1):
        tag_words.append(x)
         
            
            
            

        

