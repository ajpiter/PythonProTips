
#To get rid of duplicates use drop_duplicates()
dataframe = dataframe.drop_duplicates()

#To get a count of NaN missing vaules
dataframe.info()

#To drop missing values 
dataframedroppedmissing = dataframe.dropped()

#Fill missing values with fillna from one column
dataframe['columnnamea'] = dataframe['columnnamea'].fillna('whattoreplacemissingvalueswith')

#Fill missing values with fillna from multiple columns 
dataframe[['columna', 'columnb']] = dataframe[['columna', 'columnb']].fillna(whattoreplacemissingvaluewith')

#Fill missing values with statistic such as mean or medium. Be careful for outliers when deciding what to replace the missing values with.
mean_value = dataframe['columnname'].mean()
print(dataframenewname) 
dataframe['columnname'] = dataframe['columnname'].fillna(mean_value)
print(dataframe.info())
