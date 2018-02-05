# Import data from external file
import numpy as np
import pandas as pd

# Import from csv
data = pd.read_csv('customers.csv')
data.head()

# by conditions
# Using column attribute is useful
# data.ix[data.CustomerID>20] is deprecated
data.loc[data.CustomerID>20]

data.loc[data.Country=='Germany']

data.loc[data.Country.isin(['Germany', 'Mexico'])]
