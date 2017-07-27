#There are multiple ways to index a datframe, including square brackets, loc, and iloc. 
#[] have limited functionality and are ideally used for 2D NumPy arrays
#In pandas loc can be used for indexing based on labels 
#In pandas iloc can be used for indexing based on integers 

#a simple dataframe 
import pandas as pd 
df = pd.read_csv('filename.csv', index_col = 'columnname')

#indexing using square brackets 
df['columnname']['rowname'] 

#indexing using column attribute and row label 
df.columnname['rowname']

#indexing using the .loc accessor 
df.loc['rowname', 'columnname']
#using .loc to select all rows, and some columns 
df.loc[:, 'columnnamea':'columnnamef']
#using .loc to select some rows and all columns 
df.loc['rownamea':'rownamef', :]
#using .loc to select some rows and some columns 
df.loc['rownamea':'rownamef' , 'columnanmea':'columnnamef'] 
#selecting columns using lists and rows via slice 
df.loc['rownamea':'rownamef', ['columnnamea', 'columnnameb']

#indexing using the iloc accessor 
df.iloc[#row, #column] 
#using iloc to select a block from the middle of the Dataframe 
df.iloc[2:5, 1:]
#using lists rather than slices 
df.iloc[0,4,5], 0:2]

#selecting a single column 
df['columnname']

#selecting only specific columns 
df_new = df[['columnamea', columnnameb']]

#selecting a slice from a column 
df['columnname'][#rowstart:#rowafterend]

#selecting a single value from a column 
df['columnname'][#row]

#series versus 1-column DataFrame 
#a series 
df['columnname']
#a DataFrame with a single column 
df{{'columnname']]

