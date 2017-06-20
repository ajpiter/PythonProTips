#Box plots allow you to visualize summary statistics including outliers, min/max, 25th, 50th and 75th percentiles. 

#To create a box plot using pandas 
import pandas as pd 
import matplotlib.pyplot as plt 
variable = pd.read_csv('file.csv') 
variable.plot(y = 'columnname', kind = 'box')
plt.xlabel('Label') 
plt.ylabel('Label')
plt.show()

#or 
variable.boxplot(column='columnames', by = 'columname')
plt.show()

#or
import pandas as pd
import matplotlib.pyplot as plt 
variable.boxplot(column='columnname',by= 'columnname', rot = 90)
plt.show()
