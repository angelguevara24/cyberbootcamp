## Day 1 - Sysadmin Essentials: Archiving Data using tar

### Overview

* This lesson is the first installment in Sysadmin Esssentials.  It will introduce students to archiving data using `tar`.  Students will learn how to `create`, `modify`, `search` and `extract` the contents of `tar` archives.

### Class Objectives

By the end of class, students will be able to:

* Create (`tar`) an archive.

* List and search the contents of an archive.

* Modify (`append`, `update`, `delete`) the contents of an archive.

* Extract (`untar)` the contents of an archive.

* Backup files and directories to `compressed archives`.


### Instructor Notes

* You start this session with an introduction to creating and managing archives with `tar`. Students will learn how to `create`, `list` `modify`, `search` and `extract` the contents of `tar` archives.

* Students should be comfortable using  `pipe`, `find`, `mkdir`, `touch` and `wc` commands.

* The session is structured to provide **short lectures** followed by demonstrations and guided practice activities. Demonstrations can be live or canned.

* The demonstration and activities use the `TarDocs.tar` file.   

    * The archive is located in the `/home/Projects` directory on the Instructor and Student Virtual Machine.   

    * The archive contains **documents**, **movies**, **pictures** and **programs** directories.

* The demonstrations also use **tree** to display directories using a tree structure.

* The **ClassResources/TarClass** directory on the Instructor VM contains ALL the files created in the demonstrations and activities.  Please see the Readme for a description of each file.    

* Try to stay on track of time, but always feel free to add a few extra minutes to the clock if students are struggling with an activity. As always, have your TAs refer to the `Time Tracker` to help you stay on track.

### 1. Direction Instruction: A Brief Introduction to the tar Command (0:15)

* Begin class by welcoming students back and giving them a preview of today's class.  Use the Daily Goals slide to discuss the learning objectives.

 * Tell students that today's class starts the sessions on how system administrators **archive**, **schedule** and **monitor** system data.

* Explain that in this session, we will learn  about basic **backup** and **recovery** procedures using the `tar` program. `tar` is also used for **archiving documents** and **distributing software**.

    * Point out: `tar` stands for **Tape Archive** and was first used to archive files to tape.  It is the most popular archiving tool used in Unix systems. It is similar to Winzip for Windows or iPack on the Mac.

* Explain that the `tar` program stores multiple files or directories in a single, highly compressed file called a `tarball`.

    * Explain that `data compression` reduces the **size** of files to save storage and allows for faster transfer over the network.

* Explain that backups are important to maintain compliance with regulations, ensure that systems can recover from cyberattacks and natural disasters.     

* Tell students that backups are normally done on one system and then the archives moved to another.  In these exercises we will do everything on one machine.

#### Getting Started

* Start by explaining the command syntax:

    * `tar [option(s)] [archive_name] [objects_to_archive]`

*  and some basic options so that students will be able to follow the next section.

    * `c` = create an archive

    * `v` = verbose

    * `f` = filename(s) to archive

    * `x` = extract contents

    * `t` = list contents

* Tell students that the `man tar` command is used to obtain information on all options.

    * Run: `man tar`

    * Tell students that there are a LOT of options and you will cover a few in this session.

* Before starting the demonstration, tell students that they may see the `tar` command written using three different **styles**.

    * Point out: You may see different styles written in books or on the web. This will not be confusing if you are familiar with the styles.

    * Let students know that you'll prefer the short style in class, but that they should use whichever they're most likely to remember.


* Describe that in the **traditional** style the options are a **cluster of letters**.

    * `tar cvf a.tar /etc`

    * This command will **create** an archive of the `/etc` directory.

* Point out that the **short** style prepends the `-` to the option that is used in most Unix commands.

    * `tar -xvf a.tar` or `tar -x -v -f a.tar`

    * This command will **extract** files and directories from the `a.tar` archive.

* Explain that the **long** style spells out the option name.

    * `tar --create --file --verbose a.tar /etc`

    * This command will **create** an archive of the `/etc` directory.

* Let students know that today's class will introduce them to the major features of tar through a series of exercises on:
  - Listing and extracting the contents of existing tarballs
  - Creating your own tar archives
  - Updating an existing archive
  - Compressing tarballs to save space

### 2. Direct Instruction: Listing and Extracting the Contents of an Archive (0:20)

You'll start by having students work with an **existing archive**. They will learn how to `list` and `extract` files and directories.  

* Demonstrate how to **list the contents** of an archive.

    * Point out: Listing the contents of the archive does not **write the content to disk**.

* Open a terminal window on the Virtual Machine and show the `tar file` in the `Projects` directory.

    * Run: `cd Projects`

    * Run `ls -l TarDocs.tar`

    * Point out that `tar files` have the extension `.tar`

    ![Images/tar-ls-l.png](Images/tar-ls-l.png)

* List the contents of the `TarDocs.tar` showing the file permissions, size and date/time information.   

    * `t` (list), `v` (verbose) and `f` (filename).

    * Point out that this command uses the **traditional** format.

    * Run: `clear`

    * Run: `tar tvf TarDocs.tar | less`

    ![Images/tar-listing.png](Images/tar-listing.png)

* Now show the contents of the archive without the `verbose` option. The file specs are not shown using this option.

* Tell students this is a `short` listing.

    * Run: `clear`

    * `tar -tf TarDocs.tar | less`

    ![Images/tar-listing-short.png](Images/tar-listing-short.png)    

* Stop and see if there are any questions on listing the contents of an archive.


#### Extracting Data from the tar Archive  

While the `t` option shows the contents of an archive, the `x` option (`untar`) **extracts** the specified files or directories from the backup and writes them to disk.

* In the next demonstration show students how to  **untar the contents** of our archive.

    * Point out: **Individual files** or **entire directories** can be extracted and are written to disk.

* Run: `tar -xvf TarDocs.tar | less`.

    * `x` (extract) ,  `v` (verbose), `f` (filename).

    * Point out that this command uses the **short** (`-`) format.

    ![Images/tar-extract.png](Images/tar-extract.png)

* Explain that the original directory structure is retained in the archive and now can be seen on disk.

    * Run: `clear`

    * Run: `ls -l TarDocs`

    ![Images/tar-Docs-directory.png](Images/tar-Docs-directory.png)


* Now run `tree` to graphically see the `Projects/TarDocs` directory structure.  

* Change to the `Projects/TarDocs` directory.

    * Run: `clear`

    * Run: `tree`

    ![Images/tar-tree.png](Images/tar-tree.png)    

* Demonstrate displaying the `Movies` directory of the archive.  This is useful to quickly find files in subdirectories of the archive.

    * Run: `tree -a ./Movies` to see the structure.

    ![Images/tar-tree-movies.png](Images/tar-tree-movies.png)

* Stop and see if there are any questions on extracting an archive.  

#### Extracting Groups of Files from an Archive

Start by telling students that sometimes they may need to extract a subset of an archive.

* Demonstrate extracting `one file` from the directory.

    * `tar -xvf TarDocs.tar "TarDocs/Documents/Design-Patterns/DesignPattern.pdf"`

* Demonstrate extracting ONLY the `*.jpg` files. Place the files in a `jpgPictures` directory in the `Projects` directory.

    * Point out:  This command will use the `--wildcards` option to extract the `*.jpg` files and `-C` option to place the extracted files in the `Projects/jpgPictures` directory.

* In the `Projects` directory:

    * Run: `clear`

    * Run: `mkdir jpgPictures`

    * Run: `ls` to see the new directory

    * Run: `tar -xvf TarDocs.tar -C jpgPictures --wildcards "*.jpg"`

    * Run: `cd jpgPictures`

    * Use `tree` to list the contents of the `jpgPictures` directory showing the jpg files.

    ![Images/tar-jpg-Pictures.png](Images/tar-jpg-Pictures.png)


### 3. Guided Practice: Listing and Untaring an Archive (0:20)
In this activity, students will **list**  and **extract** the contents of an archive.  Students use the `TarDocs.tar` file located in their `home/Projects` directory.

* Send students the following instructions over Slack.

* **File:** The [TarListExtract.md](Activities/Stu_TarListExtract/Unsolved/Stu_TarListExtract.md) file.

**Instructions**

In this activity, you will **list**  and **extract** the contents of an archive using the `TarDoc.tar` file.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

* Locate the `TarDocs.tar` file.

* **Exercise 1:** Using the `tar` command:

    * `List` the contents of `TarDocs.tar` using the `verbose` option.

    * Produce a `short` listing of the contents of `TarDocs.tar`.

* **Exercise 2:** Practice `extracting (untar)` the archive into the `Projects` directory.

    * `untar` TarDocs.tar.  

    * List the contents of the extracted archive.

    * **How many directories** are in the archive?

    * View the directory structure  using `tree`.


* **Exercise 3:** Next practice `extracting (untar)` two files from the archive.    

    * `untar` the files `ZOE_0003.mp4` `ZOE_0004.mp4` into directory `MyMovies` in the `Projects` directory. Extract the files *without* the directory structure.

    * **Hint:** Don't forget to create the `MyMovies` directory first.

    * `List` the contents of the `MyMovies` directory.


* **Exercise 4:** Now practice `extracting (untar)` all the `pdf` files.    

    * `untar` all the `pdf` documents to the `pdfDocuments` directory in the `Projects` directory.

    * `List` the contents of the  `pdfDocuments` directory.   


### 4. Direct Instruction: Review of Listing and Untaring an Archive (0:10)

* Review the Guided Practice using the [TarListExtract.md](Activities/Stu_TarListExtract/Solved/Stu_TarListExtract.md) solution file.

* Emphasize `tar` keeps the directory structure which can be replicated on a remote system.

* Point out that `files`, `directories` or `subdirectories` can be extracted from a `tar` archive.

* Answer any questions students may have.


### 5. Direct Instruction: Creating a tar Archive (0:15)

Now that students have worked with an existing archive, it's time for them to create a new archive.

* Start by telling students that the `c` option creates a **new archive**.  

* Explain that it is a best practice to **verify** the archive after writing it using the `W` option.

#### Adding Files and Directories

* Explain that you will create a `sample.tar` archive with **three files**.

    * Run: `touch file1.sh file2.sh file3.sh`

    * Run: `tar -cvfW sample.tar file1.sh file2.sh file3.sh`

    ![Images/tar-create-verify.png](Images/tar-create-verify.png)

    * Run: `tar tf sample.tar` to display the archive.

* Explain that you will create an archive containing a `single directory` and `multiple directories.`

    * Run: `clear`

    * Demonstrate adding a single directory.

    * Run: `tar cvfW single.tar TarDocs/Pictures`

    * Run: `ls single.tar`

* Demonstrate adding two directories.

    * Run: `tar cvfW multi.tar 'TarDocs/Pictures' 'TarDocs/Documents'`

* Now demonstrate how to use the `find` command to create an archive that contains ONLY the `xml` files in the `Projects/TarDocs` directory.

    * Run: `clear`

    * Run: `tar  cvfW xmlfiles.tar $(find TarDocs -iname "*.xml"`)

    * Run: `tar -tf xmlfiles.tar` to display the archive.

   ![Images/tar-w-find.png](Images/tar-w-find.png)


