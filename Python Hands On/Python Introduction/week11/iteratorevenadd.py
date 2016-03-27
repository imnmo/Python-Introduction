class print:
    def __init__(self,data):
        self.data=data
        self.index=0
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.data):

            raise StopIteration
        else:

            return self.data[self.index]



for i in addeven([1,2,3]):
    print(i)
    

            
