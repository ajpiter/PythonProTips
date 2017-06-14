#An uneven aspect ratio occurs when you take a sample of the pixels 
#The code below takes the 4th across and the 2nd high 
#Resulting in uneven sampling and a distored image because the aspect ratio is not equal 

variable = variableb[::4,::2]
print(variable.shape) 
plt.imshow(variable)
plt.axis('off')
plt.show()

#To adjust the aspect ratio to scale the pixels approriately 
plt.imshow(variable, aspect = 2.0) 
plt.axis('off')
plt.show()

#OR 
#Display the orginal image dimensions using the keyword extent
plt.imshow(variable, cmap='grey', extent=(0,640,0,480)
plt.axis('off')
plt.show()

#Use both aspect ratio and extent 
plt.subplot(2,2,2)
plt.title('Title')
plt.xticks([-1,0,1])
plt.yticks([-1,0,1])
plt.imshow(variable, extent=(-1,1,-1,1), aspect=1)
plt.axis('off')
plt.show()
