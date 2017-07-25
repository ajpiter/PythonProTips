#Lists all the unique variables in a single column 
dataframe['columnname'].unique()

#Filtering by column name 
variable = dataframe['columnname'] == 'variablefromcolumn'

#Creating a new dataframe from that filter
newvariable = dataframe.loc[variable,:]

#Checking to ensure the column only has variablefromcolumn as values 
dataframe['columnname'].unique() 
