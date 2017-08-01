#Many neural networks will have more than one hidden layer. 
#Always move from inputs, to hidden layer, to output using the multiply and add process.
#Operation is similar to a dot product in liner algebra. 

#How to solve on paperwith two hidden layers:
#HiddenLayerNode0 = (InputNode0 * WeightfromInputtoHidden1) + (InputNode1 * WeightfromInputtoHidden2)
#HiddenLayerNode1 = (InputNode0 * WeightfromInputtoHidden3) + (InputNode1 * WeightfromInputtoHidden4)
#HiddenLayer1Node0 = (HiddenLayerNode0 * WeightfromHiddentoHidden5) + (HiddenLayerNode1 * WeightfromHiddentoHidden6)
#HiddenLayer1Node1 = (HiddenLayerNode0 * WeightfromHiddentoHidden7) + (HiddenLayerNode1 * WeightfromHiddentoHidden8) 
#Output = (HiddenLayer1Node0 * WeightfromHiddentoOutput) + (HiddenLayer2Node1 * WeightfromHiddentoOutput1)

#Always move from inputs, to hidden layer, to output using the multiply and add process.
#Operation is similar to a dot product in liner algebra. 


import numpy as np 
#input_data = np.array([InputNode0, InputNode21)
input_data = np.array([2,3]) 
#weights = {'input0': np.array([WeightfromInputtoHidden1, WeightfromInputtoHidden2]), 
    #'node_1: np.array([WeightfromInputtoHidden3, WeightfromInputtoHidden4]), 
    #'output': np.array([WeightfromHiddentoOutput1, WeightfromHiddentoOutput2])}   
weights = {'node_0': np.array([1, 1]), 'node_1': np.array([-1, 1]), 'output': np.array([2, -1])}
node_0_value = (input_data * weights['node_0].sum()
node_1_value = (input_data * weights['node_1']).sum()
hidden_layer_values = np.array([node_0_value, node_1_value])
#to confirm the values of the hidden layer you could print them
# print(hidden_layer_values) 
output = (hidden_layer_values * weights['output']).sum()
print(output) 

                     
#Deep networks build representations of patterns in the data that are useful for making predicitions.
#The more hidden layers they go through the more complex patterns they find
