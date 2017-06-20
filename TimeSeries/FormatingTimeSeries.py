#You can create specific formats for time series data and then convert your data to the format. 

# Prepare a format string: time_format
variabletimeformat = '%Y-%m-%d %H:%M'

# Convert variablelist into a datetime object
datetimeobject = pd.to_datetime(variablelist, format= variabletimeformat)  
