#In 2d you can have multiple shapes, including rectangles using plt.hist2d()
#Where x, and y are 1d arrays of the same length. 

import matplotlib.pyplot as plt 
plt.hist2d(x,y,bins=(10,20))
plt.colorbar()
plt.xlabel('label') 
plt.ylabel('label') 
plt.title('Title')
plt.show()

#You can change the range of the histogram by
import matplotlib.pyplot as plt 
plt.hist2d(x,y,bins=(10,20), range= ((xmin,xmax),(ymin,ymax)))
plt.colorbar()
plt.xlabel('label') 
plt.ylabel('label') 
plt.title('Title')
plt.show()
