
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python average.py <input file>', file=sys.stderr)
        sys.exit(1)

    filename = sys.argv[1]
    with open('input.txt') as f:
         file= f.readlines()
         c = [int(e) for e in file]
         sum = 0
    
    for line in file:
         in_line= int(line)
         
         sum = sum + in_line
         average = sum/len(file)


    return average


if __name__ == '__main__':
    main()    
