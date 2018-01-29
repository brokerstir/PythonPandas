# Import libraries
import numpy as np
import pandas as pd

# Create series by giving scalar value
pd.Series(3.14)
pd.Series(3.14, index = ['a','b','c'])

# Create series using dictionary
d = {'0':'a', '1':'b', '2':'c'}
pd.Series(d)

# Create from numpy array
arr = np.random.randn(5)
pd.Series(arr)

# Or pass a custom index
pd.Series(arr, index = ['a','b','c','d','e'])
