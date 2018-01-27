# Python practice part 1
# Master these string methods for data science with Python 3

# String.replace
# Returns a copy of the string where old characthers are replaced by new ones
# Syntax string.replace(old, new)

ques = "Hello, world! How are you today?"
print (ques.replace("today","doing"))
# Note, this method does not change the value of original string
print(ques)

#String.split
# Returns a list of all the words in the string, using the str as the separator
# Syntax: string.split(str)

print(ques.split())
# Note, space is default separator
# Specify spearator as follows
print(ques.split("o"))

#String.join
# Returns a string in which the string elements of sequence have been joined with the string itself as the separator
# Syntax: string.join(sequence)

words = ques.split()
print(words)
# Speciy how you join
print(" ".join(words))
print("-".join(words))

# String.startswith / String.endswith
# Returns a Boolean value indicating whether the string starts / ends with the given String
# Syntax: string.startswith(str) / string.endswith(str)

print(ques.startswith("Hello"))
print(ques.endswith("!"))
# Expect it to return a boolean value
