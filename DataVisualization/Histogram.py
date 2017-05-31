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

#Histograms for data cleaning 
#In addition to data visualization, the use histograms can be used as a way to spot outliers and errors in continous data and plan your data cleaning steps

df.columnname.plot('hist')
import matplotlib.pyplot as plt 
plt.show 

#Looking at a histogram plot on a log scale allows you to adjust data when there is an extremly large difference bewteen the min and max. 
import matplotlib.pypplot as plt 
df['columnname'].plot(kind = 'hist', rot = 70, logx = True, logy = True)
plt.show

#You can identify the error by returning all data points in a column over a certain value.
#Although not all outliers are bad data points, some are valid values.
df.df.columnname > 1000000
