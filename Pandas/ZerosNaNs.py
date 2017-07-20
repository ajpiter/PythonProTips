#DataFrames with zeros and NaNs 
df2 = df.copy()
df2['columnname'] = [ 0,0, 50, 60, 70, 80] 
df2

#select columns with all nonzeros 
df2.loc[:, df2.all()] 

#select columns with any nonzeros 
df2.loc[:, df2.any()] 

#select columns with any NaNs 
df.loc[:, df.isnull().any()] 

#select columns without Nans 
df.loc[:, df.notnull().all()]

#Drop rows with any NaNs 
df.dropna(how = 'any') 

#filtering a column based on another 
df.columnname[df.columnnameb > 55] 

#modifying a column based on another 
df.columnname[df.columnnameb > 55] += 5 
