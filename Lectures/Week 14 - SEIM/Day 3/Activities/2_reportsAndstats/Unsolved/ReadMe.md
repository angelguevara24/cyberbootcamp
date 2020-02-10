## Student Activity: Generating a Statistical Report from Firewall Attack Logs

### Instructions

Welcome to the Activity!  You may select a teammate to work with you on this exercise.

Your team works in a corporate digital forensic department and have been tasked to look at past network activity.  Your department analyzes logs such as traffic logs, anti-virus logs and attack logs for various government agencies (*The Customer*).

Your team is to prepare a **statistical report** for The Customer's digital forensics case.  The Customer's IPS logs contain detailed information about whether the network was protected as well as the nature of the attack.  

The team will start by reviewing *firewall attack log* event data collected for several years.  The task is to prepare a report that provides information on a specific attack during this time.

### Starting the Investigation

Begin by uploading the `fortinet_logs.csv` file into Splunk.

Review the fields in the `Interesting Fields` list and answer the following questions:

1. What are the **years** for the attack data?

2. What is the **attack name**?

3. Using the **NIST National Vulnerability Database**, What does the attack do?

4. What **port** does the attack target?


### Getting Started

We introduce another new SPL command that will help you with the investigation. The command is `stats` and it provides statistics such as `average`, `count` or `sum`.
 
 The syntax for the command to obtain the **count** is: 
 
 `stats by count <field>, <field>, <field> ...` where:

 - `stats` is the Splunk command

 - `count` provides the number of events

 - `field` is a field in the event

 For example: `stats by count "field1", "field2", "field3" ...`

 Documentation for the command can be found [here](<https://docs.splunk.com/Documentation/SplunkCloud/latest/SearchReference/Stats>)


#### 1: Create the Search 

The team will start by gathering information on the number of attacks that occurred in a given year.

Locate these **fields** to analyze the detected attack attempts.

- What field contains the **year(s)** for the attack?

- What field contains the **month(s)** for the attack?

- What field contains the **attack name**?

- What is the **attack name**?

- Use the [NIST National Vulnerability Database](<https://nvd.nist.gov/vuln/detail/CVE-2002-0509>), "What does the attack do?"

**Move** the fields from the previous answers to the `Selected Fields` list.

Using this information you have found, create an SPL search command that searches the firewall IPS event logs `using the attack name` and returns:

* The *count of attacks* by **year** and **month**

* Then *sorts the counts* in **descending** order (we used the SPL **sort command** in Day 2). 

* And executes the search using `All Time`.


#### 2. Create the Statistical Search Report

* Save the search as a Report with:

- Title = OPS115: `Firewall IPS Report`

* Save and view the Report.

#### 3:  Locate the Report in Splunk

* Find and Display the Report in the `Reports` list.

#### 4. Extra Challenge:

* How would you obtain the total number of attacks for each month for each year in the attack log?

#### 5. Report Results

* Document what month(s) and year(s) had the most attacks.