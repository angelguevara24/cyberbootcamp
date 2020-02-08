## Working with Logs and Events Solution File

**Solutions:**

1. List two benefits of using SIEMS. Answers may vary:

    * *Increasing efficiency*: Organizations can use SIEMs to gather and monitor a large amount of logs in one place using a simple interface.

    * *Preventing potential security threats*: SIEMS monitor and alert on suspicious activity in the logs; organizations can get notified ahead of time of potential threats by reducing the **mean time to detect** (MTTD) and the **mean time to respond** (MTTR) to cyber threats.

    * *Reducing the impact of security breaches*: Review of logs will show certain areas of the network that may need additional security controls, which can be put in place to mitigate or even stop a breach.

    * *Reducing costs*: One central system is used to view, monitor, and alert. Organizations can reduce costs on hardware and software.

    * *Better reporting, log analysis, and retention*: One system collects all of the logs and makes it easier to generate reports and analyze logs.

    * *IT compliance*: The depth of visibility into the logs makes its possible for organizations to see if they remain compliant.


2. How are *logs* used in a SIEMS? 

    * SIEMS collect logs from different sources in real-time and security teams use the data to detect and respond to security incidents.

    * Log data is processed into events, which are used in analysis.

3. What is a baseline and how is it used in a SIEMS?

    * A baselines provide a measure of what is normal in a set of data in a SIEMS.  A baseline is calculated over a period of time so we can see how something operates normally.

**Part 2:**

* Here is the sample log entry:

    ```bash
    192.188.106.240 - - [06/Feb/2019:23:59:45] "GET http://www.buttercupgames.com/category.screen?
    categoryId=TEE&JSESSIONID=SD2SL4FF9ADFF4959 HTTP 1.1" 200 2958 
    ```

 **Answer** Field names and values. 

 - client_ip =  `192.188.106.240`

 - timestamp = `06/Feb/2019:23:59:45`

 - http_method = `GET`

 - http_url = `GET http://www.buttercupgames.com/category.screen?categoryId=TEE&JSESSIONID=SD2SL4FF9ADFF4959 HTTP 1.1`

- status = `200`

- bytes = `2958`


**Part 3:**

Write a pseudo-code statement(s) that checks if the GET request to the server was unsuccessful for the source IP address and date in our sample log entry.  Students should use the field names they developed in Part 2 in the answer to this question.

* Here is a suggested answer:

    ```bash
    
    *client_ip* is equal to `192.188.106.240`

    *AND* 

    **timestamp** is equal to `06/Feb/2019:23:59:45`

    *AND*

    **status**  does not equal `200`

    ```

 **Extra Challenge:** Send an alert if the count of unsuccessful GET responses are greater than 50 in one minute.

* Here is a suggested answer to the EXTRA CHALLENGE:

     ```bash
    
    store the count of unsuccessful responses in **count**

    if **count** is **greater than 50** 

    *AND* 
    
    **time** is **one minute**

    **send an alert** to the trouble ticket system

    ```
