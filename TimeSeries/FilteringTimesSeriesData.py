import pandas as pd
#parse_dates['Date'] converts the column from strings to datetime objects 
variable = pd.read_csv('filename.csv', parse_dates=['Date']
variable.head()

#To transfer all the values in a column to upper case
database['Columnname'].str.upper()

#which rows have strings that contain the supplied substring 
#Results come back as a True/False Boolean 
database['Columnname'].str.contains('search') 

#Boolean aritmetic 
#In python the boolean value of True = 1 and False = 0 
#We can add up all the true values in a column
database['Columnname'].str.contains('search').sum()

#To extract the hour of the day from the date column 
datebase['columnname'].dt.hour 

#To convert time zones 
#first localize to the timezone that the data is in, in this case central 
central = database['colunname'].dt.tz_localize('US/Central')
central 
#convert to US Eastern time zone 
central.dt.tz_convert('US/Eastern')

#OR you can localize and convert time zones in one line 
database['columnname'].dt.tz_localize('US/Central').dt.tz_convert('US/Easterm')
