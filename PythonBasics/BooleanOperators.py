#Boolean operators are and, or, not 
#Numpy also uses logical_and(), logical_or(), and logical_not()

----- #Example: and -----
True and True #output is True 

False and True #output is False 

False and False #output is False 

x = 12 
x > 5 and x < 15 
#output is True 

----- #Example: or ----- 
True or True #output is True 

False or True #output is True 

False or False #output is False 

y = 5 
y < 7 or y > 13 
#output is True 

----- #Example: not ----- 
not True #output is False 

not False #output is True 

---- #Example: logical_and() ----- 
np.logical_and(variable > 21, variable < 25) 
#[output] TRUE
np.logival_and(array > 21, array < 25) 
#[output] array([True, False, True, True], dtype=bool)


