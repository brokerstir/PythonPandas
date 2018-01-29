# Functions
# Functions are groups of code

# def function(parameters):
    # do something
    # return something

def greet(name):
    print("Hello {0}".format(name))
    # Note, this function doesn't return anything

greet("John")

# Loop throug list with greet Function
names = ['John', 'Mike', 'Tony']

for name in names:
    greet(name)

# If condition in Function
def decide(temp):
    hot = 30
    warm = 20
    chill = 10
    freezing = 0
    cloth = ''
    if temp > hot:
        cloth = 'T-shirt'
    elif temp > warm:
        cloth = 'shirt'
    elif temp > chill:
        cloth = 'jacket'
    elif tem > freezing:
        cloth = 'sweater'
    else:
        cloth = 'coat'
    return cloth

# Call function using variable
clothes = decide(18)
print (clothes)
