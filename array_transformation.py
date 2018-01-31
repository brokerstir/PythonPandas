import numpy as np
# Make 2 dimensional array, 4 rows and 7 columns
a = np.arange(28).reshape(4,7)
# View shape of this array
print(a.shape)

# Transpose the array
print(a.T)

# Force to 1 dimensional array
print(a.ravel())

# Reshape array but product of dimension must be equal to total elements in the array
print(a.reshape(2,2,7))

# Stack arrays vertically or horizontally
# Consider two 2 dimension arrays
a = np.array([[8,-1],[4,9]])
b = np.array([[0.2,0.9],[-0.02,0.04]])

# Vertically stack arrays
# Order matters
print(np.vstack((a,b)))

# Horizontally
print(np.hstack((a,b)))

# Split arrays
v = np.vstack((a,b))
h = np.hstack((a,b))
print(h)
print(v)

# Give number of fractions you want h Split
print(np.hsplit(h,2))

# Do it vertically with v
print(np.vsplit(v,2))
