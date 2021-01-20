----- #Common mathematical operators inlcude: ----- 

#Addition: + 
#Subtraction: - 
#Multiplication: * 
#Rasing to Power: **

#Floating Point Division vs. Integer Division 
#Division, returns a float down to decimal: /
#Integer Division, returns a whole interger number: // 
#Returns the remainder: % 

----- #Math Summaries of a Dataframe ----- 

#Describe provides summary information on the dataset including: 
#Count, Mean, Standard Deviation (std), min, 1st quartile, mean/2nd quartile, 3rd quartile, and max
dataframe.describe() 

#Count is the number of entries 
dataframe.count()
#or for just one column 
dataframe['columnname'].count()
#or multiple columns as a list 
dataframe[['columnname', 'columnnameb', 'columnnamec']].count()

#Min and Max 
dataframe.min()
dataframe.max()

#Mean 
dataframe.mean()
#one column in a dataframe 
dataframe['columnname'].count()
#or use indexes to specifiy columns, and/or rows. 
np.mean(dataframe[:,0]

#Medians 
dataframe.median()        
#use numpy and indexes to specify columns, and/or rows. 
np.median(dataframe[:,0])
        
----- #SqRt, Variance & Standard Deviations ----- 
        
#Square Root 
np.sqrt(variable)
#corrcoef
np.corrcoef(dataframe[:, 0], dataframe[:,1])

#Variance is a measure of the spread of the data
#Calculated by the mean squared distance of the data from the mean       
np.var(columnname) 

#Standard Deviations 
#Calculated by taking the square root of the vairance        
dataframe.std()
#one column in a dataframe
np.std(columnname)         
dataframe['columnname'].std()
#the standard deviation of a specific slice of a dataframe 
np.std(dataframe[:,0])

----- #Quartile Math ----- 
        
#1st Quartile
q1 = .25
dataframe.quartile(q1)
#3rd quartile
q3 = .75 
dataframe.quartile(q3)

#Inter-quartile ranges (IQR)
qRange = [0.25, 0.75]
dataframe.quartile(qRange)
        
# for 1st and 3rd quartiles plus the median 
np.percentile(dataset['columnname'], [25,50,75])

----- #Numpy Math -----

np.mean(np_array[:,0])
np.median(np_array[:,0])
np.corrcoef(np_array[:,0], np_array[:,1])
np.std(np_array[:,0])

# for 1st and 3rd quartiles plus the median 
np.percentile(dataset['columnname'], [25,50,75])

#The variance is the mean squared distance of the data from the mean, or a measure of the spread of the data
np.var(columnname) 

#computing the standard deviation, or the square root of the variance 
np.std(columnname)

#Square Root 
np.sqrt(variable)
