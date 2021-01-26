#conditional statements are if, else, elif statements 
if condition: 
  expression 
elif: 
  expression
else: 
  expression 
  

----- #if Statement ----- 
z = 4 
if z % 2 == 0: 
  print('z is even')   
#output z is even

#Request a user input a value. Then check that the value meets the requirements. 
value = int(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <= 10: # Only one, slightly more complicated check
    print("In range")
print("Done")

----- #else Statement ----- 
z = 5 
if z % 2 == 0: 
  print('z is even')
else: 
  print('z is odd') 
#output z is odd 

#Do the values match? 
d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1 =', d1, ' d2 =', d2)
if d1 == d2:
    print('Same')
else:
    print('Different')

----- #elif Statement ----- 
z = 3 
if z % 2 == 0: 
  print('z is divisible by 2') 
elif z % 3 == 0:
  print('z is divisible by 3') 
else:
  print('z is neither divisible by 2 nor by 3')
#output z is divisible by 3 

#request a user input a value and then check to see if the value is within the range of acceptable numbers. 
TempC = int(input("Please enter the tempature in Celsius:"))
if TempC >= -90: # First check
    if TempC <= 58: # Second check
        print("The tempature in F is ", (TempC*2 + 30))
    else:
        print("Are you sure you entered the Tempature in C? ", TempC, "is larger than the highest recorded temperature.")
else:
    print("Are you sure you entered the Tempature in C?", TempC, "is smaller than the lowest recorded temperature.")
