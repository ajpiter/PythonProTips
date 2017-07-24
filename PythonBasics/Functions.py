#You can call a function instead of rewriting the code yourslef using (). 
#Examples of built in functions are round(), max(), len(). 

#Round will round the number you place inside the () to the number of digits you specific. 
#round(NumberToRound, DigitsToRound) 
#If digits are not specified the number will be rounded to 0 digits. 
round(22.79) 
#output would be 23 
round(22.79, 1) 
#output would be 22.8 

#Methods are built in functions 

#Example, use the function index() on a list to see the index number of a specified value
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.index('b')
#output would be 2 

#Example of using the count() function on a list to determine the number of times a specified value appears
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.count('b')
#output would be 1 

#example of using the capitalize() function on a string 
name = 'amanda'
name.capitalize()
#output would be 'Amanda' 
