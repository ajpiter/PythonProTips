#You can use the seaborn styling package to customize the historgram 
#to make the style seaborns default use sns.set() function 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set()
_ = plt.hist(dataframe['columnname'])
_ = plt.xlabel('Label')
_ = plt.ylabel('Label')
plt.show()
