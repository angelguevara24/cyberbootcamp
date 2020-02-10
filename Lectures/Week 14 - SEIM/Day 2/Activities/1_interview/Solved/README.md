## SIEMs Day 2: Guided Practice - Warm-Up Exercise
--------

## Solution

-------


Splunk Web Interface Searches for Web Performance and Threat Detection

####  Why: Checking web site performance issues.

1. `host=quiz sourcetype=access_* AND (status=500 OR status=404)`

    This search monitors for **servers internal errors** or **pages not found errors** on all servers.

    ![Images/1.png](Images/1.png)  

#### Why: Investigating possible password cracking.

2. `host=quiz source=*mailsv/secure.log failed password`

    This search looks for password attempts on the mail server host in the **secure.log** file .

    ![Images/2.png](Images/2.png) 

#### Why: Tracking down specific information for requests made to the buttercupgames site.

3. `host=quiz source=*www1* useragent=*`

    This search can be used to analyze a request header.  The User-agent Header contains the application type, operating system, software vendor or software version of the requesting software user agent. We are conducting the investigation on all www hosts.

    ![Images/3.png](Images/3.png)


#### Why: Investigating possible credit card fraud.

4. `host=quiz "?msg=Credit*" AND file="error.do" AND host!=www2`

    This search return the purchase date, purchase item id, user agent and client IP address for transactions on all hosts except www2.

    ![Images/4.png](Images/4.png)


5. Sample Event Fields and Values returned from the Credit Card Search.

    ![Images/interview-question_event.png](Images/interview-question_event.png)
