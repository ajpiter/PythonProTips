#Pandas dataframes have columns that are a series, and share a common index. 
#When a series of an index represents dates and times, it is a time series. 
#Pandas timeseries can be sliced using strings. 

#slices all time series data from one day 
columnname['2010-07-04']

#slices all time series data from one month 
columnname['2010-05']

#slices all time series data from two months 
columnname['2010-03':'2010-04']

variable = dataframe['columnname']
#extract march and april only 
variableb = variable['2010-03:'2010-04']
variableb.shape 
#extract the last four measurements from a time series 
variableb.iloc[-4:] 
