# Master dictionaries for Data Science with Python 3

# Ptyhon dictionaries are made up of key / value pairs, separated by a comma. Each key must be unique.

drink = {
    'type' : 'coffee',
    'quantity' : 'a cup'
}

# Use the key to reference its value
drink['type']

# Use a dictionary for dynamic content
print("Would you like " + drink['quantity'] + " of " + drink['type'] + "?")

# Update a dictionary

# Create a new entry
drink['brand'] = 'Starbucks'
print(drink)

# Change value of existing entry
drink['type'] = 'black coffee'
print(drink)

# Delete elements
# Remove entry with key name
del drink['brand']
print(drink)
# Remove all entries
drink.clear()
print(drink)

# Dictionary drink is clear, so recreate
drink = {
    'type' : 'coffee',
    'quantity' : 'a cup'
}

# Functions and methods
# .keys() return a list of keys
print(drink.keys())

# .values() return a list of values
print(drink.values())

# .items() return a list of items
print(drink.items())

# Above methods often used wth for loops
