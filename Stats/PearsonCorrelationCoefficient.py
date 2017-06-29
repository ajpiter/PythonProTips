
#Pearson correlation coefficient 
A measue of how two variables depend on each other, without any units 
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
