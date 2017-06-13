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
