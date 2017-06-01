#Globbing uses pattern mattching for file names to concatenate multiple files. 
#Returning a list of file names that can be used to build into DataFrames. 
# * allows any character(s) in a file name to be matched
# ? only allows one character to match 

#Anycsv = '*.csv'
#anycharacter = 'file_?.csv' 

import pandas as pd 
import glob
csvfiles = glob.glob('*.csvs')
print(csvfiles)
listdata = [] #emptylist 
for filename in csvfiles:
    data = pd.read_csv(filename) 
    listdata.append(data)
variable = pd.concat(listdata)
print(variable.shape)
print(variable.head())
