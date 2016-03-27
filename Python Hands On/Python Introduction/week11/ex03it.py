class ByParagraph:


    def __init__(self,data):

        self.data=data
        


    def __iter__(self):

        return self

    def __next__(self):

        return self.data
        
        #for line in self.data:
            #return line
            #line = line.rstrip()
            #if line == 0:
            #    raise StopIteration
            #else:
            #    line != ''
            #    return line


with open("example.txt") as f:
    for par in ByParagraph(f):
        print(par)
