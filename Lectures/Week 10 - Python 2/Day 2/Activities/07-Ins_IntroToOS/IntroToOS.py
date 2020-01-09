# import the os library to use later
import os

# The os.path.join() function creates a file path which will work for the current file system (so this code will work for any filesystem)
real_path = os.path.join("Resources", "CoolText.txt")

# This path can then be used for open()
cool_text = open(real_path)
print(cool_text.read())
print("--------------")


# The os.path.isfile() function returns True if the file path provided points to an actual file, false otherwise
fake_path = os.path.join("Resources", "NotAFile.txt")
print(os.path.isfile(real_path))
print(os.path.isfile(fake_path))
print("--------------")


# you can use isfile before you do a read to avoid errors if you're not sure the file will be there:
fileName = input("Please enter the file you're looking for: ")

filePath = os.path.join("Resources", fileName)

if os.path.isfile(filePath):
    print("Found it!")
    # read the file here
else:
    print("That file doesn't exist")