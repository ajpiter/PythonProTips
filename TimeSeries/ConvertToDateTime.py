import pandas as pd
#parse_dates['Date'] converts the column from strings to datetime objects 
variable = pd.read_csv('filename.csv', parse_dates=['Date']
variable.head()

#OR TO convert indivdual strings to datetime
variable = pd.to_datetime(['yyyy-mm-dd hh:ss', 'yyyy-mm-dd hh:ss', 'yyyy-mm-dd hh:ss'])

