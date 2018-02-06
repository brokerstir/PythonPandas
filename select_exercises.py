import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Practice
# Using the ix indexer

# Select records 10-15 and only name and city
data.ix[10:15, 'CustomerName':'City']


# Select all rows, specify columns by name
data.ix[:,['City', 'CustomerName']]

# Replace column  names with numbers
data.ix[:,[0, 1]]

# Splice out rows 0 - 3, including 3
data.ix[0:4]

# Pull first and last cutomer name
total = len(data)
data.ix[[0,total-1], 'CustomerName']

# One line version first and last customer name
data.ix[[0,data.tail(1).index.tolist()[0]], 'CustomerName']

data.ix[[0,len(data)-1], 'CustomerName']
