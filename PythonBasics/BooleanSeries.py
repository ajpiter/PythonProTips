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
