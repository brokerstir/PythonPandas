import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Alwasy backup
backup = data.copy()

# Setting specific column as new index
data.set_index('CustomerName')
# Sets CustomerName as indexer

# Caution abut setting index with column of non unique values
temp = data.set_index('City')
# temp.ix['London'] is deprecated
temp.loc['London']
# Note, five results show because London is not unique

# Tip, veryify index will be unique
temp = data.set_index('City', verify_integrity = True)

# Restore original indexe
data.reset_index()
# Restore but prevent copied column of index 
data.reset_index(drop=True)
