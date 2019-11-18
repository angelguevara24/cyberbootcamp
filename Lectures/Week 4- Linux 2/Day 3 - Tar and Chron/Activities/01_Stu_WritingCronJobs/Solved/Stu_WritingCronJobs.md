## Scheduling Backups Using Cron

--------

## Solutions to Practice Writing Cron Jobs

------

**Job 1:**

* Schedule the shell script `/scripts/backup.sh` to run `every 10 hours`.

    `0 */10 * * * /scripts/backup.sh`

**Job 2:**    

* Create a compressed `pictures.tar.gz` file of the `/home/pictures` directory. The job runs on Monday and Friday at 10 PM.

    `0 22 * * mon,fri  tar -czf pictures.tar.gz $HOME/pictures`

**Job 3-Challenge:**

*  Schedule the jobs `/scripts/expenses.sh` and `/scripts/paidexpenses.sh` using one cron entry. The jobs run at 4 am and 5 pm on Tuesday.

    `0 4,17 * * tues /scripts/expenses.sh; /scripts/paidexpenses.sh`