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

# Plot a basic histogram
df.plot.hist()
# Note, bar for male does not show when outnumbered by females

# Plot the males separately
df.male.plot.hist()

# Use alpha for transparency with both genders
df.plot.hist(alpha=0.5) # alpha can range from 0 to 1

# Use stacked to add both columns and show sums
df.plot.hist(stacked=True)

# Make a box Plot
df.plot.box()
# Box plots show quartiles
