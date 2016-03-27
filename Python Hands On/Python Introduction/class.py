class Person:
    def __init__(self, f, l, a):
        self.firstname = f
        self.lastname = l
        self.age = a
class Account:
    def __init__(self, person, num):
        self.holder = person
        self.num = num
        self.balance = 0
        return None 
    def deposit(self, amount):
        self.balance += amount



if __name__ == '__main__':
    anne = Person("Anne", "Friedrich", 85)
    annesAcc = Account(anne, 1)
