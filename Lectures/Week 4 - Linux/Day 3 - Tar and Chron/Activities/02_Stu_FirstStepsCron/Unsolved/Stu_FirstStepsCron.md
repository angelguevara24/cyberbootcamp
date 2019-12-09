## Scheduling Backups Using Cron

--------

## Instructions 

------

## Create a Cron Table

In this activity, you will create a **new crontab table** and **add two entries**.

* Start by opening a terminal window on the VM.
    
* Check to see if the `cron service` is running.

* Edit the `crontab file`.

* Select the `nano` editor if the file is being created.

* Scroll down to the bottom of the file and add two cron jobs.

	* The first job will echo the text `Hello world` to the file `myhellojob.txt` `every two minutes`. 
	
	* The next job will echo the text `This is test` to the file `myhellojob.txt` `every two minutes`.
 

* Wait two minutes and confirm that the jobs are writing text to the file.

* **IMPORTANT:** 

	* Disable the jobs in the cron table after checking the output to the text file.