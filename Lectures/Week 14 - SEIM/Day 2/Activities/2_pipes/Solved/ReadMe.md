## SIEMs Day 2: Guided Practice - Using Pipes with Splunk Solutions


### Question 1.

You are asked to investigate a number of TCP alerts.

  * The search command is: 
  
- Solution: `source="alert_json_000015.log" | top dst_ap`


  * Click on `Statistics`. How many search results were returned from the `top` command?

    * **Answer**: The `top` command returns the first `10` search results by default.

  * Look at the `Interesting Fields` down on the protocols, `prot` for short.  What were the top three scans that were performed?

    * **Answer**:

    * `ICMP`

    * `TPC`

    * `ARP`


Now, narrow **this search** so that it includes all the `TCP` traffic for the `top five` source IP addresses. Show **ONLY the number** of search results.

  * This search command uses the **logical AND operator** and **two pipes**.

- Solution: `source="alert_json_000015.log" AND proto="TCP" | top limit=5 src_ap | fields - percent`


### Question 2.

- **Sort** by the `destination IP` in `descending` order.

  * This search command uses the **sort command** and **one pipe**.
  
- Solution: `source="alert_json_000015.log" | sort -dst_ap`
    
#### Question 3:

Answer/Fill in the blank for the questions below:

- Limiting search by (blank) is key to faster results and is a best practice
  - `Solution: Time`
- The three main search modes?
  - `Solution: Fast, Verbose, and Smart`
- (Blank) mode has discovery off for event searches. No event or field data for stats searches.
  - `Solution: Fast`
- (Blank) mode has all events and field data; switches to this mode after visualization.
  - `Solution: Verbose`
- (Blank) mode (default-based on search string data) has field discovery ON for event searches. No event or field data for stats searches.
  - `Solution: Smart`
- List the three booleans
  - `Solution: NOT AND OR`
- When searching for exact phrases you need to use (Blank)
  - `Solution: Quotations`
- (Blank) fields that appear by default are host, sourcetype, source
  - `Solution: Selected Fields`

Having only the choices of `inclusion` and `exclusion` fill in the following:
- (Blank) is better than (Blank)
  - `Solution: Exclusion is better than inclusion`









