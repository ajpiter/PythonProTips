#which rows have strings that contain the supplied substring 
#Results come back as a True/False Boolean 
database['Columnname'].str.contains('search') 

#Boolean aritmetic 
#In python the boolean value of True = 1 and False = 0 
#We can add up all the true values in a column
database['Columnname'].str.contains('search').sum()
