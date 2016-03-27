# Introduction to Python Programming
# Winter 2012/13
# Exercise Sheet 2: Functions


# 1. Leap years (2 Points) '''


def is_leap(year):
    """ This function returns True if the year is a 
    leap year and False otherwise.

     >>> is_leap(1988)
     True
    """
    if (year % 2 == 0):
     return True
    else:
     return False
    pass

# 2. Prime numbers (4 Points)

def is_prime(n):
    """
    Implement a funktion is_prime(n) that returns True if n is a prime, False
    otherwise. 

    For example:
    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    >>> is_prime(8)
    False
    """
    if (n!=2) and (n%2==0)or (n==1):
        return False
    else:
        if(n!=3)and(n%3==0):
            return False
        else:
            if (n%n == 0):
                return True
    pass


# 3. Zeller’s Congruence (6 Points)
'''
(see additional pdf file)
'''

def zeller(day, month, year):
    """
    >>> zeller(18, 11, 2012)
    1
    """
    m = month
    q = day
    if (q==1) or (q==2):
        if (q == 1 ):
            q = 13
            t = year -1
            i = str(t)
            j = i[0]+i[1]
            k = i[2]+i[3]
            J = int(j)
            K = int(k)
            a = int((m+1)*26 /10)
            b = int((K/4) + (J/4))
            h = (q + a + K + b - 2*J)%7
            return h
        
    i = str(year)
    j = i[0]+i[1]
    k = i[2]+i[3]
    J = int(j)
    K = int(k)
    a = int((m+1)*26 /10)
    b = int((K/4) + (J/4))
    h = (q + a + K + b - 2*J)%7
    return h 
  
    
    
    
    

    # This is not correct, but shows that the tests fail if the
		# implementation is wrong.
    # Your code will go here and it should not always return 0 :)
    return 0



# This automatically tests your code
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

