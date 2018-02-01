import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Select Rows by index
data[0:4]

# Syntax for select one rows
# data.ix[0] method is deprecated
data.iloc[0]

# Select a list of rows
data.iloc[[1,3]]

# Slice a set of Rows
data.iloc[3:10]
