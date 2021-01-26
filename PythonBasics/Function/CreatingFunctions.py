#Functions are useful when you will have to preform the same tasks repeatedly

#Creating your own Function 
1. define the function 
   def function(parameter): 
       print(parameter + "string") 
2. call the function, function()

----- #Basic Function: Outputs a Print Statement ----- 
def function(parameter, parameter2, parameter3):
  print(parameter + "string" + parameter2 + "string" + paramenter3 + ".") 

def write_a_book(character, setting, special_skill):
  print(character + " is in " + 
        setting + " practicing her " + 
        special_skill) 
        
write_a_book('Superman', 'Smallville', 'xRayVision')
#[output] Superman is in Smallville practicing her xRayVision. 

----- #Function Return Statement Instead of Print ----- 
def write_a_book(character): 
  return character == 'Superman' 
  
write_a_book('Batman')
#[output] False 

print("Superman is the main character in your book" + write_a_book('Batman') 
#[output] Superman is the main character in your book False 

----- #Data Type Rules Still Apply in Functions -----
#Functions that return a print() require all parameters to be strings 

def sales(grocery_store, item_on_sale, cost):
  print(grocery_store + " is selling " + item_on_sale + " for " + cost) 
  
sales("The Farmer’s Market", "toothpaste", "$1")
#[output] The Farmer’s Market is selling toothpaste for $1

sales("Amazon", "Alexa", 20) 
#[output] can only concatenate str (not "int") to str

----- #Keywords as Parameters ----- 
#By using keywords with default values in the parameters argument of the function, any order could be used when calling the function 

def findvolume(length=1, width=1, depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth;
  
findvolume(length=5, depth=2, width=4)
#Length = 5
#Width = 4
#Depth = 2
#40

#All keywords will still need to be defined 
findvolumne(lenth=5, depth=2)
#[output] NameError: name 'findvolumne' is not defined

----- #Saving Outputs as Variables ----- 
def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  # Return all three values:
  return x_squared, y_squared, z_squared
  
square_point(3, 4, 5) 
#[output] (9, 16, 25)

#There is no ouput when assigning function values to multiple variables 
three_squared, four_squared, five_squared = square_point(3, 4, 5)
#[output] 

#To see an output call a variable 
three_squared
#[output] 9 

#or write a print() with the specified variables 
print(three_squared, four_squared, five_squared) 
#[output] (9, 16, 25)





#For more information on functions see Code Academy's cheat sheet on functions 
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-functions/cheatsheet
