## Sysadmin Essentials: Archiving Data using tar

--------

## Solutions to How to Backup Data to Compressed Archives

-------


In this activity you will create a `gzip` and `bz2` archive of the `TarDocs/Programs` directory in a single command.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

**Exercise 1:**

* Create the `tardocs.tar.gz` archive using the `TarDocs/Programs` directory.

    * `tar czf tardocs.tar.gz TarDocs/Programs`

**Exercise 2:**

* Create the `tardocs.tar.bz2` archive using the `TarDocs/Programs` directory.

    * `tar cjf tardocs.tar.bz2 TarDocs/Programs`

**Exercise 3:**

* Compare the size of the `tardocs.tar.gz` and `tardocs.tar.bz2` archives.

    * `wc -c tardocs.tar.bz2`

    * `wc -c tardocs.tar.gz`

* Which archive is smaller?

    * The `tardocs.tar.bz2` is smaller.
