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
