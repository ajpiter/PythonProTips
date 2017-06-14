#Greyscale images are stored as 2d arrays with values 0 to 1. 
#Color images are stored as 3,2d arrays, one for for each color channel, RGB(Red, Green, Blue) either as: 
# 0 to 1 as a floating point or 
# 0 to 255 as 8 bit intergers
#The resulting array is still 2d and plotted as 2d image

import matplotlib.pyplot as plt 
#imread() loads the image 
variable = plt.imread('imagetitle.jpg')
print(variable.shape)
#imshow() displays the image 
plt.imshow(variable)
plt.axis('off')
plt.show()
