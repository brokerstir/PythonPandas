# Import data from external file
import numpy as np
import pandas as pd

# Import from csv
data = pd.read_csv('customers.csv')
data.head()

# data.ix[0,4] is deprecated
data.iloc[0,4]

# Slice columna and rows
# Intersecton of rows 0-3, and cols 4-7
data.iloc[0:3,4:7]

# Select using column names
data.ix[0, 'City']

data.ix[0:3, 'CustomerName':'City']

# Pick only the heads
data.ix[:, 'CustomerName':'City'].head()