#### Excluding Directories

* Next demonstrate how to create a `tar` archive **excluding** a directory in the `Projects/TarDocs` directory.  

    * Tell students you will exclude the `Programs` directory in the `TarDocs` directory using the `--exclude [pattern]` option.  This example uses the **long** format.

    * Run: `clear`

    * Run: `tar cvfW mytest.tar --exclude="TarDocs/Programs" TarDocs/`

    * Run: `tar tf mytest.tar` to display the archive.

    ![Images/tar-exclude.png](Images/tar-exclude.png)

* Stop and see if there are any questions.    


### 6. Guided Practice: Creating a tar Archive (0:20)

In this activity, students will practice **creating** four archives.  Students use the `Projects/TarDocs` directory.

* Send students the following instructions over Slack.

* **File:** The [CreateTar.md](Activities/Stu_CreateTar/Unsolved/Stu_CreateTar.md) file.

**Instructions**

In this activity, you will **create**  four `tar archives` using the `Projects/TarDocs` directory.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

* Locate the `TarDocs` directory.

**Exercise 1:** Using the `tar` command:

* Create a `sample.tar` archive with four files: `file1.txt` `file2.txt` `file3.txt` and `file4.txt`.

* List the contents of `sample.tar`.

**Exercise 2:**

* Create a `multidir.tar` archive containing the `Pictures` and `Movies` directories.

