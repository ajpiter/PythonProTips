#to convert the image from color to greyscale you can avaerage the RGB channels 

import matplotlib.pyplot as plt 
#imread() loads the image 
variable = plt.imread('imagetitle.jpg')
variable = img.mean(axis=2)
print(variable.shape)
#imshow() displays the image 
plt.imshow(variable)
plt.axis('off')
plt.show()

#Another way to convert the image from color to greyscale is to set the colormap 

variable = plt.imread('480px-Astronaut-EVA.jpg')
print(variable.shape)
variableb = variable.sum(axis=2)
print(intensity.shape)
plt.imshow(variableb, cmap='gray')
plt.colorbar()
plt.axis('off')
plt.show()
