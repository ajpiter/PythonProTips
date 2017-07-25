
#To label both axis and add a title. You can also choose to omit either label or the title by removing that line of code. 
import matplotlib.pyplot as plt 
lista = [2001, 2002, 2003, 2004] 
listb = [1, 2, 3, 4] 
plt.plot(lista, listb)
plt.xlabel('Label on the X axis')
plt.ylabel('Label on the Y axis') 
plt.title('Title of the plot')
plt.show()

#To plot tick marks along your axis at specific intervals just add 
plt.yticks([0,1,2,3,4,5]) 

#Or to plot ticks with additional information 
plt.yticks([0,1,2,3,4,5], ['0','1 Mil', '2 Mil', '3 Mil', '4 Mil', '5 Mil'])
