## Sysadmin Essentials: Monitoring Log Files 

--------

## Solutions for Using the logger to Create Log Messages 

------

## Using the logger to Create Log Messages

In this activity, you will create three short log messages using `logger`.  For each message **confirm** that the message was written to `/var/log/syslog`.

* First display and review the `man page` for `logger`.

    * `man logger`

* Create a simple message such as "This is a logging message".

    * `logger "This is a logging message from <your first name>."`

* Confirm that message is displayed in `var/log/syslog`.

    *  `grep -i <your firstname> /var/log/syslog`

* Create a simple message using a `tag`. Use **your name** as the tag and the text `"This is a test using a tag."`

    * `logger -t <name> 'This is a test using a tag'`

* Display a log message to `standard error` as well as the `/var/log/syslog`.

    * `logger -s "This message goes to the screen and a log file.`

* **Challenge**: Create a log message using the `-f` option.

    * `cat > testfile.txt`
    `My name is <your name>` 
    `I am in class tonight`
    `learning about logging`

    * `logger -f testfile.txt`


