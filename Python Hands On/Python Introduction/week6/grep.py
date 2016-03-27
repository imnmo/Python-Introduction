''' 2. Grep (3 Points)

Write a program grep.py that searches a given input file for lines containing
a word, and prints all matching lines. For instance, 

    python3 grep.py wsj00.txt research

should print all lines in wsj00.txt that contain the string "research".
'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python grep.py <input file> <string>', file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    searchfor = sys.argv[2]
    # your code

if __name__ == '__main__':
    main()


def grep(filename, word):
    
    f = open(filename)
    while True:
        line = f.readline()
        if line == '': # no input => stop
            break
        for word in line:
            if word == 'research':
               print (line)
    f.close()
