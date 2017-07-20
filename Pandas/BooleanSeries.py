#Creating a Boolean Series 
df.columnname > 60 

#filtering with a Boolean Series 
df[df.columnname > 60] 
variable = df.columnname > 60 
df[variable] 

#combining filters based on both conditions 
df[(df.columnname >= 50) & (df.columnnameb < 200)] 

#combining filters based on either condition 
df[(df.columnname >= 50) | (df.columnnameb < 200)]

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



