#To convert time zones 
#first localize to the timezone that the data is in, in this case central 
central = database['colunname'].dt.tz_localize('US/Central')
central 
#convert to US Eastern time zone 
central.dt.tz_convert('US/Eastern')

#OR you can localize and convert time zones in one line 
database['columnname'].dt.tz_localize('US/Central').dt.tz_convert('US/Easterm'
