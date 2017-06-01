#Similar to joining tables in SQL. 
# #Combine datasets based on common columns. 
#If the column names are the same use on = columnname

import padas as pd 
pd.merge(left = dataseta, right = datasetb, on = columnname) 

#If the column names are different use the actual names of the columns

import pandas as pd 
pd.merge(left = dataseta, right = datasetb, on = None, left_on = 'columnname', right_on = 'columnnameb')
