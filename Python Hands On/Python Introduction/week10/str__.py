class one:
    def __str__(self):
        self.simply='Just to check'
        
        return self.simply

class two:
    def __str__(self):
        return'just to check once again'
class three:
    def print_one(self):
        self.customisedsimply=self.simply
        print('Lets c what it prints')
        print(self.customisedsimply)
    def print_two(self):
        pass



if __name__=='__main__':
   
    imran=two()
    imran=one()
    imran=three()
    print(imran)

    imran.print_one()
