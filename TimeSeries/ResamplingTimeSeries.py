#Resampling can be done to slow or speed up frequency. 
#Down-sampling is done to reduce date time rows to slow down frequency 
#Up-sampling is done to increase date-time rows to increase frequency 

import pandas as pd 
variable = pd.read_csv('filename.csv', parse_dates = True, index_col='columnname')
variable.head()
variable.info()
