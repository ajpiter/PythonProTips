#Meshgrid replicates 1D grid arrays along different axis to make 2D arrays. 
#They have identical shape but are constant vauled on different axis. 
#The entries of X, and Y correspond to the rectangular coordinates of a grid. 

#using meshgrid()
import numpy as np 
import matplotlib.pyplot as plt 

#creates two, 1D arrays of uniform vaules 
#The array u should contain 3 values uniformly spaced beween -2 and +2.
#The array v should contain 5 values uniformly spaced between -1 and +1.
u = np.linspace(-2, 2, 3) 
v = np.linspace(-1, 1, 5)

#creates a 2D array
x,y = np.meshgrid(u,v) 

#fills every entry of a 2D array 
z = x**2/25 + y**2/4 

#prints the array 
print('z:\n', z)

#displays the line as a image 
plt.set_cmap('gray')
plt.pcolor(z)
plt.show()

#saves the file
plt.savefig('filename.png')
