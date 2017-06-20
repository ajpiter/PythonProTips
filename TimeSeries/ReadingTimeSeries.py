#To use Pandas to read time series data, specifiy parse_dates =True
#dates will be formated as yyyy-mm-dd hh:mm:ss

import pandas as pd 
variable = pd.read_csv('filename.csv', parse_dates=True, index-col='columnname')

#you can use .head() to see the first five rows to see if you 
