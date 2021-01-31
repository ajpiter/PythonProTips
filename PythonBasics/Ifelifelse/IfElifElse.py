----- # If Satement ----- 
z = 4 
if z % 2 == 0: 
  print('z is even')   

#output z is even
#Request a user input a value. Then check that the value meets the requirements. 
value = int(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <= 10: # Only one, slightly more complicated check
    print("In range")
print("Done")

----- #If Else -----   
#Is Z Even? 
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
    
#Graduation Requirements
credits = 120
gpa = 1.9
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else: 
  print("You do not meet the requirements to graduate.")
  
----- # If, Elif, Else ----- 

## Elif Statement 
z = 3 
if z % 2 == 0: 
  print('z is divisible by 2') 
elif z % 3 == 0:
  print('z is divisible by 3') 
else:
  print('z is neither divisible by 2 nor by 3')
#output z is divisible by 3 

#Letter Grade Calculator 
if grade >= 90: 
  print("A")
elif grade >= 80: 
  print("B")
elif grade >= 70: 
  print("C")
elif grade >= 60: 
  print("D")
else: 
  print("F")
  
----- #Input, If Else ----- 
Age = float(input("How old are you?"))

if Age >= 21:
  print("Cheers, enjoy a drink on us!")
else:
  print("Sorry, the legal drinking age is 21 or older.")
