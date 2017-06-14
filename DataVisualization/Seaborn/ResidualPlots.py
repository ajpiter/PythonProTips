#Residual Plots show how much the data misses the regression line 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.residplot(x='columnname', y='columnnameb', data=variable, color='indianred')
plt.show()

#residual plots have similar arguments to lmplot but 
#x, and y can by numPy arrays or strings 
# data argument is opitional 
#opitional arguments are consistant with matplotlib, for example color = 
