#Example from Code Academy Python 3, Loops

#The break in this for loop, stops the loop from executing on the list dog_breeds_available as soon as the correct breed is found. 
dog_breeds_available = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available: 
  print(dog)
  if dog == dog_breed_I_want: 
    print("They have the dog I want!")
    break
    
#P.S. There are no 'correct' dog breeds in real life. Puppies of everytype are awesome. In the program specified it's only looking for a dalmatian

#Continue allows you to skip values when iterating over a list. 
#Prints all the positive numbers regardless of where they are in the list.  
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i < 0:
    continue
  print(i)

#Comparison break stops the list at the first negative number 
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i < 0:
    break
  print(i)
  
#Watch your indentation for your print() to appear in different points in the loop
name =["Elsa", "Emily", "Caitlin", "Sophia", "Brooklyn", "Abby", "Debbie", "Karen", "Liz"]
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages: 
  if age < 21: 
    print("Sorry you are only ", age, "years old. I cannot allow you enter the bar.")
    continue 
  print("Welcome, to Hometown Bar.")
print("All IDs have been checked")
