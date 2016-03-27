class Customer:
    customer_id=0
    number_of_customers=0
    cust={}

    def __init__(self,fn,ln,age):
        self.fn=fn
        self.ln=ln
        self.age=age
        Customer.number_of_customers+=1
        if self.fn=='Anne':
            self.customer_id=1
        if self.fn=='Stefan':
            self.customer_id=2

        self.cust[self.fn]=self.customer_id
        
        
    def increment_age(self):
        self.age+=1
        
    def __str__(self):
        customer = "*** Customer Info ***\n"
        customer+="Customer id:"+str(self.customer_id)+'\n'
        customer += "First name:" + str(self.fn) + "\n"
        customer += "Lastename:" + self.ln + "\n"
        customer += "Age: " + str(self.age) + "\n"
        return customer
    def set_lastname(self,ln):
        self.lastname=ln
        
    def print_value(self):
         
         print(self.cust)
       
    @staticmethod
    def numbercust():
        print('number of Accounts:',Customer.number_of_customers)


class Account:
    acc_id=0
    number_of_account=0
    acc={}
    def __init__(self,holder):
        
        self.holder=holder
        self.balance=0
        
     
    def withdraw(self, amount):
        
        if amount > self.balance:
            amount = self.balance
        self.balance -= amount
        
        return amount
        
    def deposit(self, amount):
        
        self.balance += amount

    def set_holder(self, new_holder):
        
        self.holder = new_holder
        
    def __str__(self):
       
        return "[Account: ID=" + str(self.acc_id) \
              + " BALANCE=$" + str(self.balance) \
              + " HOLDER=" + str(self.holder)+ "]"
        

    
        
    @staticmethod
    def numberacc():
        print('number',Account.number_of_account)

class Bank:
    def __init__(self, name):
        
        self.name=name
        
    # INSTANCE METHODS
    def add_customer(self, customer):
         
        ''' adds a customer object to the bank's customers '''
        self.customer=customer
        
    def add_account(self, account):
        ''' adds an account object to the bank's accounts '''
       
        self.account=account
        
        
    def print_accounts(self):
        ''' print out all accounts of the bank '''
        print("\n** ACCOUNTS **")
        
        print(self.account)
       
    def print_customers(self):
        ''' prints out all the customers of the bank '''
        print("\n** CUSTOMERS **")
        print(self.customer)

    
    def deposit(self, acc_id, amount):
        ''' deposit money into the account '''
        self.acc_id=acc_id
        self.amount=amount
        self.balance=0
        Account.deposit(self,amount)

    def withdraw(self, cust_id, acc_id, amount):
        ''' withdraw money from the account with the given ID,
        but only if its holder has the given customer ID.
        Returns the amount of money (=cash)'''
        self.cust_id=cust_id
        self.acc_id=acc_id
        self.amount=amount
        Account.withdraw(self,amount)
       
        
        

    def print_info(self):
        print(self.amount)
        
if __name__ == "__main__":
    # Create a new bank object
    bank = Bank('PYTHON-BANK')
    print(bank)

    # Create a few customers and add them to the bank object
    anne = Customer("Anne", "Friedrich", 85)
    bank.add_customer(anne)
    stefan = Customer("Stefan", "Thater", 76)
    bank.add_customer(stefan)
    


    #Account
    
    annesAcc1 = Account(anne)
    bank.add_account(annesAcc1)
    
    stefansAcc = Account(stefan)
    bank.add_account(stefansAcc)
   
    
    
  
    
   

    # Deposit money into accounts
    print("\nAnne deposits $300 into account with ID 1.")
    bank.deposit(1, 1000)
    
    
   # Withdraw money from some accounts
    print("\nAnne tries to withdraw from Stefan's account.")
    bank.print_info()
    bank.withdraw(0, 1, 100)
    print("Anne got:", )

     # Print out all the customers of the bank
    bank.print_customers()

     # Print out all the accounts of the bank
    bank.print_accounts()

   
    
    
    
    




        
        
    





