


def byParagraph_generator(l):
        
        for line in l:
            line = line.rstrip()
            if line != '':
                    yield line
           
            
               

with open('example.txt') as f:
    for par in byParagraph_generator(f):
        print(par)
