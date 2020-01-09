# Cheat Sheet - Python Day 3

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

 ### os.stat

The `os.stat` function takes in a file path as a parameter and returns an object that contains metadata on that file.

 - **Example**:
    ```bash 
    The function returns:
    - st_atime = time of most recent access
    - st_size = size of file in bytes
    - st_dev = device
    - st_uid = user id of owner
    - st_mtime = time of most recent content modification
    - st_ctime = time of most recemt metadata change.
 
    # import the os library to use later
    import os 

    # Create a reference to the file path that you want to analyze
    file_path = os.path.join("Resources", "SomeCoolStuff.txt")

    # Collect the stats and save it to a variable
    statInfo = os.stat(file_path)

    # To collect the file size in bytes
    print(statInfo.st_size)

    # To collect the last time the file was accessed (opened) in unix epoch time...
    timeAccessed = statInfo.st_atime
    ```

### os.remove 

The `os.remove` function will remove a file.

 - **Example**:  
    ```bash
    # import the os library to use later
    import os 
    # If a potentially malicious file is uncovered, sometimes it is best to just remove it immediately
    # This can be done using os.remove()
    os.remove("Resources/BigOlWallpaper.jpg")
    ``` 

### datetime

The `datetime` module allows a user to convert dates and times from one format to another. 

 - **Example**:  
    ```bash
    import os
    import datetime

    # Get the stats on the file, save to fileInfo variable
    fileInfo = os.stat(file_path)

    # Collect the last time at which the file was modified
    timeModified = fileInfo.st_mtime

    # Change the format of timeModified to locale's appropriate date and time format
    timeModified = datetime.datetime.fromtimestamp(timeModified).strftime('%c')
    ```            

### zipfile

The `zipfile` module allows users with the ability to read, write, append and list a zip file.

 - **Example**:  
    ```bash
    # Import the zipfile module into the application
    import zipfile

    # Create a reference to the ZIP file you would like to extract
    zipfileReference = zipfile.ZipFile("Text.zip")

    # Run the `.extractall()` function on the variable containing the connection to the external ZIP file
    zipfileReference.extractall()

    # creating another reference, this time to a locked ZIP file
    lockedZip = zipfile.ZipFile("Books.zip")

    # Variable used to store the password string
    password = "password"

    # Running the `.extractall()` function with a password
    lockedZip.extractall(pwd=password.encode('cp850','replace'))
    ```            

-------

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
