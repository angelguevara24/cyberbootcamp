# Bring the OS library into the application
import os

# Prompt the user for what book they would like to read
fileName = input("What is the name of the file you want to open? ")

# Create a path from the location of the script to the file entered
filePath = os.path.join("Books", fileName + ".txt")

# Check if the file exists
# If the file exists, create a connection to it and print its contents to the terminal
if (os.path.isfile(filePath)):
    
    # Create a connection to the file
    bookFile = open(filePath)

    # Read in the text the file contains
    bookText = bookFile.read()

    # Print out the contents to the terminal
    print(bookText)

# If the file does not exist, apologize and close the application
else:
    print("Sorry! That book is not in our records! Please try again!")