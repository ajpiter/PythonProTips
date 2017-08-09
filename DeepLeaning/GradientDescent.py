#Gradient Descent 

#repeatedly find a slope to find how your lost function changes as the weight changes
#then made a small change to the weight to get to a lower point 
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
