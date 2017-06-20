#To create a line plot using pandas 

import pandas as pd 
import matplotlib.pyplot as plt 
variable = pd.read_csv('file.csv') 
print(variable.shape)
variable.head()
varaibale.plot(x='columnname', y='columnname2') 
plt.show()
