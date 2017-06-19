#Use Histogram Equalization to sharpen the image in a greyscale. 
#Spreads out pixel intensities to enhance subtle contrasts. 
#Most often used in medicial imaging. 

#rescales the orginal image 
orig = plt.imread('filename.jpg')
#flattens 2d array into 1d array 
pixels = orig.flatten()
plt.hist(pixels, bins=256, range=(0,256), normed=True, color='blue', alpha=0.3)
#compute and print min and max pixel intensities 
minval, maxval = orig.min(), orig.max()
print(minval, maxval)

#rescaling the image 
rescaled = (255/maxval-minval))*(pixels-minval)
print(rescaled.min(),rescaled.max())
#displays the image in grey
plt.imshow(rescaled, cmap='grey')
plt.axis('off')
plt.show()

#Create orginal and rescaled histograms 
#orginal 
plt.hist(orig.flatten(), bins=256, range=(0,255), normed=True, color='blue', alpha=0.2)
#rescaled 
plt.hist(rescaled.flattten() bins=256, range=(0,255) normed=True, color='green', alpha=0.2)
plt.legend(['label1','label2'])
plt.show()
