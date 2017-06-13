#A series is a one dimensional numPy array, or columns of a dataframe. 
#A dataframe is a two dimensional numPy array, whose columns are series. 

variable = dataframe['sereies']
type(variable)
#pandas.core.series.series

#A series has it's own head method, and inherets it's name from the dataframe. 
column.head()

#To extract numericial entries 
newvariable = column.values 
