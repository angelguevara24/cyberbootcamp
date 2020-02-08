## Solution File: Introduction to SPL

### Solutions


#### Part 1: Getting Started


1. What is an *event*?

    **Answer:** Events are a single record of activity or instance data that has been indexed by Splunk. For example, an event might be a single log entry in a log file.

2. What is a *source type*?

    **Answer:** Splunk assigns a *source type* to determine how to **format the event data** during the indexing process.

3. What is the most important search parameter to specify?

    **Answer:** `Time`

4. Identify what this search will do:

	```bash
		src="10.9.165.*" OR dst="10.9.165.8"
	```	

    **Answer**: Return events where the source IP addresses that start with `10.9.165.` or destination IP address is `10.9.165.8`.

#### Part 2: Investigation 

 
* The `field/value pairs`.

* **Answers:**

    - source="access_30DAY.log"

    - sourcetype="access_combined_wcookie"
    
    - status="505"

* The `Boolean operator`.

* **Answer:**

  - AND

* **Answer:**

    - source="access_30Day.log" sourcetype="access_combined_wcookie" AND status="505"



* Enter the resulting `search term` in the Search bar and execute the search.

#### Part 3: Narrowing down the search


* Start by specifying the following search term in the Search bar so that ALL events are displayed:

	```bash
		source="access_30Day.log" sourcetype="access_combined_wcookie"
	```	

1. Write the search term that will first display events for ALL *server response errors*

	**Answer:** This search term requires that students use a wildcard to specify the **5xx* family of HTTP server responses.

	```bash
	 source="access_30Day.log" sourcetype="access_combined_wcookie" AND status="5**"
	 ```

2. Next, narrow your search down to the *HTTP version not supported* events.

	**Answer:**

	```bash
	 source="access_30Day.log" sourcetype="access_combined_wcookie" AND status="505"
	 ```

3. Now, isolate the *highest client software* that is originating the response.

	**Answer:**  Use `Interesting Fields` and select the highest value from the `useragent` field.

	![Images/search-answer.png](Images/search-answer.png)

4. Number of Server 505 response events.

    **Answer:** 552

5.  Peak times vary.    


* Address any questions the students have before concluding class. 