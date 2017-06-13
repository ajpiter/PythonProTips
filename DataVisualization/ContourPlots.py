#Similar to pseudocolor blots, but used when the data varies continously. 
#Creates smooth curves representing data with constant values. 
#Used in topigraphical maps. 

#30 represents the number of contours 
plt.contour(z,30)

#You can also use x and y coordinates 
plt.contour(x,y,z,30)

#full code
import numpy as np 
import matplotlib.pyplot as plt 
u = np.linspace(-2, 2, 65) 
v = np.linspace(-1, 1, 33) 
x, y = np.meshgrid(u,v)
z = x**2/25 + y**2/4
plt.contour(x,y,z,30)
plt.colorbar()
plt.axis('tight') 
plt.show()

#Instead of just having lines at the contours you can fill them in using plt.contourf()
import numpy as np 
import matplotlib.pyplot as plt 
u = np.linspace(-2, 2, 65) 
v = np.linspace(-1, 1, 33) 
x, y = np.meshgrid(u,v)
z = x**2/25 + y**2/4
plt.contourf(x,y,z,30)
plt.colorbar()
plt.axis('tight') 
plt.show()
