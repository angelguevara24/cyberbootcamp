
hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]

# Looping through the values in a list
for hobby in hobbies:
    print(hobby)
    print("-------------")

# range(start, stop) allows you to loop through a range of numbers
# start is the starting value (inclusive), stop is the end value (not inclusive)
for x in range(2, 5):
    print(x)
    # can reference element in list at index x
    print(hobbies[x])
print("-------------")

# Using enumeration allows programmers to loop through a list and create a counter to reference the current iteration of the loop that they are on
# `index` is an integer which points to the current iteration of the loop
# Index can be named anything - it's a variable.
# For example, we could just call it 'counter' or 'i'
# `hobby` holds the value of the current element in the `hobbies` list
for index, hobby in enumerate(hobbies):
    print(hobby + " is my #" + str(index) + " hobby")
    print("-------------")
# The above example started counter/index at #0 since that's where all Python indexes begin.

# The enumerate() function also allows programmers to choose what number to start counting from. This means they can count from 1 instead of 0 if they so desired
# This is optional.
# This means they can count from 1 or 100 instead of 0 if they so desired.
for index, hobby in enumerate(hobbies, start=1):
    print(hobby + " is my #" + str(index) + " hobby")
    print("-------------")

