#########################
# Exercise Sheet 7      #
# GOLD BUG              #
#########################

''' Gold-Bug (4 Points)

(see also http://en.wikipedia.org/wiki/The_Gold-Bug)

We are given an encrypted file (using a very simple encryption scheme) in
which letters have been replaced by other letters. Implement the following
simple algorithm that decrypts the file exploiting information about the
relative frequency of characters:

1. Create a list E of characters sorted by the relative frequency of the
   characters in the encrypted file (descending order).

2. Create a list R of characters sorted by the relative frequency of the
   characters in the English reference file (descending order).

3. Replace each character x in the encrypted file as follows: if x is the nth
   character in E, replace c by the nth character in R.

Hints:

* You should use a dictionary to count character frequencies. To obtain a list
  of keys (= characters) sorted by its numerical value, you can use

  sorted(d, key=d.__getitem__, reverse=True)

  where d is the dictionary mapping keys to numbers.

* You can use l.index(x) to find the index (= position) of some value x in a
  list l. For instance, ['a', 'b', 'c'].index('b') evaluates to 1.

* The builtin function "zip" might also be useful.
  See http://docs.python.org/py3k/library/functions.html#zip

'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python goldbug.py <encrypted file> <reference file>', file=sys.stderr)
        sys.exit(1)

    encfile = sys.argv[1]
    reffile = sys.argv[2]

    # your code

if __name__ == '__main__':
    main()

