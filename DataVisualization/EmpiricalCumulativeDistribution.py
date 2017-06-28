#plotting Empliricial cumulative distribution functions(ECDF)
#An x value of an edcf is the quanity that you are measuring 
#The y axis is evenly spaced datapoints with a maxium of 1 

import numpy as np 
x = np.sort(dataset['columnname'])
y = np.arrange (1, len(x)+1) / len(x)
#plots dots instead of lines 
_ = plt.plot(x,y, marker='.', linestyle='none') 
_ = plt.xlabel('Label') 
_ = plt.ylabel('Label') 
#Keeps data off the plot edges, with a 2% buffer
plt.margins(0.02) 
plt.show()

"""Compute ECDF for a one-dimensional array of measurements."""
def ecdf(data):
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n
    return x, y

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')
plt.show()
