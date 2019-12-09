## Sysadmin Essentials: Monitoring Log Files

--------

## Solutions to Introduction to Log Files

----

In this activity, you will view log messages from the **command line** and **graphically** using the `Log File Viewer`.


* View messages in `/var/log/syslog` in real time.  

    * `tail -f /var/log/syslog`

* View only `cron` log messages in `/var/log/syslog`.

    *  `grep -i CRON /var/log/syslog`