* List the contents of `multidir.tar`.    

**Exercise 3:**

* Create a `mp4.tar` archive that contains ONLY the **.mp4** files in the `Projects/TarDocs` directory.

* List the contents of `mp4.tar`.

**Exercise 4:**

* Create a `mytest.tar` archive that **excludes** the `Programs` directory in the `Projects/TarDocs` directory.

* List the contents of `mytest.tar`.  

**Challenge:**

 * Using the `man page` for `tar` find the `--files-from = FILES` option.

* Use the `find` command to locate files that are greater than **5000K** in length in the `Programs` directory and output the list to `large-files.txt`.

* Create archive `largefiles.tar` using the `--files-from = FILES` option.

* List the contents of `largefiles.tar`.

* Why is this a good option to use?


### 7. Direct Instruction: Review of Creating a tar Archive (0:15)

* Review the Guided Practice using the [CreateTar.md](Activities/Stu_CreateTar/Solved/Stu_CreateTar.md) solution file.

* Emphasize the `W` option verifies the contents of the archive after it is written. This is important to ensure the integrity of the backup.   

* Point out that Unix commands such as `find` can be used with `tar` to filter the contents of an archive.

* Review the **Challenge** exercise.

* Answer any questions students may have.

---
### BREAK (0:15)
---

### 11. Direct Instruction: Backup Data to Compressed Archives (0:15)

