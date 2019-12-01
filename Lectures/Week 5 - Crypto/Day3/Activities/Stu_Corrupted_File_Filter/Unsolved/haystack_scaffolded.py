import hashlib
import os

# Hash of original file
hash = "6341ee17b7cd8ef719d1c236cc54c3b06b043d11f399d45fca2dbf09eb55fa6f"

# Get relative path to target directory
path = input("Please enter the relative path to the directory to search. ")

# Get list of files in target direc
for filename in os.listdir(path):
    # Create path to file
    filepath = path + "/" + filename
    print(filepath)

    # Open file
    with open(filepath, "rb") as file:
        # Get contents

        # Hash the file

        # Compare to original hash
          # Print a message and break the loop if they match
    