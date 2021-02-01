#Explination from Code Academy's Python 3, Lists, Exercise 8 Range and Exercise 9 Range II  

----- #Range from 0 to # ----- 
#Create a list of consecutive numbers 
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Python gives us an easy way of creating these lists using a function called range. The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. 
my_range = range(10)

#The range function returns an object that we can convert into a list:
print(list(my_range))
#my_range = list(range(10)) #or in one line of code
#[output] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Check your work by printing the range
print(my_range)
#[output] range(0, 10)

----- #Specific Range ----- 
#call range with two arguments, we can create a list that starts at a different number
my_list = range(2, 9)
print(list(my_list))
#output [2, 3, 4, 5, 6, 7, 8]

----- #Count by Multiples of X ----- 
#If we use a third argument, we can create a list that “skips” numbers. 
my_range2 = range(2, 9, 2)
print(list(my_range2))
#output [2, 4, 6, 8]

----- #Rules & Trouble Shooting ----- 
#range() only accepts positive interger values 
# These will return an empty list
nonumber1 = range(0)
nonumber2 = range(-10)

# Passing a decimal number will return a Python TypeError
error1 = range(3.2)
