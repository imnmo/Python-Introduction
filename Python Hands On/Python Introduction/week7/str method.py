class Account:
    
    def __init__(self,num,person,bal):
        
        self.number=num
        self.holder=person
        self.balance=bal
    def __str__(self):
        res = "*** Account Info ***\n"
        res += "Account ID:" + str(self.number) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Balance: " + str(self.balance) + "\n"
        return res

if __name__ == "__main__":
    annesAcc = Account(1, "Anne",100)
    
    print(annesAcc)
