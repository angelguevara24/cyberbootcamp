## Unit 4 Homework Assignment: Python Programming Continued


In this exercise, you are tasked with completing the following activities. Note, there are also two optional bonuses for additional challenge. 

* Creating 24 directories for each week of class, each containing three folders for each day of class.

* Copying files from `~/Downloads` into the current directory.

* **Bonus**: Adding the copy script to the PATH.

* **Bonus:** Adding an alias for the copy script to `~/.bashrc`.

---

## Part 1: Class Notes Folder

In the file called `create_notes_drs.py`, define and call a function called `main` that does the following:

* Creates a directory called `CyberSecurity-Notes` in the current working directory.

* Within the `CyberSecurity-Notes` directory, creates 24 sub-directories (sub-folders), called `Week 1`, `Week 2`, `Week 3`, and so on until up through `Week 24`.

* Within each week directory, create 3 sub-directories, called `Day 1`, `Day 2`, and `Day 3`

**Bonus Challenge**: Add a conditional statement to abort the script if the directory `CyberSecurity-Notes` already exists.

---

## Part 2: Copying Files from Downloads 

### Copying Student Exercises

So far, you've used a few different Python modules, but for the rest of the homework, you will need to familiarize yourself with a new one. 

- The `shutil` module is a Python module used for high-level file operations like moving and copying. 

- Read [this JournalDev documentation](https://www.journaldev.com/20536/python-shutil-module) beforehand to get familiar with `shutil` and make sure to use this [Python documentation](https://docs.python.org/3.5/library/shutil.html#module-shutil) while you're working through the homework. 

In the file called `copy_activities.py` with a function called `stu_activities` that does the following:

* Finds files in `~/Downloads` that contain the string `readme`.

* Copies these files into the current working directory.

**Note**: This isn't just a challenge to complete for the sake of it, this is a practical script you can run to move any downloaded files from class into your class notes directories, screenshots into a folder, or whatever you'd like it to be. You can alter the script after submitting your homework to make it work for whatever you'd like it to.


### Copying Class Files

Using the function `pptx_copy` in the file `copy_slides.py`,  create a script that does the following:

* Finds files in `~/Downloads` with the file extension `.pptx` or `.ppt`.

* Copies these files into the current working directory.

**Note**: This is another practical script you can use to move downloaded slides from class into your class notes directories.

---

## Bonuses: Updating PATH and Add an Alias

**Note**: Consider this a bonus activity. You are **not** required to complete this step for credit. However, these tools will come up in-class later, so you're strongly encouraged to study up now!

We've written the scripts, but they are only executable from their relative path - where the files are in your system. In this final step, we'll make them accessible to you anywhere in your system directory.

* First, read the [following article](http://linuxcommand.org/lc3_wss0020.php) to learn more about `.bashrc`, `PATH`, aliases, and the `export` command. Once you read it, answer the following questions:

    * What is the main difference between `~/.bashrc` and the `~/.bash_profile`?
    
    * What does the `export PATH` command do?
    
    * What is the benefit of creating aliases?

* Create a directory called `/usr/local/bin` and move your three scripts into this directory.

* Update `.bashrc` to add the directory `/usr/local/bin` to `PATH` with the following command:

    ```
    export PATH=$PATH:/usr/local/bin
    ```

* Finally create aliases in `.bashrc` for these three scripts:
    
    * `alias copy_activities="copy_activities.py"`
    
    * `alias copy_slides="copy_slides.py"`
    
    * `alias create_notes_drs="create_notes_drs.py"`

## Submission

Please submit `create_notes_drs.py`, `copy_slides.py`, and `copy_notes.py`.

