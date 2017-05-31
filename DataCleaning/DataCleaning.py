#Load Data 
import pandas as pd 
df = pd.read_csv('doc_name.csv')

#Load Header 
df.head()

#Load Tail (footer)
df.tail()

#Load Column Names. Column names are attributes so there are no parathesis needed. 
df.columns

#Load shape, which is represented by (rows, columns)
df.shape 

#Load info. Good for locating missing data. 
df.info()
