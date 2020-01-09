# Import the module that stores string data
import string

# Collect and print out all ascii letters - lowercase and uppercase
letters = string.ascii_letters
print(letters)

# Collect and print out all of the numeric digits
digits = string.digits
print(digits)

######################

# Import the module that can generate random numbers
import random

# Collect and print out a random integer between 1 and 10
randomNumber = random.randint(1,10)
print(randomNumber)

# Randomly shuffle the below list and print it to the terminal
listOfValues = [1,2,3,4,5,6,7,8,9,10]
# The `random.shuffle()` function replaces the original list with the shuffled one automatically
random.shuffle(listOfValues)
print(listOfValues)

######################

# Import the module used for hashing messages
import hashlib

# Collect and print out all of the available hashing algorithms
availableHashes = hashlib.algorithms_available
print(availableHashes)
