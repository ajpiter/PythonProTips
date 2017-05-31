#Use pandas melt to fix columns containing values instead of variables using pd.melt 

#Save the data into a dataframe named df. 
#We want the column name that stores the name to be fixed so we store it in the id_vars parameter. 
#value_vars specifies which columns you want to mely. In this case a and b. 

import pandas as pd 
pd.melt(frame = df, id_vars = 'name', value_vars = ['a', 'b']

#We can rename the column names using the var_name and value_name parameters. 

import pandas as pd
pd.melt(frame = df, id_vars ='name', value_vars = ['a','b'], var_name = 'renamecolumn', value_name = 'renamecolumn2'

#If you do not specify value_vars melt will use all the columns not specified in the id_vars parameter. 
