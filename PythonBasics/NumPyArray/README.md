## Numpy Array's 

##### Numpy is a common package used in data science that creates a new data type Numpy Arrays 
##### Arrays are similar to lists but allows python to make calculations over the enitre array 
##### Arrays can only contain one data type, if you try to use multiple types they are all converted to strings 

### Creating an Numpy Array 

import numpy as np 
variable = 95 
NpArray = np.array([87.2, 43.9, 18.73]) 
NpArray
##### [output] array([87.2, 43.9, 18.73]) 

##### Math calculations can be done across an enitre array 
Calculation = NpArray / variable 

### Arrays instead of Dataframes 
import numpy as np 
NpArray = np.array([87.2, 43.9, 18.73], [82.5, 108.3, 47.6]) 
NpArray
##### [output] array([87.2, 43.9, 18.73]
               ##### [82.5, 108.3, 47.6]) 
               
NpArray.shape
##### [output] (2, 30) #indicating there are 2 rows and 3 columns 
