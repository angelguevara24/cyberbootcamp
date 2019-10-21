# Day 1 Cheat Sheet - Unit-Terminal

## Key Terms

- **Command**: A command is an instruction that tells a computer to do something (e.g., run a program).
  - **Example**: The command `mkdir MySubFolder` will run the `mkdir` program and create a directory called `MySubFolder`.

- **Command line interface**: The program that takes commands typed from the keyboard and passes them to an operating system for processing. On some operating systems this is also known as the `shell`.
  - **Example**: The Bash (Born Again SHell) command line interface is used most often on Unix and Mac OSX systems.

- **Graphical User Interface**: A graphical user interface or GUI is an interface that contains elements such as icons, buttons, sliders, or windows. A mouse or a touch screen is used to select and activate GUI elements.
    - **Example**: Cell phones contain a GUI that has a touch screen to interact with elements.

- **Terminal**: A terminal appears as an "all text window" in a GUI and is the interface to the command line interpreter for text input/output. By default, all output is displayed in the terminal window. The terminal window is known as `standard output`.
  - **Example**:  The terminal in the Windows operating system is displayed using "Command Prompt."  

- **Redirection**: By default, all the commands that are typed using the keyboard (called `standard input`) into a terminal window appear in this window.  There may be times when you want to redirect the output to something else (e.g., a file, another program). The redirect operator (`>`) or the pipe operator (`|`) can be used to perform redirection.
  - **Example**: 
    - To see the output from the `ls` command in the terminal window use:
        `ls`
    - To redirect the output from the `ls` command to a file use:
        `ls > listing.txt`

- **tee**: Allows for redirecting standard input to standard output.
    - **Example**: In this example the output from the `ls` command is redirected to the file parts.txt.  `ls | tee parts.txt`

- **File**: A file is a document that stores information such as text, images or video.  Files have a name and an extension.
  - **Example**: `MyBestPicture.jpg` is a file that contains an image. The `file name` is "MyBestPicture" and the `.jpg` extension says it is an image.

- **Directory**:  A directory is a file that stores the names of other files or directories in a hierarchical structure.
  - **Example**: The directory `pictures` is located in the directory `home` in `home/joe/pictures/`. 

- **Slash**:  The slash character (/) is the directory separator.
    - **Example**:  `/home/joe/pictures/`

- **Directory Tree**:  A directory tree is represented as an "inverted tree" with a series of directories branching off from a single directory.  It consists of a top-level directory with other directories (branches) below it.
    - **Example**: `/home/joe/pictures/` where `/home` is the root of the tree.

- **Root Directory**: This is the "top of a tree" from which other directories branch and contains all the other directories.
    - **Example**: The root directory is represented by a `/` (forward slash).

- **Subdirectory**: A directory that is located within another directory.
    - **Example**: The `pictures` directory is a subdirectory of directory `joe` in `/home/joe/pictures`.

- **Parent Directory**: The parent directory is the directory in which a subdirectory lies.
    - **Example**: The `pictures` directory is the parent of directory `vacation` in `/home/joe/pictures/vacation`.

- **Home Directory**:   The first directory a user enters when first logging into the system. It contains the user's files, directories, and programs. 
    - **Example**: If your account name is `joe` then your home directory is `/home/joe`.

- **Tilde**:  The tilde character (~) is used to represent a user's home directory.
    - **Example**: The `~` character in `~/pictures/MyBestPicture.jpg` represents the directory `/home/joe/`. 

- **Current Working Directory**: This is the directory in which a user is currently operating while using a command line interface. It can be displayed using the `pwd` (present working directory) command.
  - **Example**: If you are working in `/home/joe/pictures` and execute `pwd`, the text "/home/joe/pictures" is displayed in the terminal window.

- **Dot**: The dot (.) character refers to the current working directory.
  - **Example**: To change the current working directory from `/home/joe` to `/home/joe/pictures` run:
        `cd ./pictures`

