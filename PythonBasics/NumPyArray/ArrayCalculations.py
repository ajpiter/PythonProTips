#Examples taken from DataCamp 

----- #Example: Basic Math with Indivdual Outputs ----- 
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
for val in bmi :
 print(val)
 
#Output 
#21.852
#20.975
#21.750
#24.747
#21.441

----- #Example: Basic Math with Array Outputs ----- 
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in meas :
 print(val)

#Output
#[ 1.73 1.68 1.71 1.89 1.79]
#[ 65.4 59.2 63.6 88.4 68.7]

----- #Example: Comparisons with Array Outputs ----- 
import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_heigh ** 2 
bmi > 23
#[output] array([False, False, True, False], dtype=bool) 

----- #Example: Logical Comparisons with Array Outputs ----- 
---- #Example: logical_and() ----- 
np.logical_and(variable > 21, variable < 25) 
#[output] TRUE
np.logival_and(array > 21, array < 25) 
#[output] array([True, False, True, True], dtype=bool)

#Could use logical_and(), logical_or(), or logical_not() functions 
