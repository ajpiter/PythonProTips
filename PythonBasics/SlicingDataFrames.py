#Slicing in Pandas allows you to determine which rows, or columns of the dataframe you see. 

dataframe.iloc[row, column] 
dataframe.iloc[startrow:endrow, startcolumn:endcolumn]

#To see the first five rows 
dataframe.iloc[:5,:]

# : start from the begining or go to the end
# - start from the end

#To see the last five rows 
dataframe.iloc[-5:,:]
