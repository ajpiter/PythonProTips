# Deep Learning Models  

Neural Networks are Deep Learning Models that take input(s) X, and predict output(s) y. Usually by goinf through a hidden layer, recurrent layer and/or kernals. 

![image](https://user-images.githubusercontent.com/28680575/112912942-bb959980-90c6-11eb-8914-963fb6160ff4.png)

As shown in the image above from Towards Ai, there are numerous types of nerural networks. Below I outline some of the more common models, and their typical use cases.  

## Dense Neural Network
In a dense neural network, every node in a hidden layer is connected with every node in the preceding layer (either input or previous hidden layer) and are the most common type of neural networks.  

- [Dense Network, Single Hidden Layer](https://github.com/ajpiter/PythonProTips/blob/master/DeepLearning/Dense_Network_Single_Hidden_Layer.ipynb): An example of the simplest of neural networks with a single input, a single hidden layer, and a single output. 
- [Dense Network, Single Hidden Layer with Two Nodes](https://github.com/ajpiter/PythonProTips/blob/master/DeepLearning/Dense_Network,_Hidden_Layer_with_Two_Nodes.ipynb): An example of how to calculate the value of hidden layers and outputs with mathmatical formulas. 
- [Image Classification Greyscale Faishon MNIST](https://github.com/ajpiter/PythonProTips/blob/master/DeepLearning/Image_Classification_Greyscale_Fashion_MNIST.ipynb): Image Classification using a single hidden layer to process greyscale images into one of 10 categorical outputs. Notebook is part of [Udacity's Intro to TensorFlow for Deep Learning](https://classroom.udacity.com/courses/ud187) course.
- [Udacity Celcuis to Fahrenheit](https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l02c01_celsius_to_fahrenheit.ipynb): An step by step walk through on how to create a neural network with a single input layer, a single hidden layer and single output.  


## Sequential Neural Network 
Nodes in a sequential neural network are only connected with a single node in the proceeding layer, making them the simplest neural networks. 
- [Digit Recoginition Model](https://github.com/ajpiter/PythonProTips/blob/master/DeepLearning/DigitRegonitionModel.py) Given an image of a number as an input, predicts which number it is as an output. Created as part of Udacity's Deep Learning Nano Degree. 

## CNNs Convolutional Neural Networks 
- CNNs are often used for image classification problems. 

## LSTM Models 

## RNNs Recurrent Neural Networks 
- RNNs are a type of sequence model that is often used in Natural Language Processing and speach recoginization. 


### Resources 
[1] Chollet, Francois. Deep Learning with Python, Second Edition. 2020. https://livebook.manning.com/book/deep-learning-with-python-second-edition/welcome/v-5/5

[2] Deep Learning Foundation Nanodegree Program. Udacity https://classroom.udacity.com/nanodegrees/nd101/dashboard/overview

[3] Iriondo, R. Shikla, P. Main Types of Nerual Networks. Towards Ai. https://pub.towardsai.net/main-types-of-neural-networks-and-its-applications-tutorial-734480d7ec8e

[4] Ng, Andrew. Deep Learning Specialization on Coursea. DeepLearning.AI. https://www.coursera.org/specializations/deep-learning

