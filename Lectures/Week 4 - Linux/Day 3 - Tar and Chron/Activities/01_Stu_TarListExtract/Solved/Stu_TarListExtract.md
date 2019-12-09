## Sysadmin Essentials: Archiving Data using tar

--------

## Solutions for Listing and Extracting the Contents of an Archive

-------

In this activity, you will **list**  and **extract** the contents of an archive using the `TarDoc.tar` file.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

    * `cd Projects`

* Locate the `TarDocs.tar` file.

    * `ls TarDocs.tar`

* **Exercise 1:** Using the `tar` command:

    * `List` the contents of `TarDocs.tar` using the `verbose` option.

        * `tar -tvf TarDocs.tar`

    * Produce a `short` listing of the contents of `TarDocs.tar`.

        * `tar -tf TarDocs.tar`


* **Exercise 2:** Practice `extracting (untar)` the archive into the `Projects` directory.

    * `untar` TarDocs.tar.

        * `tar -xvf TarDocs.tar`

    * List the contents of the extracted archive.

        * `ls -l TarDocs`
        * OR `tree TarDocs`

    * **How many directories** are in the archive?

        *  `4 Main directories. 520 total directories.`

    * View the directory structure  using `tree`.

        * `tree`


* **Exercise 3:** Next practice `extracting (untar)` two files from the archive.    

    * `untar` the files `ZOE_0003.mp4` `ZOE_0004.mp4` into a directory named `MyMovies` in the `Projects` directory. Extract the files *without* the directory structure.

        * `mkdir MyMovies`

        * `tar -xvf TarDocs.tar -C MyMovies/ --strip-components=2 "TarDocs/Movies/ZOE_0003.mp4" "TarDocs/Movies/ZOE_0004.mp4"`

    * `List` the contents of the  `MyMovies` directory.

        * `cd MyMovies`

        * `ls MyMovies`


* **Exercise 4:** Now practice `extracting (untar)` all the `pdf` files.    

    * `untar` all the `pdf` documents to a directory named `pdfDocuments` in the `Projects` directory.

        * `mkdir pdfDocuments`

        * `ls` to see the new directory

        * `tar -xvf TarDocs.tar -C pdfDocuments --wildcards "*.pdf"`

    * `List` the contents of the  `pdfDocuments` directory.

        * `ls pdfDocuments`
        
        * OR `tree pdfDocuments`
