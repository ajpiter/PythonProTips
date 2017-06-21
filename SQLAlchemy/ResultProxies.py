#Result Proxies can be used in a variety of ways to get the data returned 
#We get a result set when we use a fetch method on a result proxy 
#The difference bewteen a result proxy and result set allows us to fetch as much or little data as we want 

#giving us an object that we can use to fetch results
result_proxy = connection.excute(statementvariable) 
#fetch all results from the table 
results = result_proxy.fetchall()

#handling result sets 
firstrow = results[0]
print(firstrow)

#to find out what columns are in the row, use the keys method 
print(firstrow.keys())

#print the value of the first row, and column by using the column name 
print(firstrow.columnname)
