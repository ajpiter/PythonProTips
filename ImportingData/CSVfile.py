#Use Pandas for data analysis and modeling. 
#Pandas allows you to carry out the entire data anaysis workflow in Python without switching to R. 
#It is a best practice to use Pandas to import flat files as data frames. 

#A DataFrame is the pythonic analog of R's dataframe. A dataframe has observations and variables as opposed to rows and columns. 

import pandas as pd 
filenamevariable = 'filename.csv'
data = pd.read_csv(filename.csv)
data.head()

#.head() checks the first five rows of the data frame including the header. 

#To print the header 
import pandas as pd 
filenamevariable = 'filename.csv'
df = pd.read_csv('filename.csv')
print(df.head())

#To print the first five rows without a header. 
import pandas as pd 
filenamevariable = 'filename.csv'
data = pd.read_csv('filename.csv', nrows = 5, header = None)
