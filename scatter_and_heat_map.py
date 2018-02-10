import pandas as pd
import numpy as np
# call library that pandas uses to generate plot, and diplay it inline
%matplotlib inline

# Use gg plot to make graphs look better
import matplotlib
matplotlib.style.use('ggplot')


# Generate random data to see a bar Plot
df = pd.DataFrame(np.random.randint(100, size=(100,2)), columns=['male', 'female'])
df.head()

# Lable axes for scatter plot
df.plot.scatter(x='male', y='female')
# Scatter plot demonstrates relative distribution of two variables

# Present a third dimension
# Comput a score column
df['score']=df.male*0.3+df.female*0.7
df.head()

# Add third parameter to plot
df.plot.scatter(x='male', y='female', s=df.score)
# Size of dot will be relative to its value

# Heat map evaluates concentration of Data
# This is an advantage of scatter plots
# And also good for large observations
# Change the observation size to 10000 for example
df = pd.DataFrame(np.random.randint(100, size=(10000,2)), columns=['male', 'female'])
df.head()

# Now plot hex bin / heat map
df.plot.hexbin(x='male', y='female', gridsize=25)
# Play with grid size param
