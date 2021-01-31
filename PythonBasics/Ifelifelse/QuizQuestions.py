#Code Academy If  Statement Example 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Water'
option4 = 'A&W'
  
print("1. For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = input("Answer 1 is:")

if answer == 'A' or answer == 'a': 
  score += 10
  print("\nCorrect!")
else:
  print("\nNope, sorry!")
