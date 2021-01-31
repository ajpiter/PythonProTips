

credits = 120
gpa = 1.9

----- #If Else ----- 
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else: 
  print("You do not meet the requirements to graduate.")
  
----- # If, Elif, Else ----- 

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
