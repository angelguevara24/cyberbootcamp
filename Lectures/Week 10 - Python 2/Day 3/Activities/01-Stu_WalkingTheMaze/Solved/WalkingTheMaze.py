# import the os library to use later
import os

# Create the file path
folder_path = "TheMaze"

# Walk through all of the files contained within "TheMaze" directory
for root, dirs, files in os.walk(folder_path):

    # Loop through the files within the current root
    for oneFile in files:

        # Add some separation between the text that will be printed this time and the next
        print("---------------")

        # Create the path to the current file
        filePath = os.path.join(root, oneFile)

        # Create a connection to the file in read mode
        openedFile = open(filePath)

        # Read in the text of the current file
        fileText = openedFile.read()

        # Print out the location of the file found
        print("File found at " + filePath)

        # Print out the text that was inside of the file
        print(fileText)
