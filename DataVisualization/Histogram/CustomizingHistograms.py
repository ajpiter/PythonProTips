#Hisograms can be further customized typically through bins, range, normed or cumulative. 
#bins indicate the number of intervals in the histogram 
#range indicates the min and max of the bins 
#normed is a boolean of whether to normalize a histogram 
#cumulative is computes the Cumulative Distrubution Function (CDF) 

#An example of a histogram using common customizations 

variable.plot(y='columnname', kind='hist', bins=30, range=(4,6), normed=True) 
plt.show()
