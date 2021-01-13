#DataCamp Tutorial Installing Jupyter Notebook: https://www.datacamp.com/community/tutorials/installing-jupyter-notebook
#Difference between Jupyter Notebook and Jupyter Lab 

1. Launch through Terminal  
2. Launch through Anaconda

# Launch Through Terminal 

## Install Jupyter notebook through Pip 
#In the terminal run the following code 
pip3 install virtualenv
virtualenv jupyter
source jupyter/bin/activate
pip3 --version
pip3 install -U pip setuptools
pip3 install jupyter

## Launch Jupyter notebooks in your terminal by writting: 
jupyter notebook 

## 

# Install Notebook Conda to help manage your environments: 
conda install nb_conda
#If you run the notebook server from a conda environment you'll also have access to the Conda tab. 
#The Conda tab allows you to manage your environments within Jupyter. 

#Shutdown Indivdual Notebooks 
#In the browser click the checkbox and click shutdown
#shutdown the entire server 
Control C, Control C 

# Notebook Interface 

![image](https://user-images.githubusercontent.com/28680575/104406521-7af99b80-552d-11eb-9d64-bc40f3d0b9a2.png)

#Cells are in green boxes, and where you will write your code. 
#The play button runs the code in the cell, and displays the output below the cell. 
#Cells get numbered based on when you ran the code.
#Running the cell in markdown mode creates text. 
#Command Palette allows you to search for what you want to do. 

#Any code executed in one cell is available in all other cells 
