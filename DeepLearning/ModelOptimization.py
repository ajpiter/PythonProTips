#Model Optimization 
#Optimal value of one weight depends on the value of other weights 
#Weight updates may not improve the model meaningfully 
#A small learning rate might cause such small updates to the models weights that the model does not improve 
#A large learning rate might take the model too far 

#Stochastic Gradient Descent (SGD)
#SGD is an optimizer that uses a fixed learning rate 
#Start by using a function that creates a new model
#create models in a for loops 
#each time we loop through, we compile the model using SGD with a different learning rate 

 #We have created a function get_new_model() that creates an unoptimized model to optimize.


from keras.optimizers import SGD
def get_new_model(input_shape = input_shape): 
  model = Sequential()
  model.add(Dense(100, activation='relu', input_shape = input_shape)) 
  model.add(Dense(100, activation='relu'))
  model.add(Dense(2, activation='softmax'))
  return(model)   
#Create a list of learning rates 
lr_to_test = [.000001, 0.01, 1] 
#Loop over the learning rates 
for lr in lr_to_test:
  #Build new model to test, unaffected by previous models
  model = get_new_model()
  #Create SGD optimizer with specified learning rate: my_optimizer
  my_optimizer = SGD(lr=lr) 
  #Compile the model
  model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')
  #Fit the model
  model.fit(predictors, target) 


  
