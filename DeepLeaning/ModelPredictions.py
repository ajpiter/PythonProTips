#Just because a model has the structure of a neural network does not mean it will make good predicitions. 
#Changes in model weights can improve the model to give more accurate predications. 
#Making accurate predicitions gets harder with more hidden layers. 

#We use the loss function to aggregates errors in predicitions from many data points into a single number
#The loss function is a measure of a model's predicitive performance. 

#A common loss function for a regression task is mean squared error. 
#You square each error and take the average of that as a mesaure of model quality. 
#The smaller the loss function value the better the prediction. 

#Gradient descent is an Algorythm to find the low point of a model. 
#Steps of gradient descent is to start at a random point, and until you are somewhere flat find the slope and take a step downhill. 

#Optimizing a model with a single weight.
#We have a U shaped curve, to find the low point of a curve. 
#Pick a random point on that curve. 
#idenity activation function returns the input

# The data point you will make a prediction for
input_data = np.array([0, 3])
# Sample weights
weights_0 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 1]
            }
# The actual target value, used to calculate the error
target_actual = 3
# Make prediction using original weights
model_output_0 = predict_with_network(input_data, weights_0)
# Calculate error: error_0
error_0 = model_output_0 - target_actual
# Create weights that cause the network to make perfect prediction (3): weights_1
weights_1 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 0]
            }
# Make prediction using new weights: model_output_1
model_output_1 = predict_with_network(input_data, weights_1)
# Calculate error: error_1
error_1 = model_output_1 - target_actual
# Print error_0 and error_1
print(error_0)
print(error_1)
