# While Loops are a numerically calculating model and repeatedly runs until a condition is met.  
# While loops can be useful when you don’t know how many iterations it will take to satisfy a condition.

error = 50.0 
while error > 1: 
  error = error / 4 
  print(error) 
  
#output 12.5 
#output 3.125 
#output 0.78125 

----- #Example While Loop ----- 
#Assign students missing a class 4th period to the new poetry class. 
students_not_in_class = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6: 
  student = students_not_in_class.pop()
  students_in_poetry.append(student)

students_in_poetry.sort() #prints the list alaphabetically 

print("The following students have been added to the new poetry class: ", students_in_poetry)
print("")
print("The students still not assigned a class are: ", students_not_in_class)

#The following students have been added to the new poetry class:  ['Alexa', 'Arius', 'Dora', 'Loki', 'Minerva', 'Obie']
#
#The students still not assigned a class are:  ['Alex', 'Briana', 'Cheri', 'Daniele']
