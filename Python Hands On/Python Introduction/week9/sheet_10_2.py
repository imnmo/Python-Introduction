''' 2. Extracting noun phrases (3 Points)

On the course homepage, you can download the file "wsj00-pos-oneline" that
contains POS tagged text. Implement a program that reads this file and prints
all noun phrases that occur in the text. To keep things simple, take noun
phrases to be the following sequence of parts of speech:

    DT + zero or more JJ + NN

where DT is the POS for determiners like "the" or "a", JJ is the POS for
adjectives, and NN is the pos for nouns.

Example:

python3 sheet_10_2.py wsj00-pos-oneline.txt

should print:

the/DT board/NN
a/DT nonexecutive/JJ director/NN
the/DT Dutch/NN
a/DT nonexecutive/JJ director/NN
this/DT British/JJ industrial/JJ conglomerate/NN
...

'''

import sys
import re

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            
            pat1=re.findall(r'\w*/DT\s*\w*/NN',line)
            pat2=re.findall(r'\w*/DT\s*\w*(/JJ|/JJ*)\s*\w*/NN',line)
            print(pat2)


if __name__ == '__main__':
    main()
