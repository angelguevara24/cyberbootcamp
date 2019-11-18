## Sysadmin Essentials: Monitoring Log Files 

--------

## Instructions 

-------

## Using the logger to Create Log Messages

In this activity, you will create four short log messages using `logger`.  For each message confirm that the message was written to `/var/log/syslog`.

* Working in your home directory launch a Terminal Window.

* First display and review the `man page` for `logger`.

* Create a simple message such as "This is a logging message from <your first name>".

* Create a simple message using a `tag`. Use **your name** as the tag and the text `"This is a test using a tag."`

* Display  the log message `This message goes to the screen and a log file` to `standard error` as well as the `/var/log/syslog`.

* **Challenge**: Create a log message that contains the following lines using the `-f` option:
    `My name is <your name>` 
    `I am in class tonight`
    `learning about logging`