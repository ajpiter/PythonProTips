#Usually you want to create a new list, but by using the '=' you accidential create a reference to a list 

----- #This creates a copy of the reference to the list -----
x = ['a', 'b', 'c']
y = x 

#Which means this will change the elements in both list x and y 
y[1] = 'z'
print(x) 
print(y) 

#output ['a', 'z', 'c']
#output ['a', 'z', 'c']

----- #This creates a copy of the list ----- 

x = ['a', 'b', 'c']
y = list(x)         #or y = x[:]
y[1] = 'z'
print(x) 
print(y) 

#output ['a', 'b', 'c']
#output ['a', 'z', 'c']

#These are notes from the DataCamp course Introduction to Python, video Mainpulating Lists 
