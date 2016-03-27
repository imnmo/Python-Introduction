class Employee:
    #init method:
    def __init__(self,name,age,sex,dept,postion):
        self.person=name
        self.age=age
        self.sex=sex
        self.dept=dept
        self.postion=postion
        self.balance
    #pay raise:
    def bonus(self,salary,amount):
            self.salary=salary
            slef.salary+=amount
            print (self.salary)
    #Change name after marriage:
    def set_holder(self,person):
            self.holder=person
            
            if not type(self.holder) == str:
                raise TypeError
            else:
                print('Name Chnged',self.holder)

    def print_info(self):
        print(self.person,self.salary)
        


#main class:

if __name__ == "___main__":
    Employee1=Employee("Mr.ruth","34","m","informatics","Reasearch Associat")
    Employee2=Employee("Ms.Christa","24","f","Bio-informatics","Assiatant")
    Employee1.bonus(2000,1000)
    Employee2.set_holder("Mrs.charlie")
    Employee1.print_info()
#    Employee2.print_info()
    
    
