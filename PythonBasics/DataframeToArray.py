#NumPy is used for fast numeric array computations. 
#You can convert from Pandas DataFrame to NumPy Array by using the .values function 

# Import numpy
import numpy as np 

# Create array of DataFrame values:
numpyarray = dataframe.values

# Create new array of base 10 logarithm values:
numpyarray_log10 = np.log10(numpyarray)

# Create array of new DataFrame
dataframe_log10 = np.log10(dataframe)

# Print original and new data containers
print(type(numpyarray), type(numpyarray_log10))
print(type(dataframe), type(dataframe_log10))
