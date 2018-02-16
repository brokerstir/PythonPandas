import numpy as np
a = np.arange(9).reshape(3,3)
print(a)

# Get the sum of array
a.sum()

# Find the min and max
a.min()

a.max()

# Average
np.average(a)

# Std Deviation
np.std(a)

# Get array for sum of each row
a.sum(axis=1)

# Get array for sum of each col
a.sum(axis=0)

# Get avg for each column
np.average(a, axis=0)
