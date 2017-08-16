#Steps to create a Keras Model 
#1 Specify architecture 
#2 Comile 
#3 Fit 
#4 Predict 

#ncols equals the number of nodes in the input layer 
#multiple types of models, sequential is the easiest 
#in a sequential model each layer has weights only to the layer coming directly after it 
#dense is the standard layer type 
#in a dense layer all the nodes in the previous layer connect to all the nodes in the current layer 

import keras
from keras.layers import Dense
from keras.models import Sequential
# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
# Set up the model: model
model = Sequential()
# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
# Add the second layer
model.add(Dense(32, activation='relu'))
# Add the output layer
model.add(Dense(1))
