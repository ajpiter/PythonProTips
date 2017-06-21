#Resampling can be done to slow or speed up frequency. 
#Down-sampling is done to reduce date time rows to slow down frequency 
#Up-sampling is done to increase date-time rows to increase frequency 

#Specific letters pertain to what you will be resampling. 
""" min, T = minute
H = hour
D = day 
B = business day 
W = week 
M = month 
Q = quarter 
A = year """

#Down-Sampling 
import pandas as pd 
variable = pd.read_csv('filename.csv', parse_dates = True, index_col='columnname')
variable.head()
variable.info()
#aggregate the mean 
variablemean = variable.resample('D').mean()
#verify 
print(variablemean.loc['yyyy-mm-dd'])
print(variable.loc['yyyy-mm-dd', 'columnname'])
variable.loc['yyyy-mm-dd', 'columnname'].mean()

#method chaining with days and weeks 
variable.resample('D').sum()
variable.resample('D').sum().max()
variable.resample('W').count()

#multipling frequencies 
variable.loc[:, 'columnname'].resample('2W').sum()

#Up-Sampling 
newvariable = variable.loc['yyyy-mm-dd':'yyyy-mm-dd', 'columnname']
newvariable.resample('4H').ffill()
      
