#To create a dataframe from a CSV file 
import pandas as pd 
dataframe = pd.read_csv('filename.csv")

#To create a dataframe from a CSV file using the first column as column labels
import pandas as pd 
dataframe = pd.read_csv('filename.csv', index_col = 0) 
