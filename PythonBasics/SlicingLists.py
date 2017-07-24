#Slicing allows you to determine which values of the list you see. 

#start with a basic list
listvariable = ['a', 1, 'b', 2, 'c', 3]

#slice using [brackets] to see values [start:end] 
#The starting value is included in your slice, but the ending value is not.
listvariable[3:5] 
#In this case the output would be [2, 'c']

#You can omit the starting variable and replace it with : and the slice will begin at the begining of the list. 
listvariable[:5]
#The output would be ['a', 1, 'b', 2, 'c'] 

#Similarly you can omit the ending variable and replace it with : and the slice will continue to the end of the list. 
listvariable[5:]
#The output would be ['c', 3]
