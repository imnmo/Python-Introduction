class Account:
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def print_ifno(self):
        print('ur value',self.balance)
if __name__ == "__main__" :
    
    
    #Account/objects creation
    imranAcc= Account()
   
    #Attributes Assigning
    imranAcc.balance =0
    imranAcc.deposit(100)
    imranAcc.withdraw(50)
    imranAcc.print_ifno()
    
