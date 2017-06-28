np.mean(np_array[:,0])
np.median(np_array[:,0])
np.corrcoef(np_array[:,0], np_array[:,1])
np.std(np_array[:,0])

# for 1st and 3rd quartiles plus the median 
np.percentile(dataset['columnname'], [25,50,75])
