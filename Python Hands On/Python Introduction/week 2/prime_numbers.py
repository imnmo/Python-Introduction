# Exercise 5: Prime Numbers
# Print out prime numbers < 200

# Inefficient version: check for each number separately whether
# it's a prime or not.
# If your version is like this, it's okay!
# The sieve of Eratosthenes (see below) was not expected.

# Using for loops
primes = []
for i in range(2,200):
    prime = True
    for j in range(2,i):
       if i%j == 0:
           prime = False
    if prime:
        primes.append(i)
print("Primes", primes)


# Using while loops & break
primes = []
n = 1
while n <= 200:
   i = 2
   while i < n:
      if n%i == 0:
          # Found a divisor
          break
      i += 1
   if i == n:
      # If i==n, this means we didn't find any number < n
      # by which n is divisible.
      primes.append(n)
   n += 1
print("Primes: ", primes)


# Efficient version:
# Sieve of Eratosthenes
# see http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# Create a list with all candidates (here: 1-200)
numbers = list(range(2,201))
# print("Candidates: ", numbers)
# start with the first prime number: p=2, first item in the list of candidates.
i = 0
p = numbers[i]
# we are not done until we checked all multiples of p once and didn't make a change
done = False
while not done:
   done = True
   x = 2
   while x*p < 201:
      # remove all multiples of p from the list (those are not primes)
      if x*p in numbers:
          numbers.remove(x*p)
          done = False	# we found something to be removed, this means we're not done yet.
      x += 1
   # go on with the next number in the list after p (must be a prime)
   i += 1
   p = numbers[i]
print("Primes: ", numbers)



