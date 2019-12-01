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

# Scan `directory` for the malware
for filename in os.listdir(directory):
    filepath = directory + "/" + filename

    # Check filepath is a file, not a directory
    if os.path.isfile(filepath):
        with open(filepath, "rb") as file:
            # Hash file
            sha256 = hashlib.sha256()
            sha256.update(file.read())
            hash_to_compare = sha256.hexdigest()

            # Compare malware_hash to hash of file
            if malware_hash == hash_to_compare:
                print("Found malware hiding in: '" + filepath + "'!")
