#Enviornments are used to isolate your projects 
#To create an environment use conda create -n environmentname listofpackages 
#example 
conda create -n my_first_environment numpy pandas 

#While it is a best practice to set up an environment for a project, many people keep standard pythin 2 and python 3 environments on their computers

#To create an environment with a specific python version 
conda create -n py3 python=3 
#or 
conda create -n py2 python=2 

#Entering an environment use 
source activate my_first_environemnt
#When you are in the environment you'll see the environment name in the terminal prompt 
#The environment only has a few packages installed 
#install packages with 
conda install package_name
#will install the package only in the environment 

#Leave the environment 
source deactivate 

#In the terminal 
#Save the packages in your environments to a YAML file 
conda env export > filename.yaml

#To create an environment from a yaml file 
conda env create -f filename.yaml 
#The environment will have the same name as the yaml file 

#Listing environments 
#To see all the environments you've created on the computer
conda env list 
#The environment you are currently in appears with an * 
#The default environment is root 

#Removing environments 
conda env remove -n env_name

#Best practice to share an environment file in a github repository for a project 
