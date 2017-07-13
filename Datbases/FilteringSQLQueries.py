#Where clauses allow you to compare a column against a value or another column. 
#Comparisons in where clauses include ==, <=, >=, or !+ 

#Example, use a where clause to select all the records for the state of california 
stmt = select([census])
stmt = stmt.where(census.columns.state == 'California')
results = connection.execute(stmt).fetchall()
for result in results: 
  print(result.state, result.age) 

#Expressions provide more complex conditions than simple comparisons  
#in_() matches a columns value against a list 
#like() matches a column's value against a incomplete value with wildcards 
#between() checks to see if a columns value is bewteen two supplied values 

#Example, use expressions to find all the state names that start with new
stmt = select ([census]) 
stmt = stmt.where(census.columns.state.startswith('New'))
for result in connection.execute(stmt):
  print(results.state, result.pop2000)
  
#Conjuntions allow us to have multiple criteria in a where clause 
#Use the underscore to avoid conflicting with the python methods of the same name 
#and_(), not_(), or_()
  
#Example, use conjuntion to find all 
from sqlalchemy import or_ 
stmt = select([census]))
stmt = stmt.where(or_(census.columns.state == 'California', census.columns.state == 'New York') 
for result in connection.execute(stmt):
  print(result.state, result.sex) 
