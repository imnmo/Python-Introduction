######################################
# Introduction to Python Programming #
# WS 2011/2012                       #
# Exercise Sheet 8                   #
# Object-Oriented Programming I      #
######################################
'''
Exercise 2: (4 points)

a) Write the complete code for the Employee class
    (including constructor, __str__,...) (2 points)

b) Create a few employee objects and show how you can
    manipulate them using the methods. (1 points)

c) Draw a UML class diagram for your Employee class. (1 point)
		(Submit as PDF!)
		Hint: There is an editor called 'dia' which makes it easy
	  to create UML diagrams. It is available for Linux, MacOS
		and Windows (http://dia-installer.de/download/index.html).

'''

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
        x=input('Enter the persons name to call on Emergency :')
        if x:
            print('Info  of the employee:  ',self.empno,self.holder)
        else:
            print('no value enetered')
    
    def __str__(self):


        return 'hey there'
if __name__ == "__main__":
    print("Employee application")
    x=Employee(2546028,"imran",23,"m","informatics","Researcher",2000)
    y=Employee(2567028,"mohamed",23,"m","informatics","Assitant",1000)
    x.payraise(500,"December")
    y.payraise(1500,"November")
    print(x)
    print(y)
    x.emergency() #This Function will have to executed on case of emeergency for immediate search on the systems
    
