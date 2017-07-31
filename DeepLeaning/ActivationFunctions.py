#Examples from DataCamp 

#For neural networks to achieve thier maximum predicative power we must apply an activation function. 
#Activation Function allows the function to capture nonlineriaties 
#Linear functions are represented on a graph by stright lines 
#Nonlinear functions are represented on a graph with curved lines 

#Activation functions are applied to node inputs to produce node output 

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

#Todays standard activation function is the ReLU (Rectified Linear Activation) 
#Has two linear pieces is suprisingly powerful when compossed through multiple seccessive hidden layers
#Math Formula RELU(x) = {O if x<0, x if x>=0}

#Example of a relu() activation function. 
#The rectified linear activation function, takes a single number as an input, 
#returning 0 if the input is negative and the input if the input is positive. 

def relu(input):
    output = max(0, input)
    return(output)
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)
hidden_layer_outputs = np.array([node_0_output, node_1_output])
model_output = (hidden_layer_outputs * weights['output']).sum()
print(model_output)

#Applying the network to many observations or rows of data 
# Define predict_with_network()
def predict_with_network(input_data_row, weights):
    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)
    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)
    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)
    # Return model output
    return(model_output)
# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))
# Print results
print(results)
