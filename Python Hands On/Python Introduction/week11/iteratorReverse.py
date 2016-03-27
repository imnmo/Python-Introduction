class Reverse:

    def __init__(self,data):

        self.data=data
        self.index=len(data)


    def __iter__(self):

        return self


    def __next__(self):
        if self.index==0:
            raise StopIteration
        else:
            self.index-=1
            return self.data[self.index]

            

for i in Reverse([1,2,3]):
    print(i)
    
