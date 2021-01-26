#unlike a list where order matters to select subsets, a dictionary is a lookup table with unique keys. 

value = [1, 2, 3, 4] 
key = ['a', 'b', 'c', 'd']
dictionary = {'a':1, 'b':2, 'c':3, 'd':4}

#then you can find the corresponding value using the key 
dictionary['a']
#output would be 1 

dictionary
#output would be {'a':1, 'b':2, 'c':3, 'd':4}

#Use index() to look up values 
dictionary.index('b') 
#output would be 2

#Check if key exists in dictionary 
"VariableKey" in dictionary 
#[output] TRUE 

#Delete keys and corresponding values from dictionary 
del(dictionary["VariableKey"]) 

del(dictionary["a"])
dictionary 
#[output] {'b':2, 'c':3, 'd':4}

#Lists use ['X', 'Y', 'Z'] or [1, 2, 3] or [1.89, 'y', TRUE]
#Dictionaries use {"X":1, "Y":2, "Z":3} 
#Arrays use [1, 2, 3]

#Dicitonary Keys have to be immutable objects 
