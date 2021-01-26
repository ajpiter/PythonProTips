#Broadcasting is assigning scalar value using a column slice to each row. 

#For example, in this NaN to every 3rd row. 
dataframe.iloc[::3, -1] = np.nan
