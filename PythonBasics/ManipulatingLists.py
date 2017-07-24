#To manipulate or change list elements 

#To change a single element in a list 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist[4] = 'z'
#output of basiclist would be ['a', 1, 'b', 2, 'z', 3] 

#To change multiple elements 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist[0:2] = ['z', 26] 
#output of basiclist would be ['z', 26, 'b', 2, 'c', 3] 

#To add elements to a list 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist + ['d', 4] 
#output of basiclist would be ['a', 1, 'b', 2, 'c', 3, 'd', 4] 

#To remove elements from a list
basiclist = ['a', 1, 'b', 2, 'c', 3] 
del(basiclist[5]
#output of basiclist would be ['a', 1, 'b', 2, 'c']
