#To order by multiple columns you can list multiple columns in the order_by()
#columns will be sorted by the first column, and then by the second column if there are duplicates from the first 
#Example

stmt = select([tablename.columns.columnname, tablename.columns.columnname]) 
stmt = stmt.order_by(tablename.columns.columnname, tablename.columns.columnname)
results = connection.execute(stmt).fetchall()
print(results[:10]) 
