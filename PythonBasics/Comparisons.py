#Comparions use == for equal, where = is used in Python to assign variables 

2 < 3 
#output True 

2 == 3 
# output False 

2 <= 3 
#output True 

2 != 3 
#output True

3 <= 3 
#output True 

x = 2 
y = 3 
x < y 
#output True 

'carl' < 'chris'
#output True 

3 < 'chris'
#error message 

3 < 4.1
#output True 

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_heigh ** 2 
bmi > 23
#[output] array([False, False, True, False], dtype=bool) 
