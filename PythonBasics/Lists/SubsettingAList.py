#When subsetting a list containing the interger numbers 1,2,3,4 and 5 you can call for the subset of the value at position 1 as follows. 
#remember to index from 0 

list 
array([1,2,3,4,5])
list[1]
#output would be 2

#You can determine which values in your list are greater than a specific vaule by: 
list > 4
array([False, False, False, False, True])

#You can get the location in the array of the value greater than a specific number by:
list[list > 4] 
array([5])
