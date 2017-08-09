#Gradient Descent 
#A mathmatical term for an array of slopes 

#To calculate the gradient descent 
#repeatedly find a slope to find how your lost function changes as the weight changes
#then make a small change to the weight to get to a lower point 
#repeat until you cannot go down hill anymore 

#Learning Rate 
#If the slope is positve, then going opposite the slope means moving to lower numbers
#Could Subtract the slope from the current value but we don't take too big of a step 
#Instead we multiply the slope by a small number called a learning rate 
#Change the weight by the product of that multiplication 
#Weight - (LearningRate * Slope)
#Standard Learning Rate is 0.01

#Use Keras and Tensorflow to do the calucus for you 

#Slope Caluclation Example 
Node1 = 3 
Weight = 2 
Node2 = 6 
PredictedValue = Node2
Actual Target Value = 10 
LearningRate = 0.01 

SlopePrediction = Slope of Mean-Squared loss function precdiction 
SlopePrediction = 2 * (Predicted Value - Actual Value) = 2*Error 
SlopePrediction = 2 *(6 - 10) = 2 * -4

Node1 = Value of the node that feeds into our weight
Node1 = 3 

SlopeWeight = Slope for a weight 
SlopeWeight = SlopePrediction * Node1 
SlopeWeight = 2 * -4 * 3 
Slopeweight = -24 

NewWeight = Weight -LearningRate *SlopeRate
NewWeight = 2 - 0.01(-24) 

#Slope Calculation Example, with two inputs and no activation function
#Code to calucalte the slopes and update the weights
Node1 = 3 
Node2 = 4 
Weight1 = 1
Weight2 = 2 

import numpy as np 
weights = np.array([1, 2]) 
inputdata = np.array([3, 4]) 
targetvalue = 6 
learningrate = 0.01
slopeprediction = (weights * inputdata).sum()
error = slopeprediction - targetvalue 
print(error) 
gradient = 2 * inputdata * error 
gradient 
#returns ([30,40}) 
weightsupdated = weights - learningrate * gradient 
predictionupdated = (weightsupdated * inputdata).sum()
errorupdated = predictionupdated - target 
print(errorupdated) 
#returns -2.5 
