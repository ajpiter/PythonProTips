#A historgram with a cumulative distrubution function or CDF plots the total for each bin, and all the lower bins. 
#This plot creates a ramp shape as opposed to the traditional bell curve in a histogram. 

variable.plot(y='columnname', kind='hist', bins=30, range=(4,8), cumulative=True, normed=True)
plt.title('Title')
plt.xlabel('Label')
plt.ylabel('Label')
plt.show()
