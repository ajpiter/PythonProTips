#Annotations places text or arrows directly on the plot
plt.annotate('text', xy=(x,y)
plt.show 

#For arrows 
plt.annotate('text', xy=(x,y) xytext(x,y), arrowprops{'color'='red'})

plt.plot(variablea, variableb, color='red', label ='Label Title')
plt.plot(variablea, variablec, color='blue', label = 'Laebel Title')
plt.legend(loc = 'bottom right') 
y_max = variableb.max()
x_max = variablea[variableb.argmax()]
plt.annotate('Arrow Label', xy =(x_max, y_max), xytext(x_max+5, y_max+5), arrowprops = dict(facecolor ='black')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title') 
