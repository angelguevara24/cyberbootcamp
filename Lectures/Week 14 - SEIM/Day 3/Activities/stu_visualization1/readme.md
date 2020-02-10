#### Instructions

Welcome to the  Activity!  

Your team has prepared a **statistical report** for The Customer's digital forensics case. You started by investigating *firewall attack log* event data that was collected for several years.  Now, you are asked to create a **Radial Gauge** to measure a specific attack id over a one hour period.  Your SOC will use this to determine if the current levels of attacks based on this attack types.

In this activity, you will use the [fortinet_logs.csv](Resources/fortinet_logs.csv) file and create visual elements for these values.

* First, upload the [fortinet_logs.csv](Resources/fortinet_logs.csv) file into Splunk.

#### Create a visual using the following elements: 

**Radial Gauge**

* Create a **Radial Gauge** to monitor the the attack_id=10725 over a one hour period
* Set the ranges and colors to values you determine would be appropriate
* Save your Radial Gauge

    * Hint: Here is how to create a sinlge value:
    
       `| stats count as total`
       