for <temporary variable> in <list variable>:
    <action>

----- #For Loops: Print Item in List ----- 
#A For loop follows the format "for item in list:"
#Any placeholder string can be used instead of item to achieve the same results. 

list = [1, 2, 3, 4] 
for item in list: 
  print(item)
#output 1 
#output 2 
#output 3 
#output 4 
for unicorn in list: 
  print(unicorn) 
#output 1 
#output 2 
#output 3 
#output 4 

----- #Include the Index, and element in your print() statement ----
for index, element in enumerate(list):
  print('index ' +str(index) + ': " + str(element)
#output index 0: 1 
#output index 1: 2 
#output index 2: 3 
#output index 3: 4 

----- #For Loops Applied to Strings -----
A for loop is most often applied to lists, but can also be applied to other data types including strings. 
for c in 'family':
  print(c.capitalize())
#Output F 
#Output A 
#Output M
#Output I 
#Output L 
#Output Y 
        
----- #Use range() to specify the number of times to run a loop ----- 
#This statement does not require a list or a variables, instead for the number of i inside the range() you are printing 
for i in range(1): 
   print('Hello')
#output Hello 

#i can be changed to any string
#the '#' inside range() is the number of times the loops runs 
for anything in range(2): 
    print('Bye') 
#output Bye
#output Bye 

#Only indented code is included in the for loop and repeats based on range() 
for lyric in range(3):
    print('row')
print('your boat') 
#row
#row
#row
#your boat
