class Account:
    #init method:
    def __init__(self,num,person):
        self.balance=num
        self.holder=person
        
    #instance method:
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        
        if amount > self.balance:
             self.balance = self.balance-amount
             print("ur holding negative balance:Reported",self.balance)

        else:
            self.balance-=amount
    def apply_interest(self,per):
        if self.balance < 0:
            self.balance=self.balance*per + self.balance
            #interest can be added per day sequence :
            
            print('Added interest per day',self.balance)
    def set_holder(self,person):
        self.holder=person
        if not type(self.holder) == str:
            raise TypeError
        else:
            print('Access Enabled',self.holder)

    
    def print_info(self):
        print(self.balance,self.holder)
        


#main class:

    
if __name__ =="__main__":
    imranAcc=Account(0,"imran")
    imranAcc.deposit(1000)
    imranAcc.withdraw(200)
    imranAcc.apply_interest(0.015)
    imranAcc.set_holder("mohmad")
    imranAcc.print_info()
  
    
    
    
