### Methods call functions on objects 
#Objects (Lists, Strings etc) have built in methods and you cannot run the method on the wrong object type. 
#A method used on a list will not work on a string.

### List Methods
#Example, use the function index() on a list to see the index number of a specified value
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.index('b')
#output would be 2 
#Example of using the count() function on a list to determine the number of times a specified value appears
basiclist = ['a', 1, 'b', 2, 'c', 3] 
basiclist.count('b')
#output would be 1 

### String Methods
#example of using the capitalize() function on a string 
name = 'amanda'
name.capitalize()
#output would be 'Amanda' 
#example of using the replace() method
notebook = Jupiter
notebook.replace("i", "y")
#output would be Jupyter
