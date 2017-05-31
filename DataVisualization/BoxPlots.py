#Box plots allow you to visualize summary statistics including outliers, min/max, 25th, 50th and 75th percentiles. 
df.boxplot(column='columnames', by = 'columname')
plt.show()

#or

import pandas as pd
import matplotlib.pyplot as plt 
df.boxplot(column='columnname',by= 'columnname', rot = 90)
plt.show()
