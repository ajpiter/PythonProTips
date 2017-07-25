#Describe provides summary information on the dataset including: 
#Count, Mean, Standard Deviation (std), min, 1st quartile, mean/2nd quartile, 3rd quartile, and max
#There are multiple methods for calculating basic stats below.

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

#Standard Deviations 
dataframe.std()
#one column in a dataframe
dataframe['columnname'].std()
#the standard deviation of a specific slice of a dataframe 
np.std(dataframe[:,0])

#Quartiles
#1st Quartile
q = .25
dataframe.quartile(q)
#3rd quartile
q = .75 
dataframe.quartile(q)

#Inter-quartile ranges (IQR)
q = [0.25, 0.75]
dataframe.quartile(q)

#corrcoef
np.corrcoef(dataframe[:, 0], dataframe[:,1])

