#Notes are from Udacity's Deep Learning Nano Degree 
#Linear Regression models work best when the data is linear
#Linear Regression is sensentive to outliers 

#Linear Regression model with one input, and one prediction 
#Shown graphically as a line 
import pandas as pd 
from sklearn.linear_model import LinearRegression
variable = pd.read_csv('filename.csv')
# Make and fit the linear regression model
variablemodel = LinearRegression()
variablemodel.fit(variable[['columnname']],variable[['columnnameb']])
# Make a prediction using the model
variablepredict = variablepredict.predict(29)

#Linear Regression model with two inputs (predictors) as an array, and two predictions 
#shown graphically as a plane 
# import pandas as pd 
from sklearn.linear_model import LinearRegression 
variablemodel = LinearRegression()
variablemodel.fit(x_values, y_values) 
model.predict([29], [54])

#Linear Regression model with multiple inputs as an array and one prediction 
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import load_boston 
variable = load_boston()
x = variable['columnname']
y = variable['columnnameb']
variablemodel = LinearRegression()
variablemodel.fit(x,y)
variablearray = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
variableprediction = variablemodel.predict(variablearray) 
