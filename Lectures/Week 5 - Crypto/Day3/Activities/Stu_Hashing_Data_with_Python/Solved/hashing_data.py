import hashlib

# TODO: Open a file to hash
with open("./hash_me", "rb") as file:
    # TODO: Store the file contents in a variable
    contents = file.read()

    # TODO: Create MD5 and SHA256 objects
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    # TODO: Generate the hexdigests of the file contents
    md5.update(contents)
    sha256.update(contents)

    md5_hash = md5.hexdigest()
    sha256_hash = sha256.hexdigest()
    
    # TODO: Print the hexdigests to the terminal
    print("Hashes for ./hash_me\n")
    print("[MD5]:\t\t", md5_hash)
    print("[SHA256]:\t", sha256_hash)