- **Dot Dot**: The ".." characters refer to parent of the current working directory.
  - **Example**: To change to the parent directory of a current working directory run:
  `cd ..`

- **Pathname**: A pathname is a route taken to get to a directory in the tree.
  - **Example**: Pathnames are specified as absolute or relative.  See the discussion below.

- **Absolute Pathname**: An absolute pathname begins with the root directory and navigates the directory tree branch by branch.  
  - **Example**:  The absolute pathname `/home/joe/pictures/journal.jpg` refers to file `journal.jpg` that is located in directory `pictures` which is a subdirectory of `joe` which in turn is a subdirectory of `home` which is located in the `root` directory. 

- **Relative Path**: A relative pathname is the location of a file relative to the current working directory. You do not specify the `/` (forward slash) character.
  - **Example**: To display a file called `loop.txt` in a subdirectory called `doc` that is located in the current directory run: 
    `cat doc/loop.txt`

----- 

## Key Commands

## Basic Directory Navigation and Manipulation Commands

### cd Command

```bash
cd {directory}
```

#### Change to the root directory 

```bash
joe@joe:$ cd /
joe@joe:/$
```

#### Change to your home directory 

To change to `/home/joe`

```bash
joe@joe~/pictures:$ cd 
joe@joe:$ 
``` 
or 

```bash
joe@joe~/pictures:$ cd ~
joe@joe~/:$ 
```

#### Change to a working directory 

To change to the directory `/home/joe/pictures` 

```bash
joe@joe:$ cd pictures/
joe@joe~/pictures:$ 
```

#### Change to the parent directory of the current working directory 
    
To change from the subdirectory `/home/joe/pictures` to the parent directory `/home/joe` 

```bash
joe@joe~/pictures:$ cd ../
joe@joe:$
```
To change from the subdirectory `/home/joe/pictures/vacation` to the parent directory `/home/joe`

```bash
joe@joe~/pictures/vacation:$ cd ../../
joe@joe:$
```

#### Return to the previous working directory

```bash
joe@joe:$ cd pictures
joe@joe~/pictures:$ cd -
/home/joe
```

#### Change to a directory using an absolute pathname

```bash
joe@joe:$ cd ~/pictures/vacation
joe@joe~/pictures/vacation:$
```

#### Change to a directory using a relative pathname

```bash
joe@joe:$ cd pictures
joe@joe~/pictures:$
```

### ls Command

#### Display instructions for the ls command

```bash
joe@joe:$ man ls
```

#### List the Contents of a Directory

To list the contents of the `pictures` directory:

```bash
joe@joe:$ cd /home/joe/pictures
joe@joe:$ ls
MyBestPicture.jpg
```
### mkdir Command

#### Display instructions for the mkdir command

```bash
joe@joe:$ man mkdir
```
To make a directory `vacation` in the `/home/joe/pictures` directory:

- start in the parent directory 
- use the `mkdir` to create the `vacation` directory
- use `ls` to see the `vacation` directory
- `cd` to the `vacation` directory

```bash
joe@joe:$ cd ~/pictures
joe@joe~/pictures:$ `mkdir vacation`
joe@joe~/pictures:$ `ls`
vacation
joe@joe~/pictures:$ cd vacation
joe@joe~/pictures/vacation:$ 
```

## Basic File Manipulation Commands

### touch Command

#### Display instructions for the touch command

```bash
joe@joe:$ man touch
```

#### Using touch to create new and empty files

To create three new empty files named `Mylist1.txt`, `Mylist2.txt` and `Mylist3.txt` in the directory `home/joe`

```bash
joe@joe:$ touch Mylist1.txt Mylist2.xt Mylist3.text
joe@joe:$ ls
Mylist1.txt Mylist2.txt Mylist3.txt
```

### cat Command

#### Display instructions for the cat command

```bash
joe@joe:$ man cat
```

#### Using cat to write text to a file

