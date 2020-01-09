# Import the secrets library into the application
import secrets

# Import the string library into the application
import string

# Connect to an external file called "PasswordList.txt" in write mode
passwordFile = open("PasswordList.txt", "w")

# Get all ascii letters and numbers and combine them into one long string
allCharacters = string.ascii_letters + string.digits

# Create a loop that will run for 100 iterations
for x in range(100):

    # Create an empty string that will be used to hold the random password being generated
    password = ""

    # Create a loop that will run for 10 iterations
    for y in range(10):

        # Collect a random character and add it into the password
        password = password + secrets.choice(allCharacters)
    
    # Write the complete password to the external file
    passwordFile.write(password + "\n")