#Used to select, intert, update or delete data within a SQL database
#Also used, to create, alter or delete tables and columns in a SQL database

#Select Statements 
SELECT columnname FROM tablename 

#To select all the columns from a table use * 
SELECT * FROM tablename 

from sqlalchemy import create_engine 
#create an engine 
enginevariable = create_engine('sqlite:///filename.sqlite')
#establish a connection by using the connect method on the engine 
connectionvariable = enginevariable.connect()
#Define our select statement and pass it to the excute method of the connection
statementvariable = SELECT * FROM table 
#giving us an object that we can use to fetch results
result_proxy = connection.excute(statementvariable) 
#fetch all results from the table 
results = result_proxy.fetchall()

#Result Proxies can be used in a variety of ways to get the data returned 
#We get a result set when we use a fetch method on a result proxy 
#The difference bewteen a result proxy and result set allows us to fetch as much or little data as we want 
