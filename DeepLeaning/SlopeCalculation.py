#Slope Calculation Example 
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
