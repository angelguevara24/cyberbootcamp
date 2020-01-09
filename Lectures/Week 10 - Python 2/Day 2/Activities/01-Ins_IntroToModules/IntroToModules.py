# In order to pull a module into script, it has to be imported
import math

# When working with the values/functions stored within a module, generally you will have to name the module and then use dot notation to access the function

# The `math.pow()` function takes in two values and returns the value of the first raised to the power of the second
squaredNumber = math.pow(4,2)
print(squaredNumber)

# The `math.sqrt()` function returns the square root of the value passed
squareRoot = math.sqrt(25)
print(squareRoot)

# The `math.ceil()` function returns the smallest integer that is not less than the value passed
ceilingInteger = math.ceil(100.75)
print(ceilingInteger)

# The `math.floor()` function returns the largest integer that is not greater than the value passed
floorInteger = math.floor(200.99)
print(floorInteger)