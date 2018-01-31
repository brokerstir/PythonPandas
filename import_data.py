# Import data from external file
import numpy as np
import pandas as pd

# Import from csv
data = pd.read_csv('customers.csv')
print(data)

#Import from excel
data_excel = pd.read_excel('customers.xlsx')
print(data_excel)

# Note, default is import of first sheetname
# Speciy another sheetname as parameter
data_excel = pd.read_excel('customers.xlsx', sheetname = 'Sheet2')
print(data_excel)

# It's also easy to export data
data.to_csv('customers_out.csv')

# Note panda will add an index to exported data
#This can be turned off
data.to_csv('customers_out.csv', index = False)

# Exporting to excel is similar
data.to_excel('customers_out.xlsx')
data.to_excel('customers_out.xlsx', index = False)
