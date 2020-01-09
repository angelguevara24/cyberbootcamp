# Import the secrets, os, and zipfile modules


# Create an empty list that will be used to store all of the words later on


# Create a connection to the "WordList.zip" file


# Exctract all of the files inside of "WordList.zip"


# Create a path to the newly created "WordList" folder


# Use os.walk() to navigate through the text files within the "WordList" folder
for root,dirs,files in os.walk(wordListFolder):

    # Loop through the files at the current root


        # Create the path that points to the current file
       

        # Create a connection to this file in read mode and read its contents
     
     

        # Split the wordsText variable on newlines


        # Loop through each element in the splitWordsText list
 

            # Push the word into the completeWordList


# Variable to store the passphrase


# Loop for however long you want the passphrase to be


  # Select a random word using the secrets module and add it to the passphrase
  
  
# Print out the passphrase
