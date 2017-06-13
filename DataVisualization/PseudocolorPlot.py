#Use a pseudocolor plot rather than a grey scale to a evaulate a 2D function on a mesh grid. 

import numpy as np 
import matplotlib.pyplot as plt 
u = np.linspace(-2, 2, 65) 
v = np.linspace(-1, 1, 33) 
x,y = np.meshgrid(u,v)
z = x**2/25 + y**2/4

#pcolor stands for pseudocolor 
plt.pcolor(z)
#displays a color bar to the right of the grid 
plt.pcolorbar()
#gets rid of white space 
plt.axis('tight')
plt.show()

#To make a non pseudocolor plot replace plt.pcolor(z) with: 
plt.pcolor(z, cmap= 'grey') #for a grey scale color map 
plt.pcolor(z, cmap='autumn') #for a yellow to red color map 

#fix axis tick numbering by using mesh grid to create mesh ticks corresponding to the x and y coordinates 
plt.pcolor(x,y,z) #in place of plt.pcolor(z)
