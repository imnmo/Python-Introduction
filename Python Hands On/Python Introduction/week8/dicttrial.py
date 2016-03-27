
class Customer:
    ''' objects of this class represent customers.
    The customer ID is supposed to be assigned automatically
    when a new customer object is created.
    Attributes:
    - first name
    - last name
    - age
    '''
    #Class Attributes
    number_of_customers=0
    customer_id=0
    
    # CONSTRUCTOR
    def __init__(self, fn, ln, age):
        
        # Constructor Method:
        self.firstname=fn
        self.lastname=ln
        self.age=age
        Customer.customer_id+=1
        Customer.number_of_customers+=1
      # STATIC METHODS
    ''' write a method here that prints out how many
    customers have been created so far '''
    @staticmethod
    def print_info():
        print('Number of Customers',Customer.number_of_customers)

        
if __name__ == "__main__":
  

    # Create a few customers and add them to the bank object
    anne = Customer("Anne", "Friedrich", 85)
   
    stefan = Customer("Stefan", "Thater", 76)
    
    maja = Customer("Maja", "Biene", 2)
    
   
    
    

    # Number of customers
    print("")
    Customer.print_info()
 
    
    
    
    
    
