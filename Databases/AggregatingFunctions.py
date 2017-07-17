#Counting  Summing and Grouping Data 

#Aggregation Functions, because they collapse multiple records into one. 
#Examples of aggregation functions include count and sum.
#More efficent to let sql calculate than to loop over them in python.

#Example to calucalte a sum in SQL
#Note it is important not to import sum directly because it will conflict with the sum function in python 
from sqlalchemy import func 
stmt = select ([func.sum(databasename.columns.columnname)])
results = connection.execute(stmt).scalar()
print(results) 

#group_by()
#group_by can accept multiple columns and will group by columns from left to right 
#every column in the select statement must be in the group_by clause OR wrapped by a function such as sum or count

#Sum by grouping by another column example sum of the data by sex
stmt = select([databasename.columns.columnnamesex, func.sum(databasename.columns.columnname)])
stmt = stmt.group_by(database.columns.columnnamesex) 
results = connection.execute(stmt).fetchall()
print(results) 

#group_by() multiple columns 

stmt = select([database.columns.columnname, database.columns.columnnameb, func.sum(database.columns.columnnamec)])
stmt = stmt.group_by(database.columns.columnnamea, database.columns.columnnameb)
results = connection.execute(stmt).fetchall()
print(results) 
