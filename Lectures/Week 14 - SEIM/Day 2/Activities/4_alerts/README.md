## SIEMs Day 2: Guided Practice - Using Alerts to Monitor System Files
--------

### Instructions

In this Guided Practice you will create a search that monitors errors in the internal Splunk log at `/opt/splunk/var/log/splunk/splunkd.log` and create an alert.

#### Getting Started

1. Set Splunk to monitor the file `/opt/splunk/var/log/splunk/splunkd.log`

2. Save the host as `splunk-alerts`. 

3. Enter the following search in the Search window:

    ```bash
    host=splunk-alerts action=login status=failure
    ```
    
    * Set the Search Period to `All Time`.

    * Click the search icon to run the search.
    
4. Set the Search Period to `All Time`.

5. Click the search icon to run the search.

#### Saving as Alert

Now save the search as an alert.

1. Select `Alert` from the `Save As` drop down list. 

2. Use the following values to populate the fields:

    * `Title` as **Error log from splunkd.log**

    *  `Permissions` as **Shared in App**

    *  `Alert type` as **Real-time**

    * `Trigger alert when` as **Per Result**

    * `Add Action` as **Add to Triggered Alerts**  and select **Info** 

3. Click **Save**.  


 #### Triggering a Failed Login Attempt Alert

Trigger a failed login attempt by logging into Splunk with an incorrect username and password (twice).   

#### View the Alerts in the Triggered Alert List

1. View alerts from the **Alert Menu**.

2. View alerts from the **Activity** drop down list.
