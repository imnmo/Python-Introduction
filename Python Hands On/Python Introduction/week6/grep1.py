def grep(filename,pattern):
    
    import re

    shakes = open(filename, "r")


    for line in shakes:
        if re.search(pattern, line):
            print (line)

    
            
          
