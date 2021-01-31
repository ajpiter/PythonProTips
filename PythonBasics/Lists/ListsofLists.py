#Lists can hold anytype of data including other lists 
ListOfList =  [["ListTitle", variable, TRUE],
              ["Grade", 100, 75],
              ["HoursStudied" 8, 4], 
              ["WatchedVideos", TRUE, TRUE],
              ["AttendedClass", FALSE, TRUE]]

----- #Use zip() to combine two lists together into one list of list -----
Phonetic = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'X-ray', 'Yankee', 'Zulu']
Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#apparently you can also make an alphabet list using 
#Alphabet = list('abcdefghijklmnopqrstuvwxyz')

#Using zip, you create a zip datatype but can transform it to list in a print() statement 
Phonetic_Alphabet = zip(Alphabet, Phonetic) 
print(list(Phonetic_Alphabet))

#You can also save the zip as a new list variable 
Phonetic_Alphabet = zip(Alphabet, Phonetic)
Phonetic_Alphabet = list(Phonetic_Alphabet) 

#Does zip work with lists of different lengths? 
#No, the resulting list will have the number of arguments from the smallest list 
#https://discuss.codecademy.com/t/does-the-zip-function-work-with-lists-of-different-lengths/351451

----- #Use cycle() to iterate one list over another list ----- 
import itertools 
Alphabet = list('abcdefghijklmnopqrstuvwxyz')
Groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

#To assign everyone to a group based on the first letter of their last name 
Group_Assignment = list(zip(Alphabet, itertools.cycle(Groups)))
print(Group_Assignment) 
