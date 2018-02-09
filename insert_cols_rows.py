import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Alwasy backup
backup = data.copy()

# Use insert command
# 3 params are position, name, data source
data.insert(0, 'New Column', data.City) #inplace
# Note, this modifies existing data
data.head()

# Insert row: slice data, stick in new row, stitch back together
# So, first creat Python dict
info = {'CustomerID':420, 'CustomerName':'Intruder', 'ContactName':'Parents', 'Address': 'Nowhere', 'City': 'Utopia', 'PostalCode': 'LST 1030', 'Country': 'Heaven'}

# Then convert dict to data frame object
line = pd.DataFrame(info, index=[3]) # index specifies rows

# Concatenate DataFrame
pd.concat([data.iloc[:2], line, data.ix[3:]]).reset_index(drop=True) # not inplace
# Must reset index or else have 2 third rows

# Note, manual input of data is rare. An alternative is to use SQL or Excel and import the data again. 
