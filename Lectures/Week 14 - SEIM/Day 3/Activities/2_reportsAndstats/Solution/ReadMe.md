## Solution Guide: Generating a Statistical Report from Firewall Attack Logs 

### Solutions:

**1: Create the Search** 

- What field contains the **year(s)** for the attack?
  - `date_year`
- What field contains the **month(s)** for the attack?
  - `date_month`
- What field contains the **attack name**?
  -  `attack_name`
- What is the **attack name**?
  - `Oracle.9i,TNS.OneByte.Dos`
- Use the [NIST National Vulnerability Database](<https://nvd.nist.gov/vuln/detail/CVE-2002-0509>), "What does the attack do?"
  - `Description: The Transparent Network Substrate (TNS) Listener in Oracle 9i 9.0.1.1 allows remote attackers to cause a denial of service (CPU consumption) via a single malformed TCP packet to port 1521.`

Using this information, create a SPL search command that searches the firewall IPS event logs `using the attack name` and returns:

* the *count of attacks* by **year** and **month**

* then *sorts the counts* in descending order

* Execute the search using `All Time`.

* Add the SPL `stats` and `sort` command:

    ` | stats count by date_year, date_month | sort - count`

- **Solution**: `source="fortinet_logs.csv" attack_name="Oracle.9i.TNS.OneByte.DoS" | stats count by date_year, date_month | sort - count`


**2. Create the Statistical Report**

- Title = `OPS115:Firewall IPS Report`
  
- **Solution**: Click on `Save As` > Report. Give it a title of `OPS115:Firewall IPS Report`


**3. Find and Display the Report in the `Reports` list.** 

- Find and Display the Report in the Reports list.
   * Select the Report tab located in the App bar.

   * Click the Report Title (`OPS115: Firewall IPS Report`) and Open in Search.


**4. Extra Challenge:**

* How would you obtain the total number of attacks for each month for each year in the attack log?

- **Solution**: `Change the sort to "sort - date_month"`
- **Solution**: `source="fortinet_logs.csv" attack_name="Oracle.9i.TNS.OneByte.DoS" | stats count by date_year, date_month | sort - date_month`

#### 5. Report Results

* Document what month(s) and year(s) had the most attacks.

- **Solution**: `march` `2019`

Great job.  Activity complete!
