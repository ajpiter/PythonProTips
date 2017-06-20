#Scatter plots are best used to show the relationship bewteen two numeric variables or 
#to flag potential errors not found by looking at one variable. 
#To create a scatter plot using pandas 

import pandas as pd 
import matplotlib.pyplot as plt 
variable = pd.read_csv('file.csv') 
variable.plot(x='columnname', y='columnname2', kind='scatter')
plt.xlabel('Label') 
plt.ylabel('Label')
plt.show()

#scatter plots can also have roatation 
variable.plot(kind = 'scatter', x = 'columnname', y = 'columnname', rot = 70)
plt.show()

#Scatter Plot of a Subset 
variable_subset.plot(kind = 'scatter', x = 'columnname', y = 'columnname', rot = 70)
plt.show()
