class person:
    def __init__(self,fn,ln,a):
        self.firstname=fn
        self.lastname=ln
        self.age=a
class Account:
    def __init__(self,holder,num):
        self.person=holder
        self.num=num

    def print_info(self):
        print(self.person)


if __name__ == "__main__":

    anne=person('anne','magai',25)
    annesAcc=Account(anne,1)
    Account.print_info()
