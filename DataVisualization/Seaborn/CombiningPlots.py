#To combine different types of plots overlaid in the same visualization. 
#For example, a swarm plot and a violin plot. 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.violinplot(x='columnname', y='columnnameb', data=variable, inner=None, color='lightgray')
sns.stripplot(x='columnname', y='columnnameb', data=variable, size=4, jitter=True)

plt.ylabel('Label')
plt.xlabel('Label') 
Plt.show()
