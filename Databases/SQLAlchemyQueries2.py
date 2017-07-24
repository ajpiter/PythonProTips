#Provides a way to build SQL Statements in Python 

form sqlalchemy import create_engine
engine = create_engine('ssglite:///filename.sglite')
connection = engine.connect 
from sqlalchemy import Table, MetaData 
metadata = MetaData()
census = Table('Table', metadata, autoload=True, autoload_with=engine) 
stmt = select([Table]) 
results = connection.excute(stmt).fetchall()

#SQLAlchemy select statement works the same as a SQl select statement 
#requires a list of one or more Tables or Columns 
#Will select all the columns of all the rows in the table 
stmt = select([Table])
#The print(stmt) will output the statement 'SELECT * FROM Table'
