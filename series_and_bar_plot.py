import pandas as pd
import numpy as np
# call library that pandas uses to generate plot, and diplay it inline
%matplotlib inline

# Use gg plot to make graphs look better
import matplotlib
matplotlib.style.use('ggplot')

# Make a series plot to show time series data, such as stock price
# Yahoo finance was used to download 3 years of data of stock for Apple
aapl = pd.read_csv('aapl.csv')
aapl.head()

# Reverse dataframe so it's oldest to newest
aapl = aapl[::-1]

# Plot adjusted close price
# Pandas gives series plot by default
# Adjusted closed is preferred becasue it accounts for dividends, buybacks, etc.
aapl['Adj Close'].plot() # series plot by default

# A bar plot would be made with
# appl['Adj Close'].plot.bar()
# A bar is made for each observation and with three years of data that's almost 100 observations.
# Not very useful

# Generate random data to see a bar Plot
df = pd.DataFrame(np.random.randint(100, size=(5,2)), columns=['male', 'female'])
df.head()
# Now bar Plot
df.plot.bar()
