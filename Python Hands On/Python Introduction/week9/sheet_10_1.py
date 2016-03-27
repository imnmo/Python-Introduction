''' 1. POS-Tagged text (3 Points)

On the course homepage, you can find a small example file containing
POS-tagged text, where words are represented as follows:

    <W TYPE="part of speech" ...>word</W>

Write a program that reads the file and outputs just the word
together with its POS (see example below).

Example:

python3 sheet_10_1.py sheet_10_1_example.txt

should print:

FACTSHEET NN1
WHAT DTQ
IS VBZ
AIDS NN1
...
'''

import re
import sys
import re

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            pat1=re.findall(r'<W\s*\w\w\w\w.*>',line)
            for line1 in pat1:
                pat2=re.search(r'"(\w\w\w|\w\w\w[-]\w\w\w)"',line1)
                pat3=re.search(r'>(.*)<',line1)
                print(pat2.group(1),pat3.group(1))

if __name__ == '__main__':
    main()

