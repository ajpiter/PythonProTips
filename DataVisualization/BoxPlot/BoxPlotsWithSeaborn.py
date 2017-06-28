import matplotlib.pyplot as plt 
import seaborn as sns 
_ = sns.boxplot(x='columnname', y='columnname', data=dataset)
_ = plt.xlabel('Label') 
_ = plt.ylabel('Label') 
plt.show()
