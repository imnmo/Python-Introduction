def grep(filename,wrd):
    with open(filename) as f:
        for line in f:
            
            if wrd in line:
                m=line.split(',')
                for n in m:
                    return n
y=grep('input.txt','Facebook')
print(y)
