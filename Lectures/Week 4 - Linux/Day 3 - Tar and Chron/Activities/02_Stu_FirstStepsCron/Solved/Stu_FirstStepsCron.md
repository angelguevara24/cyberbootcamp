## Scheduling Backups Using Cron

--------

## Solutions for Creating a Cron Table

-------

* Check to see if the `cron service` is running.

    * `service cron status`      

* Edit the `crontab file`.

    * `crontab -e`

    * Select the `nano` editor if needed.

* Next scroll down to the bottom of the file and add two cron jobs.

	* The first job will echo the text `Hello world` to the file `myhellojob.txt` `every two minutes`.

        * `*/2 * * * * echo "Hello World" >> myhellojob.txt`

	* The next job will echo the text `This is test` to the file `myhellojob.txt` `every two minutes`.

        * `*/2 * * * * echo "This is a test" >> myhellojob.txt`


* An alternative is to write this job as one statement.

    * `*/2 * * * * echo "Hello World" >> myhellojob.txt; echo "This is a test" >> myhellojob.txt`


* Wait 2 minutes and confirm that the jobs are writing text to the files.

    * `ls` myhellojob.txt

    * `cat` myhellojob.txt


* **IMPORTANT:**

	* Disable the jobs in the cron table after checking the output to the text file.

    * `#*/2 * * * * echo "Hello World" >> testing123.txt`

     * `#*/2 * * * * echo "This is a test" >> testing123.txt`

     or

    * `#*/2 * * * * echo "Hello World" >> myhellojob.txt; echo "This is a test" >> myhellojob.txt`
