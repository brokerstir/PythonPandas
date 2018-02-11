import pandas as pd
import numpy as np
# call library that pandas uses to generate plot, and diplay it inline
%matplotlib inline

# Use gg plot to make graphs look better
import matplotlib
matplotlib.style.use('ggplot')

df = pd.read_excel('commercial rent.xlsx')
df.head()

# Use pandas descriptive statistics method on the data DataFrame
df.describe()
