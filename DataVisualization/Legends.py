#To create a label in the legend of the plot 
plt.scatter(variablea, variableb, marker = '0', color = 'red', label ='Label Name')

#Determines where the legend is located on the plot
plt.legend(loc='upper right') 

#Legend locations can be written as strings or numeric codes. 
""" 'best' 0 
'upper right' 1
'upper left' 2
'lower left' 3
'lower right' 4 
'right' 5 
'center left' 6 
'center right' 7 
'lower center' 8 
'upper center' 9 
'center' 10 
