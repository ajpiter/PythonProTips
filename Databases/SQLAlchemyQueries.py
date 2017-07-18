stmt = select([census.columns.age, (census.columns.pop2008-census.columns.pop2000).label('pop_change')
stmt = stmt.group_by(census.columns.age)
stmt = stmt.order_by(desc('pop_change'))
stmt = stmt.limit(5)
results = connection.execute(stmt).fetchall()
print(results)

#Case Statement 
#used to treat data differently based on a condition 
#accepts a list of considitions to match and a column to return if the condition matches 
#the list of conditions ends with an else clause to determine what to do when a record dosent match any prior conditions 

from sqlalchemy import case 
stmt = select([func.sum(case([census.columns.state == 'New York', census.columns.pop2008)], else_=0))])
results = connection.execute(stmt).fetchall()
print(results)

#cast statement 
#converts data to another type 
#useful for converting 
#integers to floats for division 
#strings to dates and times 
#accepts a column or expression and the target type 

#percentage example 
from sqlalchemy import case, cast, Float 
stmt = select([(func.sum(case([(census.columns.state == 'New York', census.columns.pop2008)], else_=0)) / cast(func.sum(census.columns.pop2008), Float) * 100).label('ny_percent')])
results = connection.execute(stmt).fetchall()
print(results) 

#SQL Relationships 
#Allows us to avoid duplicate data 
#Make it easy to change things in one place 
#Useful to break out information from a table we don't need very often 

#automatic joins 
stmt = select([census.columns.pop2008, state_fact.columns.abbreviation])
results = connection.execute(stmt).fetchall()
print(results) 

#join
#accepts a table and an optional expression that explains how the two tables are related 
#The expression is not needed if the relationship is predefined and available via reflection 
#comes immediately after the select() clause and prior to any where(), order_by or group_by() clauses 

#Select_from 
#used to replace the default, derived from clause with a join 
#wraps the join() clause 
stmt = select([func.sum(census.columns.pop2000)])
stmt = stmt.select_from(census.join(state_fact))
stmt = stmt.where(state_fact.columns.circuit_court == '10')
result = connection.execute(stmt).scalar()
print(result) 

#Joining tables without a predefined relationship 
#join accepts a Table and an optional expression that explains how the two tables are related 
#will only join on data that match bewteen the two columns 
#avoid joining on columns of different types 

#select_from example 
stmt = select([func.sum(census.columns.pop2000)])
stmt - stmt.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))
stmt = stmt.where(state_fact.columns.census_division_name == 'East South Central')
result = connection.execute(stmt).scalar()
print(result) 

#Working with Hierarchical Tables 
#contain a relationship with themselves
#commonly found in organizational, geographic, network or graphs 
#requires a way to view the table via multiple names 
#creates a unique reference that we can use 

#Querying hierarchical data 
managers = employees.alias()
stmt = select([managers.columns.name.label('manager'), employees.columns.name.label('employee')])
stmt = stmt.select_from(employees.join(managers, managers.columns.id == employees.columns.manager) 
stmt = stmt.order-by(managers.columns.name) 
print(connection.execute(stmt).fetchall())

#group_by and func
#it is important to target group_by() at the right alias 
#be careful with what you perform functions on 
#if you don't find yourself using both the alias and the table name for the query dont create the alias at all 
managers = employees.alias()
stmt = select([managers.columns.name, func.sum(employees.columns.sal)])
stmt = stmt.select_from(employees.join(managers, managers.columns.id == employees.columns.manager) 
stmt = stmt.group_by(managers.columns.name) 
print(connection.execute(stmt).fetchall())

#Handling Large Result Sets 
#dealing with Large Result Sets 
#fetchmany() lets us specify how many rows we want to act upon 
# we can loop over fetchmany() 
#it returns an empty list when there are no more records 
#we have to close the result proxy afterwards 
while more_results: 
    partial_results = results_proxy.fetchmany(50)
    if partial_results == []:
        more_results = False 
    for row in partial_results: 
        state_count[row.state] += 1 
results_proxy.close()


