#Examples from Code Academy, Python 3 

----- #Example If And ----- 
credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

----- #Example If Or -----  
credits = 118
gpa = 2.0
if credits >= 120 or gpa >= 2.0: 
  print("You have met at least one of the requirements.")
  
----- # Example If Not ----- 
credits = 120
gpa = 1.8

if not credits >= 120: 
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0: 
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0): 
  print("You do not meet either requirement to graduate!")
