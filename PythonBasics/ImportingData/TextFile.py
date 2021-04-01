# Txt files are text file containing records in a table. 
#You can import as NumPy to store as NumPy array or pandas to store in dataframe. 
#NumPy is standard for storing numerica data, and is essential for other packages. 

#Load data
filenamevariable = 'filename.txt'
file = open(filenamevariable, mode = 'r')
#'r' is to read the file 
text = file.read()
file.close()
print(text)

#or to avoid having to close the file 
open('filename.txt', 'r') as file:
  print(file.read())

#Without a header. 
import numpy as np 
filenamevariable = 'filename.txt'
data = np.loadtext(filenamevariable, delimiter = ',')

#With a header
import numpy as np 
filenamevariable = 'filename.txt'
data = np.load.txt(filenamevariable, delimiter = ',', skiprows =1) 

#To load specific columns 
import numpy as np 
filenamevariable = 'filename.txt'
data = np.loadtxt(filenamevariable, delimiter = ',', skiprows = 1, usecols=[0,2])

#To load columns with specific data types 
import numpy as np 
filenamevariable = 'filename.txt'
data = np.loadtxt(filenamevariable, delimiter = ',', dtype = str)

#To load using a tab delimiter 
import numpy as np 
filenamevariable = 'filename.txt'
data = np.loadtext(filenamevariable, delimiter = '\t')
