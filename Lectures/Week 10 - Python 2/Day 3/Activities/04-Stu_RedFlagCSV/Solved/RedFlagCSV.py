# Import the two modules that will be used in this code
import os
import datetime

# Create a connection to the CSV file this application will write to
csvFile = open("RedFlags.csv", "w")

# Since there are so many files, os.walk would be wise
for root, dirs, files in os.walk('Text'):

    print("GETTING FILE INFO")
    # Loop through all of the files in the current root
    for file_name in files:

        # Create the path to the current file
        file_path = os.path.join(root, file_name)

        # Get the stats on the file, save to fileInfo variable
        fileInfo = os.stat(file_path)

        # Collect the last time at which the file was modified
        timeModified = fileInfo.st_mtime

        # Change the format of timeModified to datetime format
        timeModified = datetime.datetime.fromtimestamp(
            timeModified).strftime('%c')

        # Collect the file size of the file
        fileSize = fileInfo.st_size

        # Write the new line of data into the external CSV file
        csvFile.write(file_path + "," + str(fileSize) + "," + timeModified + "\n")

# Close the CSV file
csvFile.close()