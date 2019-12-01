import hashlib
import os

# Get paths to malware sample and directory to scan
malware = input("Please enter the relative path to the malware you'd like to scan for. ")
directory = input("Please enter the relative path to the directory you'd like to scan. ")

# Generate hash signature for malware
with open(malware, "rb") as file:
    sha256 = hashlib.sha256()
    sha256.update(file.read())
    malware_hash = sha256.hexdigest()

# List all the files in `directory` and loop through them
    # Create the filepath directory + "/" + filename

    # TODO: Check filepath is a file, not a directory (check cheatsheet!)
        # TODO: Open filepath in "rb" mode
            # TODO: Hash file

            # TODO: Compare malware_hash to hash of file
                # Print a message they match
