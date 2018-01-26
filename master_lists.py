# Master Lists for Data Science with Python 3
names = ['John', 'Mike', 'Tony']

# Use list comprehension to say Hi to each name
["Hello "+ item for item in names]

# List comprehension with condition
# Find all even numbers within 100
numbers = list(range(1, 101))

# Note the range method inside the list command
print(numbers)

# Keep only even numbers
[item for item in numbers if item % 2 == 0]
