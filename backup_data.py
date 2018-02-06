import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data.head()

#ALWAYS BACKUP DATA
backup = data.copy()

# This wipes out data
data = ""
print(data)

# Restore it with the backup
data = backup.copy()
data 
