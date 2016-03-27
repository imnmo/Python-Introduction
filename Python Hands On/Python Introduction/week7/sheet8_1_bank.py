######################################
# Introduction to Python Programming #
# WS 2011/2012                       #
# Exercise Sheet 8                   #
# Object-Oriented Programming I      #
######################################


'''
Exercise 1: (5 points)

a) Using the slides & the script, put together a file
    containing the complete Account class.
    Each method must have a documentation string at the
    beginning which describes what the method is doing.
    (1 points)

b) Create a main application where you create a number of accounts.
    Play around with depositing / withdrawing money.
    Change the account holder of an account using a setter method.
    (1 point)

c) Change the withdraw function such that the minimum balance
    allowed is -1000.
    (1 point)

d) Write a function apply_interest(self) which applies an interest
    rate of 1.5% to the current balance and call it on your objects.
    (1 points)

e) Draw a UML diagram representing your Account class. (1 point)

'''

class Account:
    ''' Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. '''
    '''The ___init__method allocates the holder and balance'''
    '''Deposit method takes the given amount passsed by argument
       and adds to the current balance'''
    '''Withdraw method gives the final amount after withdrawing the 
       amount,if more amount is withdrawn then Negative balance will
       be said'''
    '''Apply interest method applies the percenatge if balance is less than zero '''
    '''Set holder method creates the access to the other holder and it checks for the input String '''
    
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
        
        if person == 'mohamed':
            self.holder=person
            
            print('Access Enabled',self.holder)
            
        else:
            print('Invalid Name to grant access')

    
    def print_info(self):
        print('Balnce:' ,self.balance,'Person:', self.holder)
        
if __name__ == "__main__":
    print("Welcome to the Python Bank!")
    imranAcc=Account(0,"imran")
    imranAcc.deposit(1000)
    imranAcc.withdraw(200)
    imranAcc.apply_interest(0.015)
    imranAcc.set_holder(input('Enter the persons name: '))
    imranAcc.print_info()

