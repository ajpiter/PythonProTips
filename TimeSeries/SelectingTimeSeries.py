#You can select data based on it's time series

#To select the data from a single date and time in a particular column 
dataframe.loc['yyyy-mm-dd hh:mm:ss', 'Columnname']

#To select the entire day 
dataframe.loc['yyyy-mm-dd']

#You can also do partial dates and times 
dataframe.loc['yyyy-m'] #for the whole month 
dataframe.loc['yyyy'] #for the entire year 

#You can also use a slice to select multiple dates and time together 
dataframe.loc['yyyy-mm-01' : 'yyyy-mm-08'] #To select a week 
dataframe.loc['yyyy-01' : 'yyyy-04'] #To select the first quarter of the year 
