
#The NumPy package is an easy and fast alternative to python lists and can make calculations over entire arrays. 
#Convert to a NumPy array when doing calculations bewteen two different types, such as list and int. 
#NumPy arrays contain only one type 

#Import the whole NumPy package. 
import numpy as np
np.array([1,2,3])

#Import just the array. 
from numpy import array 
varaiable = array(file)

#Import with a clear use of package 
import numpy 
varaiable = numpy.array(file)

#You can create a 2D NumPy Array by 
#variable = np.array([list one], [list two])
variable = np.array([[1,1,1,1,1], [25,26,27,28,29]])

#You could find out the shape of a NumPy array using variable.shape
variable = np.array([[1,1,1,1,1], [25,26,27,28,29]])
variable.shape
# output (2,5) for two rows and five columns of data

#Remember that numPy arrays have to be of the same type (str, list, int, bool etc) 
