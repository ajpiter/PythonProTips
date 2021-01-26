#To select a specific portion of a NumPy array you can subset based one either the columns, the rows or both. 

variable = np.array([[1,1,1,1,1], [25,26,27,28,29]])
variable.shape
#output (2,5) 

#To return an entire row, choose the index number that matches the row. 
variable[0]
#output array([1,1,1,1,1]) 

#To return a single value choose the corresponding index value for the row and column. 
variable[1][2]
#output would be 27 

#This also returns the same value 
variable[1,2]
#output is 27 

#To select all rows and specific columns use : for rows and the corresponding index for the columns. 
variable [:, 1:3]
#output is array([[1,1], 
                 [26,27]])

#To select a specific row and all columns 
variable[1, :]
#output array([25, 26, 27, 28, 29]) 
