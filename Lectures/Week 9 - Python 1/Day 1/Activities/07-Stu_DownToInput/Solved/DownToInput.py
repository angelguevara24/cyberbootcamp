# Create a variable called user_name that captures the user's first name.
user_name = input("What is your name? ")

# Create a variable called neighbor_name that captures the name of the user's neighbor.
neighbor_name = input("What is your neighbor's name? ")

# Create variables to capture the number of months the user has been coding.
months_you_coded = input("How many months have " + user_name + " been coding? ")

# Create variables to capture the number of months the user's neighbor has been coding.
months_neighbor_coded = input("How many months has " + neighbor_name + " been coding? ")

# Use math to calculate the combined months coded between the two users. 
# Store this in a variable called total_months_coded.
total_months_coded = int(months_you_coded) + int(months_neighbor_coded)

# Print results in the form:
# I am <user_name> and my neighbor is <neighbor_name>
# Together we have been coding for <total_months_coded> months!
print("I am " + user_name + " and my neighbor is " + neighbor_name)
print("Together we have been coding for " + str(total_months_coded) + " months!")