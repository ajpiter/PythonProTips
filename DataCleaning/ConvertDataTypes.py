# To find data types 
print(dataframe.dtypes) 
type(variable) 

#You can always get info on a dataframe, before or after you make changes by using 
print(dataframe.info())

----- #Convert Data Types ----- 

#Functions to Convert Data Types in Base Python 
int()
float()
bool()
str()
variable = str(variable) 
print("Convert to non-strings " + str(number) + " to add in print statement.") 

----- #Convert a Column of Data ----- 
#To convert data to numeric 
dataframe.columnname = pd.to_numeric(dataframe.columnname)

# To convert data from one type to another, 
dataframe['columnname'] = dataframe['columnname'].astype(typetoconvertto)

# For example, a string.   
dataframe['columnname'] = dataframe['columnname'].astype(str)

#Converting data to the data type category makes a dataframe smaller in memory, and is useful in libraries that use categoricial data. 
dataframe['columnname'] = dataframe['columnname'].astype('category')

#If you expect a column to have a numeric datatype and it comes back as a string, it is probably because there are symbols/charcters for missing data. 
#If you change into numeric, invaild vaules in the column will be set as NaN missing value. 
dataframe['columnname'] = pd.to-numeric(df['columnname'], errors = 'coerce') dataframe.dtypes

----- #Adding Data Types -----
#When adding float and int datatypes the result is a float

#converting a float to an int truncates the fractional part of the number
