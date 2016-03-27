total = 0.0
length = 0.0
average = 0.0
#Get the name of a file
filename = input('Enter a file name: ')

#Open the file
infile = open(filename, 'r')

#Read the file's contents
contents = infile.read().strip().split()

#Display the file's contents
print(contents)

#Read values from file and compute average
for line in infile:
    amount = float(line)
    
    total += amount
    length = length + 1
    


average = total / length

        #Close the file
infile.close()

        #Print the amount of numbers in file and average
print('There were ', length, ' numbers in the file.' )
print(format(average, ',.2f'))

    
