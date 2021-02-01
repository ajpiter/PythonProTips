#To manipulate or change list elements 

#To change a single element in a list 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist[4] = 'z'
#output of basiclist would be ['a', 1, 'b', 2, 'z', 3] 

#To change multiple elements 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist[0:2] = ['z', 26] 
#output of basiclist would be ['z', 26, 'b', 2, 'c', 3] 

#To add an element to a list with .append()
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.append('d')
#output of basiclist would be ['a', 1, 'b', 2, 'c', 3, 'd']
# .append() only works to add a single element to a list 

#To add multiple elements to a list with .extend() 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.extend(['d', 4])
#output of basiclist would be ['a', 1, 'b', 2, 'c', 3, 'd', 4]

#To add elements to a list with += 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist += ['d', 4] 
#output of basiclist would be ['a', 1, 'b', 2, 'c', 3, 'd', 4] 

#To add elements to a new list 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
updatedlist = basiclist + ['d', 4]
#output of updatedlist would be ['a', 1, 'b', 2, 'c', 3, 'd', 4] 

#To remove specified elements from a list 
basiclist = ['a', 1, 'b', 2, 'c', 3]
basiclist.remove(3)
#output of basiclist would be ['a', 1, 'b', 2, 'c']

#To remove elements from a list by using the slice
basiclist = ['a', 1, 'b', 2, 'c', 3] 
del(basiclist[5])
#output of basiclist would be ['a', 1, 'b', 2, 'c']

#To reverse the elements in a list
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.reverse()
#output of y would be [3, 'c', 2, 'b', 1, 'a'] 

#To examin the lenght of a list 
basiclist = ['a', 1, 'b', 2, 'c', 3] 
len(basiclist) 
#output would be 6 

