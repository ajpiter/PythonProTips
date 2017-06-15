#Violin plots show curved distrubtions wrapped around a box plot rather than discrete points 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

plt.subplot(1,,2,3)
sns.violinplot(x='columnname', y='columnname2', data=variable) 
plt.ylabel('Label')
plt.xlabel('Label') 
plt.tight_layout()
Plt.show()
