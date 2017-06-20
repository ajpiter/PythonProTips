#Use pandas and matplotlib to create a historgram. 

#Histogram using one column from a file 
import pandas as pd 
import matplotlib.pyplot as plt 
variable = pd.read_csv('file.csv')
variable.plot(kind = 'hist', y = 'columnname')
plt.show()

#Histogram using a tab deliminated file, were comments are indicated with "#' and missing values are 'nothing'
import pandas as pd
import matplotlib.pyplot as plt 
filenamevariable = 'filename.txt'
data = pd.read_csv(filenamevariable, sep = '\t', comment = '#', na_values = 'nothing')
print(data.head())
#select one column in the dataframe to plot 
pd.DataFrame.hist(data[['columnname']])
#Create labels for the x and y axis 
plt.xlabel('labelname')
plt.ylabel('labelname(subname)')
plt.show()

#Sidenote :/ 
#In pandas you can create a histogram using multiple functions.
#Each creates a histogram but the results differ slightly. 
datframe.plot(kind='hist')
dataframe.plt.hist()
dataframe.hist()
