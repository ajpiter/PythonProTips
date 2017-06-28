#Swarm plots, unlike strip plots automatically show points representing repeated values to avoid overlap. 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.swarmplot(x='columnname'. y='columnnameb', data=dataframe)
plt.ylabel('Label')
plt.show()

#You can group the data further by making dots different colors based on variables in a specified column using the argument hue=
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.swarmplot(x='columnname', y='columnnameb', data=dataframe, hue='columnnamec')
plt.ylabel('Label')
plt.show()

#You can also change the orientation by using the argument orient='h'
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#load the dataset 
variable = sns.load_dataset('nameoffile')
sns.swarmplot(x='columname', y='columnnameb', data=dataframe, hue='columnnamec', orient='h')
plt.xlabel('Label')
plt.show()
