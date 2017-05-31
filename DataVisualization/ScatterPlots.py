#Scatter plots are best used to show the relationship bewteen two numeric variables or to flag potential errors not found by looking at one variable. 

df.plot(kind = 'scatter', x = 'columnname', y = 'columnname', rot = 70)
plt.show()

#Scatter Plot of a Subset 
df_subset.plot(kind = 'scatter', x = 'columnname', y = 'columnname', rot = 70)
plt.show()
