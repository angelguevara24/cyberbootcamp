## Sysadmin Essentials: Archiving Data using tar

--------

## Instructions 

-------

## Creating a tar Archive

In this activity, you will **create**  four `tar archives` using the `Projects/TarDocs` directory.  

- Open a terminal window on the Virtual Machine.

- Change to the `Projects` directory.

- Locate the `TarDocs` directory.

**Exercise 1:** Using the `tar` command:
    
- Create the following four files: `file.txt` `file2.txt` `file3.txt` and `file4.txt`.

- Create a `sample.tar` archive with the four files you have just created. 

- List the contents of `sample.tar`.

**Exercise 2:**
    
- Create a `multidir.tar` archive containing the `Pictures` and `Movies` directories.

- List the contents of `multidir.tar`.    

**Exercise 3:**
    
- Create a `mp4.tar` archive that contains ONLY the **.mp4** files `Projects/TarDocs` directory.

- List the contents of `mp4.tar`.

**Exercise 4:**
    
- Create a `mytest.tar` archive that **excludes** the `Programs` directory in the `Projects/TarDocs` directory.

- List the contents of `mytest.tar`.  

**Challenge:**

Using the `man page` for `tar` find the `--files-from = FILES` option.
    
- Use the `find` command to locate files that are greater than **5000K** in length and output the list to `large-files.txt`.

- Create archive `largefiles.tar` using the `--files-from = FILES` option.

- List the contents of `largefiles.tar` 

- Why is this a good option to use?
