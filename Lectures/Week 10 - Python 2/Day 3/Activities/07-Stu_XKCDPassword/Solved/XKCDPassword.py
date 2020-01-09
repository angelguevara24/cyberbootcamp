# Import the secrets, os, and zipfile modules
import secrets
import os
import zipfile

# Create an empty list that will be used to store all of the words later on
completeWordList = []

# Create a connection to the "WordList.zip" file
zipConnection = zipfile.ZipFile("WordList.zip")

# Exctract all of the files inside of "WordList.zip"
zipConnection.extractall()

# Create a path to the newly created "WordList" folder
wordListFolder = os.path.join("WordList")

# Use os.walk() to navigate through the text files within the "WordList" folder
for root,dirs,files in os.walk(wordListFolder):

    # Loop through the files at the current root
    for oneFile in files:

        # Create the path that points to the current file
        currentFilePath = os.path.join(wordListFolder, oneFile)

        # Create a connection to this file in read mode and read its contents
        wordsFile = open(currentFilePath)
        wordsText = wordsFile.read()

        # Split the wordsText variable on newlines
        splitWordsText = wordsText.split("\n")

        # Loop through each element in the splitWordsText list
        for oneWord in splitWordsText:

            # Push the word into the completeWordList
            completeWordList.append(oneWord)

# Variable to store the passphrase
passphrase = ""

# Loop for however long you want the passphrase to be
for i in range(4):

  # Select a random word using the secrets module and add it to the passphrase
  passphrase += secrets.choice(completeWordList).capitalize()

# Print out the passphrase
print(passphrase)
