## SIEMs Day 2: Guided Practice - Using Pipes with Splunk
--------

## Instructions

Welcome! In this Guided Practice you will practice using **pipes** in Slunk.

* You will work with the following file:

    * source = `alert_json_000015.log`. This file contains Snort alerts in  json formatted.

**Getting Started**

* Start by uploading the SNORT `alert_json_000015.log` file into Splunk.

* It is IMPORTANT to select **Structured** = **json_no_timestamp** for the `source type`.

* Continue with the file upload.

* When the upload is finished, review the **Interesting Fields** to determine what Snort `fields` can be used in the investigation.

* Scroll down and review the raw event data.  Do you recognize some of the fields?

#### The Investigations

You will create searches for two investigations. As you work through each search think about the following:

  * What fields are required in the search?

  * What operators are required in the search (e.g., AND, OR, =)?

  * What pipelines are used in the search?

* Remember that all results are located in the *Statistics* tab.  

* Hint: Use the Matching Fields area for help with entering field names and the How to Search area for help correcting errors.

#### Question 1:

You are asked to investigate a number of **TCP** alerts.

* Create a search that will find all alerts for TCP traffic. Display results for the top `destination ap addresses`. 

* Write out your search command. Then click on `Statistics`

* How many search results were returned from the `top` command?

* Look at the `Interesting Fields` down on the protocols, `prot` for short.  What were the top three scans that were performed?

Now, narrow **this search** so that it includes all the `TCP` traffic for the `top five` source IP addresses. Show **ONLY the number** of search results.

  * This search command uses the **logical AND operator** and **two pipes**.

* Write out your search command. Then click on `Statistics`

* `View the events` for the first IP address.  


#### Question 2:

Next, create a search that lists the destination AP in decending order. There is a **NEW SPL command** that is used in this search - `sort`.

  * Hint: The `sort` command is located in **Search Commands** in the Search Manual https://docs.splunk.com/Documentation/Splunk/7.2.4/SearchReference/WhatsInThisManual


#### Question 3:

Answer/Fill in the blank for the questions below:

- Limiting search by (blank) is key to faster results and is a best practice 
- The three main search modes?
- (Blank) mode has discovery off for event searches. No event or field data for stats searches.
- (Blank) mode has all events and field data; switches to this mode after visualization.
- (Blank) mode (default-based on search string data) has field discovery ON for event searches. No event or field data for stats searches.
- List the three booleans
- When searching for exact phrases you need to use (Blank)
- (Blank) fields that appear by default are host, sourcetype, source

Having only the choices of `inclusion` and `exclusion` fill in the following:
- (Blank) is better than (Blank)

* Congratulations...Activity Complete!  