In this section you show students how to create **compressed archives**.

* Explain that `tar` archives can become very large so it's a good practice to compress them.  

    * Point out: Data compression makes the file smaller to store and faster to transfer over a network.  This is extremely important to maintain system availability.

* Emphasize that `tar` **does NOT compress** files. However, there are *tools* that can compress an archive.

* Explain that two widely used compression tools are `gzip` and `bzip2`.  

* Now demonstrate creating an archive and compressing it in a **single command**.

#### Compression Demo
* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

* Create an archive and compress it using `gzip`.  

    * Explain that this command uses the `z` option.

    * Point out: The resulting `tar file` will have the extension `.gz`

    * Run: `tar czf tardocs.tar.gz TarDocs/Documents`


* Next, create an archive and compress it using `bzip2`.

    * Explain that this command uses the `j` option.   

    * Point out: The resulting `tar file` will have the extension `.bz2`

    * Run: `tar cjf tardocs.tar.bz2 TarDocs/Documents`.

* Get the size of each archive for comparison.

    * Run: `wc -c tardocs.tar.bz2`

    * Run: `wc -c tardocs.tar.gz`

* Explain that bz2 usually offers better compression than gzip, but gzip is faster.

* Stop and see if there are any questions before the Guided Practice.

### 12. Guided Practice: How to Backup Data to Compressed Archives (0:15)

In this activity, students will practice **creating** `gzip` and `bz2` archives.  

* Send students the following instructions over Slack.

* **File:** The [CreateGzBz2.md](Activities/Stu_GzB2/Unsolved/Stu_GzB2.md) file.

In this activity you will create a `gzip` and `bz2` archive of the `TarDocs/Programs` directory in a single command.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

**Exercise 1:**

* Create the `tardocs.tar.gz` archive using the `TarDocs/Programs` directory.

**Exercise 2:**

* Create the `tardocs.tar.bz2` archive using the `TarDocs/Programs` directory.

**Exercise 3:**

* Compare the size of the `tardocs.tar.gz` and `tardocs.tar.bz2` archives.

* Which archive is smaller?


### 13. Direct Instruction: Review of Backup Data to Compressed Archives (0:10)

* Review the Guided Practice using the [CreateGzBz2.md](Activities/Stu_GzB2/Solved/Stu_GzB2.md) solution file.

* Point out that compression decreases the size of an archive to allow for faster transmission and less storage.

* Poll students to see which archive was smaller.

* Answer any questions students may have.


### 14.Direct Instruction: Review of Lesson and End Session (0:10)

* Congratulate students!  This was a challenging session.

* Reiterate that backups are important to maintain compliance with regulations, ensure that systems can recover from cyberattacks and natural disasters.

* As part of the homework assignment, students will research how to use `--listed-incremental` option with `tar`. This option produces `snapshot files` that  determine which files have been changed, added or deleted since the last backup.

* Give a high level overview of how **incremental backups** are used.

    * A **full** backup is made on Sunday then on Monday **all changes** are archived, and on Tuesday **all changes** are archived ...

    * If the system fails on Wednesday you would restore the backups from the Sunday, Monday and Tuesday archives.   

* Tell students that in the next session they will learn how to `schedule` backups.

-------

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
