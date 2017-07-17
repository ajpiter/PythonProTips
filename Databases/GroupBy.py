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
