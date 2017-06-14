#Strip Plots draws values on a number line to visualize samples of a single variable

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.stripplot(y='columnname', data=variable)
plt.ylabel('Label')
plt.show()

#You can draw parrell strip plots for each variable in x 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.stripplot(x='columnname', y ='columnnameb', data=variable)
plt.ylabel('Label')
plt.show()

#In a strip plot repeated values are drawn ontop of each other. 
#To show repeated values you can add the arguments size= and jitter=True or use a swarm plot. 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.stripplot(x='columnname', y='columnnameb', data=variable, size=4, jitter=True)
plt.ylabel('Label')
plt.show()
