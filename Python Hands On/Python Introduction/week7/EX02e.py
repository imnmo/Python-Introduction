class Employee:
    def __init__(self,num,person,age,sex,dept,pos,salary):
        self.department=dept
        self.empno=num
        self.holder=person
        self.position=pos
        self.age=age
        self.sex=sex
        self.pay=salary
    def payraise(self,value,month):
       
        
        
        if month=="December" and self.holder=='imran':
            self.pay+=value
            print(self.pay,self.holder)
        if month=='November'and self.holder=='mohamed':
            self.pay+=value
            print(self.pay,self.holder)
    def emergency(self):
        x=input('Enter the persons name')
        if x:
            print('info  of the employee:  ',self.empno,self.holder)
        else:
            print('no value enetered')
    
    def __str__(self):
        res = "*** Account Info ***\n"
        res += "Account ID:" + str(self.empno) + "\n"
        res += "Holder:" + self.holder + "\n"
        res += "Age: " + str(self.age) + "\n"
        res += "Dept: " + self.department + "\n"
        res += "Salary Recieved with bonus: " + str(self.pay) + "\n"
        return res
        




#main method:
x=Employee(2546028,"imran",23,"m","informatics","Researcher",2000)
y=Employee(2567028,"mohamed",23,"m","informatics","Assitant",1000)
x.payraise(500,"December")
y.payraise(1500,"November")
print(x)
print(y)
x.emergency()
    
