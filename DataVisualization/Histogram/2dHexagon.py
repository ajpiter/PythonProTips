#You can also plot 2d hisograms using hexagon shapes 
#scalling on the vertical and horizital axis are not equal, so the hexagons are not drawn to scale. 

import matplotlib.pyplot as plt 
plt.hexbin(x,y, gridsize=(15,10), extent = (xmin, xmax, ymin, ymax))
plt.colorbar()
plt.xlabel('Label') 
plt.ylabel('Label') 
plt.show()
