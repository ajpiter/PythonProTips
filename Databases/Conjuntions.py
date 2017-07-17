#Conjuntions allow us to have multiple criteria in a where clause 
#Use the underscore to avoid conflicting with the python methods of the same name 
#and_(), not_(), or_()
  
#Example, use conjuntion to find all 
from sqlalchemy import or_ 
stmt = select([census]))
stmt = stmt.where(or_(census.columns.state == 'California', census.columns.state == 'New York') 
for result in connection.execute(stmt):
  print(result.state, result.sex) 
