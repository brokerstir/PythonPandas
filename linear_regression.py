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

# Import library to run a regression analysis
# Y = a + bX
import statsmodels.api as sm

# Study effects of Age on rental rates, os set rental rates as Y variable
Y = df.rental_rates
# Assign age to X variable
X = df.Age
# Use native function in statsmodels to add a constant a to X
X = sm.add_constant(X)
X.head()

# Creat object for the regression
est = sm.OLS(Y,X)
# Fit the regression
est = est.fit()
# Display stats with summary funciton
est.summary()

# Regression with more than one independant variable
# Put all the independent variables into X except the first one
# X = df.ix[:,1:]
X = df.iloc[:,1:]

# Filter for only the stats you need
# For example, access only the R Squared value
est.rsquared

# Access number of observations
est.nobs

# Access degrees of freedom
est.df_model

# Type est. + tab key in Jupyter Notebook to see a list of stats to Access

# Predicted values are prepared by the object
est.predict()

# And the residue values
est.resid
