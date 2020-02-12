## Solution Guide: Investigating Locked Accounts using the Contingency Command

### Solutions:

#### 1. Getting Started

* Log into Splunk using your `username` and `password`.

* Upload the `wineventlogs_baseline.csv` file into Splunk. 

#### 2. Execute a search for failed logins

* Next, write a SPL command that will search for `failed logins`.

  - Solution: There are many ways to complete this, one of the easiest would be `source="wineventlogs_baseline.csv" locked`. 

#### 3. Investigate the target for the activity

* Now write a `contingency search` command that will display the relationship between `account names` and `account domains`.  This will narrow down the targets for the failed login attempts.

  - Solution: `source="wineventlogs_baseline.csv" host="splunk-VirtualBox" sourcetype="csv" "locked" | contingency Account_Name Account_Domain`

![Images/contingency-locked-account.png](Images/contingency-locked-account.png)

 #### 4. Answer the following question  

* Where was the attacker trying to gain access?
  - Solution: The attacker was using `user_f` and `Domain_E` which showed `57 locked` events.

#### Challenge Question

* Using the `access_30DAY.log` file, give another example of where a contingency table can be used such as User agent and status analysis.

  - Solution: `source="access_30DAY.log sourcetype="access_combined_wcookie" | contingency useragent status`

![Images/contingency.png](Images/contingency.png)

