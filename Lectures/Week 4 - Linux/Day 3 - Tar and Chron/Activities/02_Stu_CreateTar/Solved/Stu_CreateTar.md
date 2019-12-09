## Sysadmin Essentials: Archiving Data using tar

--------

## Solutions for Creating a tar Archive

-------


In this activity, you will **create**  four `tar archives` using the `Projects/TarDocs` directory.  

- Open a terminal window on the Virtual Machine.

- Change to the `Projects` directory.

- Locate the `TarDocs` directory.

**Exercise 1:** Using the `tar` command:
    
- Create a `sample.tar` archive with four files: `file1.txt` `file2.txt` `file3.txt` and `file4.txt`.

    - `touch file1.txt file2.txt file3.txt file4.txt`

    - `tar cvfW sample.tar file1.txt file2.txt file3.txt file4.txt` 

- List the contents of the `sample.tar`.

    - `tar -tf sample.tar`


**Exercise 2:**
    
- Create a `multidir.tar` archive containing the `Pictures` and `Movies` directories.

  - `tar cvfW multidir.tar 'TarDocs/Pictures' 'TarDocs/Movies'`

- List the contents of the `multidir.tar`. 

  - `tar -tf multidir.tar`   

**Exercise 3:**
    
- Create a `mp4.tar` archive that contains ONLY the **.mp4** files `Projects/TarDocs` directory.

  - `tar cvfW mp4.tar $(find TarDocs -iname "*.mp4")`

- List the contents of the `mp4.tar`. 

  - `tar -tf mp4.tar`


**Exercise 4:**
    
- Create a `mytest.tar` archive that **excludes** the `Programs` directory in the `Projects/TarDocs` directory.

  - `tar cvfW mytest.tar --exclude="TarDocs/Programs" TarDocs/`

- List the contents of the `mytest.tar`.  

  - `tar tf mytest.tar` 

**Challenge:**

Using the `man page` for `tar` find the `--files-from = FILES` option.
    
- Use the `find` command to locate files that are greater than **5000K** in length in the `Programs` directory and output the list to `large-files.txt`.

  - `find . -size +5000 -print > large-files.txt`

- Create archive `largefiles.tar` using the `--files-from = FILES` option. 

  - `tar cvfW largefiles.tar --files-from=large-files.txt`

- List the contents of the `largefiles.tar`

  - `tar tf largefiles.tar`    

    - Why is this a good option to use?

      - `The process automatically places all files in the archive using the size of the files.  This could also be done using other criteria (name, timestamp, pattern).`
