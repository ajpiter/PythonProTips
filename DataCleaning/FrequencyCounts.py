#Select the column that you want to count 
#dropna lets you know the counts of missing values 
df.columnname.value_counts(dropna=False)

#you can also get frequency counts by using bracket notation, which is helpful when column names have spaces, special characters, or the same name as a python function.
df['columnname'].value_counts(dropna=False)

#you can also load the header function to get the frequency counts for the first five rows 
df.columnname.value_counts(dropna=False).head
