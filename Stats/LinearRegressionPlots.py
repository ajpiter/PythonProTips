#Linear Regression Plots are a stright line through a scatter plot 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
#plot the points and regression line 
sns.lmplot(x='columnname', y='columnnameb', data=variable)
plot.show()

#To plot in different colors on the same plot based on a column us the command hue= 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
variable = sns.load_dataset('nameoffile')
sns.lmplot=(x='columnname', y='columnnameb', data=variable, hue='columnnamec', palette='set1')
plt.show()

#To plot in seperate figures use the argument col= to produce a seperate plot for each column 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
variable = sns.load_dataset('nameoffile')
sns.lmplot(x='columnname', y='columnnameb', data=variable, col='columnnamec')
plt.show()
