import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

variable = dataframe('columnname')
plt.plot(variable['2010-01'], color='red', label='labelname')
variableb = dataframe['columnb']
plt.plot(variableb['2010-01'], color='blue', label='labelname']
plt.legend(loc='upper right')
plt.xticks(rotation=60)
plt.show()

#selecting and formating dates with formated labels 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

variable = dataframe['2010-01']
#picks every 4th day, since the data is collected hourly 
variableb = variable.index[::96]
print(variableb)
labels = variableb.strftime('%b%d')
print(labels)
plt.plot(variableb['2010-01'], color='blue', label='labelname']
plt.legend(loc='upper right')
plt.xticks(dates, labels, rotation=60)
plt.show()
