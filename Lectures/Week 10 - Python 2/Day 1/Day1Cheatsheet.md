# Cheat Sheet - Advanced Python Day 1

## Key Terms

### File Handling

- **File Object**: A file object allows a program to read and write data from external files. 

  - **Example**: See examples below.

- **Opening a File**: The `open()` function returns a **file object** we can save to a variable for use later in the application. The **external_filename** used in the function is the relative or absolute path to the file to open. 

   -  **Example**:  
  ```bash 
  file_object = open(external_filename, access_mode)    

  where access_mode:
  r = open the file to "read data" from the file
  w = open the file to "write data" to the file
  a = open the file to "append data" to the file

  # Using the open() function to read data from a file.  
  diary_txt_file = open("Diary.txt","r")
  ```

- **Reading a File**: The `file_object.read()` function uses a file_object to read through the *entire* file and returns a string version of the contents. The external file must first be opened using the **"r"** access mode. The "r" access mode is the default and can be obmitted.

  - **Example**:
  ```bash 
  string = file_object.read()    
 
  # Using the .read() function read to data from the external file.
  # The function places the text from the file into the string "diaryText"
  diary_txt_file = open("Diary.txt","r")
  diaryText = diary_txt_file.read()    
  ``` 

- **Writing Data to a File**: The `file_object.write()` function uses the file_object to write data to an exernal file. The external file must first be opened using the **"w"** access mode.

  - **Example**:
  
  ```bash 
  file_object.write(string)    
 
  # Open the file in "write" access mode
  diary_txt_file = open("Diary.txt","w")
  diary_txt_file.write("I don't write in diaries.")  
  ```

- **Appending Data to a File**: The `file_object.write()` function uses a file_object to **add new text** onto an **existing file**. The external file must first be opened using the **"a"** access mode.

  - **Example**: 

  ```bash 
  string = file_object.write(string)    

  # Open the file in "append" access mode.
  diary_txt_file = open("Diary.txt","a")
  diary_txt_file.write("This is the start of a new entry") 
  ```

- **Closing a File**: The `file_object.close()` function closes the connection to the file.  This is not necessary but it is a good habit to form to free up system resources.

  - **Example**:

  ```bash 
  file_object.close()    
 
  # The read() function reads data from the file using the file_object.
  diary_txt_file.close()    
  ``` 

### String Functions

- **split Function**: The `split()` function splits a string into a list. `split()` uses a delimiter in the data (e.g., a space) to separate the data.

  - **Example**: 

  ```bash 
  string.split(separator, [optional max no. of splits])        

  # The split() function breaks the string apart based on spaces.
  line =  "IP Address 192.168.1.1"
  word = line.split(" ")
  print word[0]
  print word[1]
  print word[2]
  ```

- **find Function**: The `find()` function determines if the substring passed into it as a parameter occurs anywhere within the text the method is being run on. 

  - **Example**: 

  ```bash 
  string.find(value, [optional start], [optional end])        

  # The find() function looks for the word "Harry"
  line =  "Harry Porter Books"
  if line.find("Harry") > -1:
    print("Found Harry")
  ```


## Key Commands

## Python Functions

### File Operations

#### Open a file.

```bash 
# The open() function creates a connection to an external file
# The parameter passed into the function is the relative or absolute path to file to open
# The "r" parameter indicates that we are reading from a file.
diary_txt_file = open("Diary.txt","r")
  ```

#### Read data from a file.

```bash 
# Using the .read() function to read the file's contents
diaryText = diary_txt_file.read()
print(diaryText)
```

#### Write data to a file.

```bash 
# The .write() function is then used to push the text into the external file
diary_file.write("I don't write in diaries.")
```

#### Append data to a file.

```bash 
# The .write() function is then used to push the text into the external file
diary_file.write("This is the start of a new entry.")
```

#### Close connection to a file.

```bash
# The .close() function to close the connection to the external file in order to save memory
diary_txt_file.close()
```

### String Functions

#### split function.

```bash 
# The split() function breaks a string apart into a list based upon common 
# words/characters that appear in the original string
diarySplit = diaryText.split(" ")
```

#### find Function.

```bash
# The find() function will navigate through some text, determine whether or not the 
# string passed into it is contained within, and return the index of that string.
if diaryText.find("malarkey") > -1:
    print("Malarkey found!")
``` 

-------

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
