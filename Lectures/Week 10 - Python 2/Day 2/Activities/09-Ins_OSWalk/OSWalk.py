# import the os library to use later
import os

folder_path = os.path.join("Resources", "DiaryEntries")

# The os.walk() function is used to navigate through a collection of folders/files
# This function returns three values for each step it takes: root, dirs, and files
for root, dirs, files in os.walk(folder_path):

    # The root is the folder that is currently being searched through
    print("Currently inside of... " + root)

    # The dirs list stores all of the names of the folders inside the current root
    print("The folders in here are..." + str(dirs))

    # The files list stores all of the names of the files inside the current root
    print("The files in here are..." + str(files))
    print("~~~~~~~~~~")

print("--------------")

# In order to construct the file path to use dynamically...
for root, dirs, files in os.walk("Resources"):

    # Loop through all of the files in the current root
    for file_name in files:

        # Create a path by combining (joining) the root and the file name
        current_file_path = os.path.join(root, file_name)
        print(current_file_path)

        # We can then check that the file exists through using os.path.isfile()
        print("EXISTS: " + str(os.path.isfile(current_file_path)))
