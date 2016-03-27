import functions

"""
This program asks the user to enter a date
and calculates the day of the week using Zeller's Congruence.

You don't need to change anything here. Just run it!
(After you have implemented the function zeller(day, month, year)
in the functions.py file!!)
"""

def num_to_day(weekday):
    """
    Converts an integer from 0 to 6 to a weekday starting with Saturday.
    For example:

    >>> num_to_day(0)
    'Saturday'
    >>> num_to_day(1)
    'Sunday'
    >>> num_to_day(6)
    'Friday'
    """
    weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    return weekdays[weekday]

def format_date(day, month, year):
    """ 
    Returns a string with the date encoding  D/M/YYYY 
    For example:
    
    >>> print format_date(30,12,1991)
    30/12/1991
    """
    return "/".join([str(day),str(month),str(year)])
    
# The User-Interface for the program

print("** ZELLER's CONGRUENCE **")
print("Let's compute the weekday!")
year = int(input("Please enter year:"))
month = int(input("Please enter month (a number between 1 and 12):"))
day = int(input("Please enter day of the month:"))


print(format_date(day,month,year),
      "is a",
      num_to_day(
          functions.zeller(day, month, year)
          )
      )
