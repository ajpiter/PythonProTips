#Covariance is a measure of how two quanities vary together 
#If you have two datasets you can measure the mean of both datasets 
#If you select a single point, you can measure the differences bewteen the mean and the point
#Coviance is The mean of the product of these differences 

#Positive Covariance occurs when the point is above, or below both means 
#If x is high so is y 
#Meaning they are positivily correlated

#If x is high while y is low, or y is high while x is low 
#The covariance is negative and the data is negativly correlated

#Pearson correlation coefficient 
A measue of how two variables depend on each other, without any units 
#Divide the covariance by the standard deviations of x and y variables 
#Ranges from -1 to 1. a value of 0 means there is no correlation bewteen the data 

#How two quanites compare together using a scatter plot 
plt.plot(columnname/1000, columnname, marker='.', linestyle='none')
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