The `>` operator is used for output redirection.  The cat command can uses the `>` operator to write lines of text to a file. 

To write lines of text to the file `MyShoppingList.txt` in the directory `home/joe`:

```bash
joe@joe:$ touch MyShoppingList.txt
joe@joe:$ cat > MyShoppingList.txt
My List:
cheese
bread
milk
```
Exit entering lines by simultaneously pressing the `CONTROL` and `d` keys

#### Using cat to display the contents of a file

To display the contents of `MyShoppingList.txt` in the directory `home/joe` to the terminal window screen:

```bash
joe@joe:$ cat MyShoppingList.txt
My List:
cheese
bread
milk
```
#### Using cat to display the contents of a large file using the less program

`cat` can be used to display the contents of a large file one screen at a time.  This command uses the `|` (pipe operator) which can send data to the `less` program.

The `less` program adjusts output to the width and height of the terminal window.  Use the `space bar` to advance to the next screen and the `b` key to go back.

```bash
joe@joe:$ cat MyShoppingList.txt | less
My List:
cheese
bread
milk
.
.
.
```

#### Using cat to replace the contents of a file

Use the `cat` command with the "output redirection operator" (`>`). The output from this command is written to the file, NOT to the screen.

Example:
- MyList1.txt contains `apple ball cat`
- MyList2.txt contains `kitchen penny table`

```bash
joe@joe:$ cat MyList1.txt > MyList2.txt
joe@joe:$ cat MyList2.txt
apple ball cat
```

#### Using cat to add more content to an existing file from another file

Use the `cat` command with the `>>`operator. The output from this command appends text from the first file to the file after the `>>` operator. The output is NOT displayed to the screen.

Example:
- MyList1.txt contains `apple, ball, cat`
- MyList2.txt contains `kitchen, penny, table`

```bash
joe@joe:$ cat MyList1.txt >> MyList2.txt 
joe@joe:$ cat MyList2.txt
apple ball cat 
kitchen penny table
```

### cp Command

#### Display instructions for the cp command

```bash
joe@joe:$ man cp
```

#### Using cp to copy a file from one directory to another directory

`cp` file-from-directory file-to-directory

NOTE: The file will still reside in the from-directory.

To copy the file `MyBestPicture.jpg` from `home/joe/pictures` into the `/home/joe/pictures/vacation` directory:

```bash
joe@joe~/pictures:$ cp MyBestPicture.jpg  ./vacation
joe@joe~/pictures:$ ls
MyBestPicture.jpg 
joe@joe~/pictures:$ cd vacation
joe@joe~/pictures/vacation:$ ls
MyBestPicture.jpg 
```

### mv Command

#### Display instructions for the mv command

```bash
joe@joe:$ man mv
```

#### Move a file from one directory to another directory

`mv` file-from-directory file-to-directory.

NOTE: The file will no longer resides in the from-directory.

To move the file `MyList1.txt` from `home/joe/pictures` in the `/home/joe/pictures/vacation` directory:

```bash
joe@joe~/pictures:$ mv MyBestPicture.jpg  ./vacation
joe@joe~/pictures:$ ls

joe@joe~/pictures:$ cd vacation
joe@joe~/pictures/vacation:$ ls
MyBestPicture.jpg
```

### tee Command

#### Display instructions for the tee command

```bash
joe@joe: man tee
```
#### Using tee to capture output from the ls command

Use `tee` to capture output from the `ls` command to a file named pipe.txt

```bash
joe@joe:$ ls | tee pipe.txt
```

### head Command

#### Display instructions for the head command

```bash
joe@joe:$ man head
```
#### Using head to display the first ten lines in a file

```bash
joe@joe:$ head MyList2.txt
```

### tail Command

#### Display instructions for the tail command

```bash
joe@joe:$ man tail
```
#### Using tail to display the last ten lines in a file

```bash
joe@joe:$ tail MyList2.txt
```
