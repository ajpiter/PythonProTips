import numpy as np 
sex = np.array(['M', 'M', 'F', 'F', 'M'])
height = np.array ([68, 72, 64, 69, 65])
femaleheight = height[sex != 'M']
print(femaleheight)
