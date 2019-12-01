# Open file in binary mode
with open("./hash_demo.py", "rb") as binary_file:
    # Get the contents as bytes 
    contents = binary_file.read()

    # Print the type of the data
    print(type(contents))

    # Print the data
    # It looks the same, but Python treats it differently!
    print(contents)
