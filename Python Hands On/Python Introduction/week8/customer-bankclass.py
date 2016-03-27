class customer:
    number_of_customers=0
   
    
    def __init__(self,fn,ln,age):
        self.fn=fn
        self.ln=ln
        self.age=age
        customer. number_of_customers+=1
        
       
    def increment_age(self):
        self.age+=1
    def __str__(self):
        customer = "*** Customer Info ***\n"
        customer+="customer id:"+str(self.customer_id)+'\n'
        customer += "First name:" + str(self.fn) + "\n"
        customer += "Lastename:" + self.ln + "\n"
        customer += "Age: " + str(self.age) + "\n"
        return customer




        return res
    def set_lastname(self,ln):
        self.lastname=ln
    @staticmethod
    def number_of_customers():
        
        print('number of customer',customer.number_of_customers)






if __name__=='__main__':
    anne=customer('anne','freidrich',65)
    stefan=customer('stefan','thtacher',78)
    customer.number_of_customers()
    print(anne,stefan)
