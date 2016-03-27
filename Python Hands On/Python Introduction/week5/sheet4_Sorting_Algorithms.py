#########################
# Exercise Sheet 4	#
# SORTING ALGORITHMS	#
#########################



''' 1. Bubblesort (6 Points)

Bubblesort is an extremely simple algorithm to sort a list of numbers.
The basic idea is to
1. iterate over the input list (from "left" to "right").
2. if two consecutive numbers are in the wrong order: swap items
3. if no swaps are needed: stop; otherwise go back to step 1

a) Execute the Bubblesort algorithm with pen & paper (similar to how
	we looked at it in the lecture - see slides) for the following
	list: b = [9, 3, 6, 2, 7, 8, 1]

b) Implement a function bsort(numbers) that implements the bubblesort
	algorithm. The result should be an ordered list.
	The full 6 points will only be awarded if the steps of the algorithm are
	sufficiently commented! You are not allowed to use the sorted() or sort()
  functions!
'''

def bubble_sort(numbers):
    
    for i in range(len(numbers)):        #This iterates over the list from ith position till the length of the list(as here 6)
        
        for j in range(i+1,len(numbers)):#This iterates over the list from (i+1)th positiontill the length of the list
            
            if(numbers[j] <  numbers[i]):#will compare the values present in ith and (i+1)th positions
                t = numbers[j]           #the lowest value will be stored to a temporary variable
                
                numbers[j]=numbers[i]    #the highest value will be moved to the jth postion
                
                numbers[i]=t             #the lowest value will be swaped to ith position
                
                                         
    
    return (numbers)

''' 2. Bubblesort (2 Points)

Modify the function bubble_sort() so that it accepts an optional keyword 
argument that indicates whether the list should be sorted in
ascending or descending order. You are not allowed to use the sorted()
or the sort() function provided by Python.
'''

def bubble_sort2(numbers, ascending=True):#This function should return a ascending sorted value  when keyword is True

    for i in range(len(numbers)):
    
        for j in range(i+1,len(numbers)):
        
        
            if(numbers[i] <  numbers[j]):



                 t = numbers[i]
                 numbers[i]=numbers[j]
                 numbers[j]=t
    if ascending:                         #This will look for the keyword is true or not if true will rverse the list
        numbers.reverse()
        return(numbers)
    else:
        return(numbers)                   #This will return the descending order of the given list


''' 3. 
	a) Implement one of the following in-place sorting algorithms: (4 Points)
	Explanation of the algorithms see lecture / slides.
	The full 6 points will only be awarded if the steps of the algorithm are
	sufficiently commented!
	i) Mergesort
	ii) Quicksort

	b) Execute your selected algorithm with pen & paper (similar to how
	we looked at it in the lecture - see slides) for the following
	list: b = [9, 3, 6, 2, 7, 8, 1]
'''

def mergesort(numbers):
    pass

def quicksort(numbers):

    b=[]                    #This creates a Empty list to store the values lesser than pivot
    c=[]                    #This creates a empty list to store the  values greater than pivot
    
    
    if len(numbers) <= 1:   #will return the same list since its lemgth less than 1
        return numbers
    
    
    for i in numbers[1:]:   #Iterates over the list from first index till the length of the list
        
        if (i < numbers[0]):#number[0] will be taken as Pivot and compred for lesser value 
            
            b.append(i)     #numbers will be appended to the empty list b
            
        else:               #This part will execute for the vslue higher than the Pivot
            
            c.append(i)     #numbers will be appended to the empty list c

    return quicksort(b)+numbers[0:1]+ quicksort(c)  #final list will be returned with the concatanation of all the lists    
            
