#When adding two python lists the values of the second list are just amended to the values of the first list.
python_list + python_list 
[1,2,3,1,2,3]

#When adding two NumPy arrays the value of both lists are added to each other. 
### Adding Numpy Arrays 
numpy_array = np.array([1, 2, 3])
numpy_array + numpy_array
array([2,4,6])

#When adding a single number to a numpy array that number is added to every number in the array. 
import numpy as np 
m = np.array([2, 4, 6]) 
n = 2 
print(m + n) 
#the output is [4 6 8]
