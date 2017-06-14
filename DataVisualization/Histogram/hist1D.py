#Histograms are the perferred format for 1D. 
#choose bins/intervals 
#In 1D plotting in stright line segments are the only opition 

import matplotlib.pyplot as plt
counts, bins, patches = plt.hist(x, bins=25)
plt.colorbar()
plt.xlabel('label')
plt.ylabel('label')
plt.title('Title')
plt.show()

