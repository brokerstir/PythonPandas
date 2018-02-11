import pandas as pd
import numpy as np
# call library that pandas uses to generate plot, and diplay it inline
%matplotlib inline

# Use gg plot to make graphs look better
import matplotlib
matplotlib.style.use('ggplot')


# Generate random data to see a bar Plot
df = pd.DataFrame(np.random.randint(100, size=(10,4)), columns=['a', 'b', 'c', 'd'])
df.head()

# Pie and area plots are used for composition data, such as revenue from product lines
# Let the data be 10 years of revenue from 4 prducts
# Pie plot the first year
# df.ix[0].plot.pie() deprecated
df.iloc[0].plot.pie()

# df.iloc[0].plot.pie(figsize = (5,5)) ?by row

# Make pie plot of product a through time
df.a.plot.pie()

# Make an area plot
df.plot.area()

# Make area plot for single product
df.c.plot.area()
