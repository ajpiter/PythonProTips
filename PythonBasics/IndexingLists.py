#In python the index values of a list begin at zero.
#This is known as zero-based indexing. 

#For example, the following lists has indexes at the below values. 
listnamevariable = [8.27, listvalue, True, listvalue2, 55.60, listvalue3, 1, False, 4] 
#index:             0     1           2     3           4      5          6   7     8 

#To subset a list using the index number 
listnamevariable[3]
#In this case would return listvalue2 

#Lists can also be indexes from the end using negative numbers begining with -1
listnamevariable[-1] 
#would return 4 

#You can also get the index number of an item in a list 
lista = ["Jan", "Feb", "Mar", "Apr", "May", "June"]
print(lista.index("May")
#output 5 
