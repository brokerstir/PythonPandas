import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
print(data.head())

# Select by column name
data['CustomerName']

# Select multiple column names
data[['City', 'CustomerName']]
# Order matters

# Select by column number
data[[1,5,2]] # Not working

# Select by attribute
data.CustomerName
