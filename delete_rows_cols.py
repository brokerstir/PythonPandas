import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

# Alwasy backup
backup = data.copy()

# Drop the city column
data.drop('City', 1) # 1 for col and 0 for row
# Original data still has city column

# Drop multiple columns
data.drop(['City', 'CustomerName'], 1)

# Drop row 5
data.drop(5, 0)

# Drop multiple rows
data.drop([0,2,4,7],0)


# Delete column by condition
data[data.Country != 'Germany'] # Drop customers from Germany

# Drop ID <= 50
data[data.CustomerID > 50]
