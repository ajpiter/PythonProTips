#The process of organizing, plotting, and summarizing a data set 

#Graphicial Exploratory Data Analysis, involves taking data from a table, and converting it into a graph
#Below is how to take a table and convert it into a histogram
#for EDA _ are used as a placeholder(dummy variable) when you don't care about the variable 

import matplotlib.pyplot as plt 
_ = plt.hist(dataframe['columnname'])
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()

#Customize the bins, by calling bin_edges, and the calling bins=bin_edges
import matplotlib.pyplot as plt 
bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
_ plt.hist(dataframe['columnname'], bins=bin_edges)
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()

#Or use the bins keyword argument to specify the number of bins. 
import matplotlib.pyplot as plt 
bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
_ plt.hist(dataframe['columnname'], bins=20)
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()

#You can use the seaborn styling package to customize the historgram 
#to make the style seaborns default use sns.set() function 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set()
_ = plt.hist(dataframe['columnname'])
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()
