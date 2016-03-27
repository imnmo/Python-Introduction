# Exercise 4: Factorial
# Computes the factorial of 14.

# Version using a while loop.
x = 14
factorial = 1
while x > 0:
   factorial *= x
   x -= 1
print("Using a while loop: ", factorial)

# Another version using a for loop
n = 1
for i in range(14,1,-1):
    n *= i
print("Using a for loop: ", n)


# A version that computes the factorial of any number.
def factorial(x):
   n = 1
   for i in range(2, x+1):
      n *= i
   return n

print("Using a function: ", factorial(14))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
