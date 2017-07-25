#To create a line plot using pandas 

import pandas as pd 
import matplotlib.pyplot as plt 
variable = pd.read_csv('file.csv') 
print(variable.shape)
variable.head()
variable.plot(x='columnname', y='columnname2') 
plt.show()

#To create a line plot using Matplotlib 
import matplotlib.pyplot as plt 
lista = [2001, 2002, 2003, 2004]  
listb = [1, 2, 3, 4] 
plt.plot(lista, listb) 
plt.show()
