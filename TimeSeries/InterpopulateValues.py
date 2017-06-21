Interpopulate Values 

#file is sampled every ten years 
population = pd.read_csv('filename.csv', parse_dates=True, index_col='Date')

#we can upsample the population to sample for every year. 
#Using the .first method, pandas fills in NaN for years in bewteen. 
population.resample('A').first()

#better to fill in with other interpertaions, below the vaules are filled in with a linear sample. 
population.resample('A').first().interpolate('linear')
