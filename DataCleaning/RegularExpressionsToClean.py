#Use regular expressions in Pandas when you want to match values down a column. 

import re 
pattern = re.complie('\$\d*\.\d{2}')
result = pattern.match('$20.17')
bool(result)

# re is for regular expression 
# \d is to match any digit 
# * is to match 0 or more times 
# \$ represents the actual $ when proceded by \ 
# \. represents the . when proceded by \ 
# \d{2} would match exactly two digits 
#A-Za-z tp match upper and lower case letters 

# ^ match begining value 
# $ match end value 
# axis = 0 is for columns 
# axis = 1 is for rows 

import re 
from numpy import NaN 
pattern = re.compile('^\$\d*\.\d{2}$')

def diff_money(row, pattern): 
    rownewnamea = row['rownameA']
    rownewnameb = row['rownameB']
    if bool (pattern.match(rownewname)):
        #removes the $ 
        rownewnamea = rownewnamea.replace('$', '')
        rownewnameb = rownewnameb.replace('$', '')
        #convert into a floating point number
        rownewnamea = float(rownewnamea)
        rownewnameb = float(rownewnameb) 
    else:
        return (NaN)
dataframe['diff'] = dataframe.apply(diff_money, axis = 1, pattern = pattern)
print(dataframe.head())

#OR another example that prints, anything that does not match the regular expression. 

# Create the series 
seriesname = dataframe.columnname 
# Drop all the duplicates from countries
seriesname = seriesname.drop_duplicates()
# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'
# Create the Boolean vector
mask = seriesname.str.contains(pattern)
# Invert the mask: mask_inverse
mask_inverse = ~mask
# Subset countries using mask_inverse
invalid_seriesname = seriesname.loc[mask_inverse]
# Print invalid_countries
print(invalid_seriesname)
