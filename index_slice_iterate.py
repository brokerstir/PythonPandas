import numpy as np
a = np.arange(10)**2
print(a)

# Get array element by index
a[3]

# Slice part of array
# Last number not inclusive
a[2:7]

# Omit first parameter to select from beginning
a[:7]

# Same concept with last parameter
a[7:]

a[:] # == a

# Iterate through array
for i in a:
    # Do something
    print(np.sqrt(i))

# Iterate through array and perform function
def f(x): return 0
for i in a:
    print (f(i))

# Work with multi dimensional array
b = np.arange(20).reshape(4,5)
print(b)

# Grab element by index
b[1,4]

# Slice
b[1:3,2:4]
