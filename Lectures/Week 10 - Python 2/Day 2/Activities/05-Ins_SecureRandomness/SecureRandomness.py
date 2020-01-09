# Import the secrets module into our application
import secrets

# The `secrets.randbelow()` function takes in a single value and will return a random integer between it and the number 0.
randInteger = secrets.randbelow(100)
print(randInteger)

# The `secrets.choice()` function takes in a list and selects a random element from within it
myList = [1,2,3,4,5,6,7,8,9,10]
randElement = secrets.choice(myList)
print(randElement)