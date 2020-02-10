## Warm-Up Activity: Investigating Locked Accounts using the Contingency Command

### Instructions

Welcome to the Warm-up Activity!  

In a previous exercise, your task was to monitor a web application that allowed customers to purchase your company's products. You are concerned that there is a threat of an attacker attempting to **brute force login** to your application. 

Your search discovered that the Windows event log showed **57 failed login** attempts occurred in one minute. Using this data, you developed a `baseline` and `threshold` for creating alerts for `failed login attempts` to the web application.  

Your next task is to investigate the **target of the activity** by looking at the `account names` and `account domains` for failed login attempts in the Windows event log.
In this activity, you will be introduced to a new SPL command that will help you with the investigation.
 
- The syntax for the command is: `contingency <field><field>` 

   - `contingency` is the Splunk command

   - `field` is a field in the event

  [Documentation](<https://docs.splunk.com/Documentation/Splunk/7.2.5/SearchReference/Contingency>) is available for the command at the Splunk website.

#### 1. Getting Started

* Log into Splunk using your `username` and `password`.

* Upload the `wineventlogs_baseline.csv` file into Splunk.

#### 2. Execute a search for locked accounts

* Write a SPL command that will search for locked accounts.

#### 3. Investigate the target of the activity

* Wite a `contingency search` command that will display the relationship between `account names` and `account domains`.  This will narrow down the targets for the failed login attempts.

   * Hint: `pipe` this command to your first command.

#### 4. Develop your conclusion

* Answer the following question:

   * Where was the attacker trying to gain access?

Great job.  Activity Complete!

#### Additional Challenge 

* Using the `access_30DAY.log` file, provide another example of when a `contingency table` can be used, such as **User agent and status** analysis.