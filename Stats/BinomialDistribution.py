#A binomial distrubution is the number of r successes in n Bernoulli trials with probability p of success. 

#Example, The number of heads in 4 coin flips of a fair coin. 
np.random.binomial(The number of coin flips, the proability of success) 
np.random.binomial(4, 0.5) 

#To conduct the experiment repeatedly use the size= argument 
np.random.binomial(4, 0.5, size=10) 

#to plot the binomial PMF  
import numpy as np 
variables = np.random.binomial(The number of trials, the probability of success, size=10000)

#To plot the binomial CDF 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set()
x, y = ecdfd(samples) 
_ = plt.plot(x, y, marker='_', linestyle='none')
plt.margins(0.02) 
_ = plt.xlabel('Label')
_ = plt.ylabel('Label') 
plt.show()
