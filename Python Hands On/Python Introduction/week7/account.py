class Account:
 # METHODS
    def deposit(self, amount):
    self.balance += amount

 if __name__ == "__main__":
     annesAcc = Account()
     
     annesAcc.balance = 200
     annesAcc.deposit(500)
