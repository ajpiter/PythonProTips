import pandas as pd
#parse_dates['Date'] converts the column from strings to datetime objects 
variable = pd.read_csv('filename.csv', parse_dates=['Date']
variable.head()

#To transfer all the values in a column to upper case
database['Columnname'].str.upper()
