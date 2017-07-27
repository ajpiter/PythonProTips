#A DataFrame is a 2 dimensional numPy array, whose columns are series. 
#Dataframes can be built from Dictionaries. Below we construct a dictionary of lists. 

import pandas as pd 
#keys are used as column labels 
dictionary = {'key':['0','1','2','3'],'key2':['a','b','c','d']}
#with no indexes specified row indexes start with zero by default 
dataframe = pd.DataFrame(dictionary)

#OR
#We can create DataFrames using lists for the column data. 

import pandas as pd 
list = ['0','1','2','3']
listb = ['a','b','c','d']
#contains the column labels 
listlabels = ['list','listb']
#contains the column entries for each column 
listcols = [list, listb] 

#When outputed the rows of a dataframe are observations and the columns are variables. 
#The keys of a dictionary are the column labels. 
#To add row labels call dictionary.index = ['label', 'labelb', 'labelc', labeld']

variable 
dictionary = { 
 "country":["Brazil", "Russia", "India", "China", "South Africa"],
 "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
 "area":[8.516, 17.10, 3.286, 9.597, 1.221]
 "population":[200.4, 143.5, 1252, 1357, 52.98] }
import pandas as pd
variable = pd.DataFrame(dictionary) 
dictionary.index = ['label', 'labelb', 'labelc', 'labeld']
