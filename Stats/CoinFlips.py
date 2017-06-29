#Use simulated repeated measurements to compute probabilities
#np.random is a suite of functions based on random number generation 
#draws a number bewteen 0 and 1 
np.random.random()

#integer fed into random number which will produce the same random results everytime 
np.random.seed()

#Bernoulli trial, an experiment that has two opitions, success (true) and failure(false) 

# Example, Coin Flips to achieve four heads out of four flips 
#where heads is represented as a number less than .5 
#size= the number of random numbers we want 
import numpy as np 
np.random.seed(42)
random_numbers = np.random.random(size=4) 
random_numbers
heads = random_numbers <0.5 
heads 
np.sum(heads) 

#The probability of getting four heads if we were to repeat the experiment 
#initialize the count to 0
n_all_heads = 0 
for _ in range(10000):
  heads = np.random.random(size=4) < 0.5 
  n_heads = np.sum(heads)
  if n_heads == 4:
    n_all_heads += 1
n_all_heads / 10000
