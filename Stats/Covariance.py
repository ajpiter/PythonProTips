
#How two quanites compare together using a scatter plot 
plt.plot(columnname/1000, columnname, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()

#Covariance is a measure of how two quanities vary together 
#If you have two datasets you can measure the mean of both datasets 
#If you select a single point, you can measure the differences bewteen the mean and the point
#Coviance is The mean of the product of these differences 

#Positive Covariance occurs when the point is above, or below both means 
#If x is high so is y 
#Meaning they are positivily correlated

#If x is high while y is low, or y is high while x is low 
#The covariance is negative and the data is negativly correlated

# Compute the covariance matrix: covariance_matrix
import numpy as np 
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)
# Print covariance matrix
print(covariance_matrix)
# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0,1]
# Print the length/width covariance
print(petal_cov)

#Pearson correlation coefficient 
#A measue of how two variables depend on each other, without any units 
#Divide the covariance by the standard deviations of x and y variables 
#Ranges from -1 to 1. a value of 0 means there is no correlation bewteen the data 

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)
    # Return entry [0,1]
    return corr_mat[0,1]
# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)
# Print the result
print(r)
