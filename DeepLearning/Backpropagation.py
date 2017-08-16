#Backpropagation 
#Calculate the slopes you need to optizime more complex deep learning models (vs. Gradient Descent) 
#By estimating the slope of the loss function with regard to each weight 

#Takes the error from the output layer 
#through the hidden layers 
#towards the input layer 

#Use a library to implement this, rather than doing the math yourself 

#Always do forward propagation to calculate predictions and errors before doing backpropagation 
#After forward propagation, go back one layer at a time
#Gradients for weight is product of 
#node value feeding into that weight 
#slope of loss function of the node it feeds into 
#slope of activation function at the node it feeds into 
