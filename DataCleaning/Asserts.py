#Asserts allow you to write a statement to verify something you would usually look for with an .info()
#An example would be to verify that there are no NaNs
#If an assert statement is true nothing happens
#If an assert statement is false then you will get an error

assert database.column.notnull().all()
assert pd.notnull(dataframe).all().all()
assert(dataframe >= 0).all().all()

# Test if column is of type object
assert dataframe.column.dtypes == np.object

# Test if column is of type int64
assert dataframe.column.dtypes == np.int64

# Test if column is of type float64
assert dataframe.column.dtypes == np.float64
