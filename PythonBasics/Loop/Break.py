#Example from Code Academy Python 3, Loops, 5. Break 

#The break in this for loop, stops the loop from executing on the list dog_breeds_available as soon as the correct breed is found. 

dog_breeds_available = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available: 
  print(dog)
  if dog == dog_breed_I_want: 
    print("They have the dog I want!")
    break
    
#P.S. There are no 'correct' dog breeds in real life. Puppies of everytype are awesome. In the program specified it's only looking for a dalmatian
