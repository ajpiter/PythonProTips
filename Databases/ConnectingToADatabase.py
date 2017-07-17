#Connection strings tell us what kind of database we are connecting to, and how we should access it. 
'databasedrive:///'filename'

#Create an engine, which is the commone interface to the database from SQLAlchemy

from sqlalchemy import create_engine 
#call create_engine on the connection string 
enginevariable = create_engine('sqlite:///filename.sqlite')
#once we have an engine we are ready to make a connection 
connectionvariable = enginevariable.connect()

#SQLAlchemy won't make the connection until we give it some work to excute 

