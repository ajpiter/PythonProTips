#use pandas to combine multiple data files
#the methods belwo are to indivdual concatenate files, you can also use globbing to concatenate multiple files.

import pandas as pd 
concatenated = pd.concat ([dataframea, dataframeb])

#Row Index labels will keep orginal labels unless you rest the index label. 
#To reset the row index label 

pd.concat([dataframea, dataframeb], ignore_index = True)

#axis = 0 is the default, and for row wise concatenation 
#axis = 1 is for column wise concatenation 

newdataframe = pd.concat([dataframea, dataframeb], axis = 1) 
print(newdataframe.shape) 
print(newdataframe.head())

