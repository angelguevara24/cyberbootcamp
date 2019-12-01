import os

directory = "DemoDirectory"

# Iterate over every file in `directory`
for filename in os.listdir(directory):
    # Creates a path to the file using the directory name
    filepath = directory + "/" + filename

    # Prints the path to the file
    print(filepath)