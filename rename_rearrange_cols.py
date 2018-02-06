import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Alwasy backup
backup = data.copy()

data.rename(columns={'ContactName':'Salesman'})

# Rename multiple columns
data.rename(columns={'ContactName':'Salesperson', 'CustomerID':'ID'})

# Note, new values are not being stored, but only displayed. Original data is intact
data

# Rearrange the columns
# First step, output column names to a list
data.columns.tolist()

# Save it to a veriable
cols = data.columns.tolist()
# Reverse the list
cols =  cols[::-1]

# Reorder data frame
data[cols]

# Can also reorder with ix indexer
data.ix[:, cols]
