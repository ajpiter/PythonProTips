#Box Plots show illstrations of values for a dataset including the min, max, median, 1st quartile, 3rd quartile and outliers. 

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

plt.subplot(1,,2,3)
sns.boxplot(x='columnname', y='columnname2', data=variable) 
plt.ylabel('Label')
plt.xlabel('Label') 
plt.tight_layout()
Plt.show()
