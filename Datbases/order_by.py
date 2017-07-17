#Ordering Query Results in SQL Alchmy 
#The order_by() command orders from lowest to highest, or alphabetically by default 

#Example of building a select statement, appending an order_by() clause and executing the statement
#By Default this sorts alphabetically  
stmt = select([tablename.columns.columnname])
stmt = stmt.order_by(tablename.columns.columnname) 
results = connection.execute(stmt).fetchall()
print(results[:10])

#To order by descending, or highest to lowest use desc()

#To order by multiple columns you can list multiple columns in the order_by()
#columns will be sorted by the first column, and then by the second column if there are duplicates from the first 
#Example

stmt = ([tablename.columns.columnname, tablename.columns.columnname]) 
stmt = stmt.order_by(tablename.columns.columnname, tablename.columns.columnname)
results = connection.execute(stmt).first()
print(results) 
