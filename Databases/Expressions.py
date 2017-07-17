#Expressions provide more complex conditions than simple comparisons  
#in_() matches a columns value against a list 
#like() matches a column's value against a incomplete value with wildcards 
#between() checks to see if a columns value is bewteen two supplied values 

#Example, use expressions to find all the state names that start with new
stmt = select ([census]) 
stmt = stmt.where(census.columns.state.startswith('New'))
for result in connection.execute(stmt):
  print(results.state, result.pop2000)
