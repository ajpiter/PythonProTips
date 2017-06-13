#By customizing the axis on a plot, you can zoom into specific sections of the plot. 

#To adjust the entire axis
axis([xmin, xmax, ymin, ymax])

#To adjust indivdual axis limits 
xlim([xmin, xmax]) 
ylim([ymin, ymax]) 
#or also written as: 
xlim((xmin, xmax))
ylim((ymin, ymx))

import matplotlib.pyplot as plt 
plt.plot(variablea, variableb, color = 'red') 
plt.xlabel('Label on X Axis') 
plt.ylabel('Label on Y Axis') 
plt.title('Title of Plot')
plt.xlim((xmin, xmax))
plt.ylim((ymin, ymax))
plt.show()
plt.savefig('DocName.png')

#Other axis opitions 
#Turn off axis limits 
axis('off')

#Equal scalling on x and y axis 
axis('equal')

#Forces square plot
axis('square')

#Sets xlim() and ylim() to show all data
axis('tight') 
