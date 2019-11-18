## Scheduling Backups Using Cron

--------

## Instructions 

------

## Practice Writing Cron Jobs

In this activity, you will use a **text editor** and learn to write cron statements. This is a best practice because cron jobs run as soon as you put them in a cron table.

* Start by opening a terminal window on the Virtual Machine.

* Working in your `home` directory, launch the nano editor:  `nano firstcroncommands.txt`

* Enter the following cron jobs in the text file.


**Job 1:**

* Schedule an imaginary shell script `/scripts/backup.sh` to run `every 10 hours`.

* **Hint:** 

    * To get the cron syntax, review the cron syntax from the instructor's earlier `rsync` example.

**Job 2:**    

* Create a compressed `pictures.tar.gz` file of the `/home/pictures` directory. The job runs on Monday and Friday at 10 PM.

* **Hints:** 

    * **Hour** is the located in the second field 
    
    * **days_of_the_ week** can be specified using **mon** or **fri**.
    

**Job 3-Challenge:**

*  Schedule the jobs `/scripts/expenses.sh` and `/scripts/paidexpenses.sh` using one cron entry. The jobs run at 4 am and 5 pm on Tuesday.

* **Hints:** 

    * Use **`,`** to separate hours in the second field 
    
    * Use **`;`** to separate tasks in the sixth field.

* `Save` your text file.

* `Exit` the editor.
