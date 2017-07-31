#Forward Propagation in Neural Networks 

#Inputs, value of the nodes on the far left
#Weights, the number on the line bewteen inputs and nodes
#Hidden Layer, value of the nodes on the Hidden Layer
#Output, final value 

#Each line bewteen the inputs and the nodes has a weight that shows how strongly that input affects the node
#How to solve on paper:
#HiddenLayerNode1 = (InputNode0 * WeightfromInputtoHidden1) + (InputNode1 * WeightfromInputtoHidden2)
#HiddenLayerNode2 = (InputNode0 * WeightfromInputtoHidden3) + (InputNode1 * WeightfromInputtoHidden4)
#Output = (HiddenLayer1 * WeightfromHiddentoOutput1) + (HiddenLayer2 * WeightfromHiddentoOutput2)

#Always move from inputs, to hidden layer, to output using the multiply and add process.
#Operation is similar to a dot product in liner algebra. 
#The above is forward propagation for a single data point. 
#Output is that models predicition for that data point. 

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
