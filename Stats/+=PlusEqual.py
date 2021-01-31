#Example from Code Academy, Learn Python 3, Hello World, Plus Equals  

#When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.

----- #Example: Integers ----- 

# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

number_of_miles_hiked_sat = 4 
number_of_miles_hiked_sun = 2 
number_of_miles_hiked += number_of_miles_hiked_sat + number_of_miles_hiked_sun
print(number_of_miles_hiked)
# Prints 20

----- #Example: Strings ----- 
hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption) 
#Prints What an amazing time to walk through nature! #nofilter #blessed

