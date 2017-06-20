#Use pandas and matplotlib to create a historgram. 

import pandas as pd
import matplotlib.pyplot as plt 
filenamevariable = 'filename.txt'
data = pd.read_csv(file, sep = '\t', comment = '#', na_values = 'nothing')
print(data.head())

#select one column in the dataframe to plot 
pd.DataFrame.hist(data[['columnname']])

#Create labels for the x and y axis 
plt.xlabel('labelname')
plt.ylabel('labelname(subname)')
plt.show()
