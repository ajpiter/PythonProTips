stmt = select([tablename.columns.columnname, tablename.columns.columnname]) 
stmt = stmt.order_by(tablename.columns.columnname, tablename.columns.columnname)
results = connection.execute(stmt).fetchall()
print(results[:10]) 
