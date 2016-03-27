''' 1. Average and median (3 Points)

Write a program average.py that reads in a list of numbers (integers) from a
file and prints the average value and the median.

For instance, if input.txt is a file containing the numbers 1, 17, 6 and 25,

    python3 average.py input.txt

should produce the following output:

average: 12.25
median: 11.5

It is required to use exactly this format:
First line: "average", colon, white space, number
Second line: "median", colon, white space, number


Hints:

* To map a string representing a number to an actual number, you can use "int(str)"

* The average (or arithmetic mean) of a list of numbers is the sum of all
  numbers divided by the length of the list.

* The median of a list of numbers can be obtained by sorting the list and
  picking the middle element (if the list has an odd number of elements). If
  there is an even number of elements, compute the mean of the two middle values

'''

import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python average.py <input file>', file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    # your code
    with open(filename) as f:
    file= f.readlines()
              
    c = [int(e) for e in file]
    c.sort()
    sum = 0
    for line in file:
        in_line= int(line)
        sum = sum + in_line
        average = sum/len(file)


       

    
    len_in_line=int(len(c))
    if(len_in_line%2 == 0):
        
        median1 = (c[int(len_in_line/2)]+c[int(len_in_line/2)-1])/2
        print ("Median"+ ':'+ ' ', median1)
            
    else:
        
        median2 = c[int(len_in_line/2)]
        
        print ("Median"+ ':'+ ' ', median2)
            
    print ("Average"+ ':'+ ' ', average)  

if __name__ == '__main__':
    main()

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
    import re

    words = open("wsj00.txt", "r")

    for line in words:
        if re.match("(.*)(r|l)esearch(.*)", line):
            print ("The Lines are :",line)
            
    

if __name__ == '__main__':
    main()


''' 3. Counting tagged words (4 Points)

On the lecture's homepage, you can find a file containing an English text where each
word is annotated with a part-of-speech (POS) tag.

Write a program poscount.py that counts how often each word occurs in the file,
and how often it has been tagged by which POS.

For instance,

    python3 poscount.py wsj00-pos.txt

should produce a output like this:

Manufacturers   2       NNS     1       NNP     1
Western         10      JJ      5       NNP     5
straight        4       RB      1       JJ      3
reported        16      VBN     7       VBD     9
...

The second column gives the total number of times the word occurs in the 
input file.

It is required to use exactly this format: 
word, tab (\t), number, POS, tab, number, POS, tab, number, ...

Hints:

* To split a word/pos pair into two separate strings (word and pos), you can
  use pair.rsplit('/', 1).
  
'''

import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python poscount.py <input file>', file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    # your code

if __name__ == '__main__':
    main()


