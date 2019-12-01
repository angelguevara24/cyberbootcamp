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
        contents = file.read()

        # Hash the file
        sha256 = hashlib.sha256()
        sha256.update(contents)
        hash_to_compare = sha256.hexdigest()

        # Compare to original hash
        if hash == hash_to_compare:
            print("Found original file at: '" + filepath + "'!")
            break
    