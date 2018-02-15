import numpy as np

# Create an index array 0 - 9
np.arange(10)

# Provide steps of couting
np.arange(0,100,2)

# Evenly fill gap between space
np.linspace(0,10,3)

np.linspace(0,10,4)

# Fill array with zeros or ones
np.zeros((2,2,3))

np.ones((2,2))

# Create random empty array
np.empty((9,9))

# Create array from python list
from_list = np.array([3,7,11])
from_list

# Create from a tuple
from_tuple = np.array((11,7,3))
from_tuple

# Create multi dimensional array from nested list
multi = np.array([[0,0],[1,1]])
multi
