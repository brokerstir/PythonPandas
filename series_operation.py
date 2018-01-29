import numpy as np
import pandas as pd

# Create one dimension array
arr = np.random.randn(5)
# Create series
srs = pd.Series(arr)
print(srs)

# Pick index
print(srs[1])
# Slice it
print(srs[2:])
# Pick multiple elements
print(srs[[3,0,4]])
# Calculate
print(srs **2)
