#Validation data is data that is held from training and only used to test model performance
#A model's performance in training data is not a good indicatior of how it will perform on new data
#Cross Validation is not usedin deep learning, because it would take oo long on large datasets 

#Use Keras to split your data, keeping some for validation 
#specifiy the split using the fit method with validation_split equal to the percentage of your data held back 
#Example, model.fit(predictors, target, validation_split=0.3) would hold back 30% of data for validation

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']
model.fit(predictors, target, validation_split=0.3) 

#Early Stopping 
#Keep training while validation is improving and stop training when validation isn't improving 
#patience is how many epochs the model can go without improving before we stop training 

from keras.callbacks import EarlyStopping 
early_stopping_monitor = EarlyStopping(patience=2)
model.fit(predictors, target, validation_split=0.3, epochs=20, callback=[early_stopping_monitor])

#Keras will go until the number of epochs is reached or the validation rate stops improving (early stopping) 
#By default, keras runs 10 epochs unless you specify 
