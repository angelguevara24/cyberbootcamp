# Cheat Sheet - Python Day 2

## Key Terms

### Python Modules

 **Python Built-in Modules**: These modules are included in Python for executing different tasks. Modules are located in the Python Standard Library.

 - **Example**: The **csv module** allows users to more easily work with .csv files.  


**Import a Module**: The *import* statement is used to make a module accessible to a program.
 - **Example**: 
```bash 
    import  <module_name>   

    # In order to pull a module into a Python script, it has to be imported 
    import csv   
```

## Key Commands

## Python Built-in Modules

### math

The `math` module provides access to mathematical functions (e.g., pow).

 - **Example**: 

```bash 
 variable = math.[function(parameter(s))] 

 # The `math.sqrt()` function returns the square root of the value passed
 import math
 squareRoot = math.sqrt(25)
 print(squareRoot)  
 ```

### string

The `string` module provides functions for strings.

 - **Example**: 

    ```bash 
    variable = string.[constant]
 
    # Import the string library into the application
    import string
    # Get all ascii letters
    allAscii = string.ascii_letters
    print (allAscii)
    ```

### csv  

The `csv` module allows users to more easily work with external CSV files. CSV files can be read or written.

 - **Example**:
    ```bash 
    list_of_strings = csv.reader(csvFile_object) 

    # Import module and open a file for reading ("r" is the default)
    # Read in the data within the file
    # Contents are returned as a CSV object
    import csv
    csvFile = open("WWE-Data.csv")
    contents = csv.reader(csvFile)  
    ```

### random

The `random` module adds pseudo-random elements into a program. *random* is used for modeling and simulation as opposed to *secrets* which is used for cryptography.

 - **Example**:
    ```bash 
    variable = random.[function(parameter(s))] 
  
    # Collect and print out a random integer between 1 and 10
    import random

    randomNumber = random.randint(1,10)
    print(randomNumber) 

    # Randomly shuffle the below list and print it to the terminal
    listOfValues = [1,2,3,4,5,6,7,8,9,10]
    # The `random.shuffle()` function replaces the original list with the shuffled 
    # one automatically
    random.shuffle(listOfValues)
    print(listOfValues)
     ```
 
### secrets

The `secrets` module is used to generate cryptographically strong random numbers.

 - **Example**:
    ```bash 
    variable = secrets.[function(parameter(s))]

    # Import the secrets module into our application 
    import secrets
    # The `secrets.randbelow()` function takes in a single value and will return 
    # a random integer between it and the number 0.
    randInteger = secrets.randbelow(100)
    print(randInteger)

    # The `secrets.choice()` function takes in a list and selects a random element from within it
    myList = [1,2,3,4,5,6,7,8,9,10]
    randElement = secrets.choice(myList)
    print(randElement)
    ```

### hashlib

The `hashlib` module allows you to easily work with hash algorithms (e.g., SHA1)

 - **Example**:
    ```bash 
    variable = hashlib.[constant]
    variable = hashlib.[function(optional parameter(s))]
 
    # Import the module used for hashing messages
    import hashlib
    # Collect and print out all of the available hashing algorithms
    availableHashes = hashlib.algorithms_available
    print(availableHashes)  
    ```

### os.path

The `os` module allows a user to create scripts that are capable of looking into and working with the file or folder system of a computer regardless of its operating system. The *os.path* module provides functions to work with pathnames. 

 - **Example**: 

    ```bash 
    variable = os.path.[function (parameter(s))]
   ```

### os.path.join 

The `os.path.join` function will join one or more paths.
    
  - **Example**: 
    
    ```bash 
    # import the os library to use later
    import os 

    # The os.path.join() function creates a file path which will work for the current 
    # file system (so this code will work for any filesystem)
    real_path = os.path.join("Resources", "CoolText.txt")

    # This path can then be used for open()
    cool_text = open(real_path)
    print(cool_text.read())
    print("--------------")
    ```

### os.path.isFile 

The `os.path.isFile` function will validate the file path.

 - **Example**:  

    ```bash
    # import the os library to use later
    import os 
    # you can use isfile before you do a read to avoid errors if you're not sure the file will be there:
    fileName = input("Please enter the file you're looking for: ")

    filePath = os.path.join("Resources", fileName)

    if os.path.isfile(filePath):
        print("Found it!")
        # read the file here
    else:
        print("That file doesn't exist")
    ``` 

### os.walk

The `os.walk` function is used to navigate through a collection of folders/files. It generates the filenames in a directory tree by traversing the tree from the top or from the bottom.  The result is the root directory of the tree, followed by directories and files within directories. The *os.walk* function must always be in a *for loop*.  

 - **Example**: 

    ```bash 
    variable = os.walk.[pathname]

    # import the os library to use later
    import os

    # We're walking through the "Resources/DiaryEntries" directory.

    folder_path = os.path.join("Resources", "DiaryEntries")

    # The os.walk() function is used to navigate through a collection of folders/files
    # This function returns three values for each step it takes: root, dirs, and files.

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
            
## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
