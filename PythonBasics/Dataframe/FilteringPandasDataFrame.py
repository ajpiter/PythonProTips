#Example below of how to filter a dataframe based on values in one column.  

import pandas as pd 
dataframe = pd.read_csv('filename.csv', index_col = 0) 
variable = dataframe['columnname'] > 8 
variable 
#output would be a boolean statement (True or False) on whether each value in the columnname is greater than 8 

dataframe[variable]
#output would be the entire row where the value in columnname was greater than 8 
