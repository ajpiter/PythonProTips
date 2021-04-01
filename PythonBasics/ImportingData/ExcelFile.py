import pandas as pd 
varaiablefilename = 'filename.xlsx'
data = pd.ExcelFile(variablefilename)
print(data.sheetname)
