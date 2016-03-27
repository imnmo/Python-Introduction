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
word, tab (\t), number, tab, POS, tab, number, tab, POS, tab, number, ...
word, tab (\t), number, tab, POS, tab, number, tab, POS, tab, number, ...


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


