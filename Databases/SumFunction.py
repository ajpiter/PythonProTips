#Example to calucalte a sum in SQL
#Note it is important not to import sum directly because it will conflict with the sum function in python 
from sqlalchemy import func 
stmt = select ([func.sum(databasename.columns.columnname)])
results = connection.execute(stmt).scalar()
print(results) 
