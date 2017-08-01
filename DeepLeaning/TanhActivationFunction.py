#Example of a tanh() activation function 
import numpy as np 
input_data = np.array([-1, 2])
weights = {'node_0': np.array([3, 3]), 'node_1': np.array([1, 5]), 'output': np.array([2, -1])}
#distingueses the input from the output in each node 
node_0_input = (input_data * weights['node_0']).sum()
#apply the tanh() to convert the input to the output 
node_0_output = np.tanh(node_0_input)
node_1_input = input_data * weights['node_1']).sum()
node_1_output = np.tanh(node_1_input)
hidden_layer_outputs = np.array([node_0_output, node_1_output])
output = (hidden_layer_output * weights['output']).sum()
print(output) 
