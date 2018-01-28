# Loops
# Loops do repetitive things efficiently

# The for loop is most common

# for item in sequence
    # do something

# Loop through a string
string = 'Do repetitive things efficiently.'

for character in string:
    print(character)

# Loop through a list
list = ['white', 'yellow', 'blue', 'black']

for word in list:
    print(word)

# Loop through a dictionary
dict = {'color':'white', 'shape':'circle', 'size':10}

for key, value in dict.items():
    print("{0} --> {1}".format(key,value))
