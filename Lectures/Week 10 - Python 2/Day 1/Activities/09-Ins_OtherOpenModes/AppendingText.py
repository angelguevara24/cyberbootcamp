###############
# APPEND MODE #
###############

# The "a" mode stands for append and allows the application to add new text onto the end of an existing file
notesFile = open("Notes.txt", "a")

# The .write() method in conjunction with the append mode will write to the end of a file
notesFile.write("\nThis is a completely new line of text created by the APPEND mode.")

# Closing the file
notesFile.close()

################
# READING MODE #
################

# Opening up the file once more in read mode to see the changes that were made
notesFile = open("Notes.txt", "r")

# Reading in the existing text to the terminal
notesText = notesFile.read()
print(notesText)

# Closing the file
notesFile.close()
