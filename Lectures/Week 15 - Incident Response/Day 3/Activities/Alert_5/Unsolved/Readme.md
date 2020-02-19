## Guided Practice: Alert 5! Activity

- In this activity, you will practice responding to an alert to determine if it is a `false positive` or a `true positive` alert.

### Setup

- **Important**: All of today's exercises use live malware. Use your Ubuntu VM to work in a contained environment.

- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and malware analysis.

   - Author, Brad Duncan (2019). *Stingrayahoy* Retrieved from [https://malware-traffic-analysis.net/2019/04/15/index.html](https://malware-traffic-analysis.net/2019/04/15/index.html)

- Move to your documents folder and create an `alert_5` directory for this exercise.

- The files you need are:

  - `https://malware-traffic-analysis.net/2019/04/15/2019-04-15-traffic-analysis-exercise.pcap.zip`

  - `https://malware-traffic-analysis.net/2019/04/15/2019-04-15-traffic-analysis-exercise-alerts.zip`

- Unzip the files. The password for these files is: `infected`.

### Instructions

- In this activity, you will responding to an alert to determine if it is a `False positive` or a `True positive` alert.

- You are provided with a snort alerts file and a pcap file.

#### Answer the following questions:

- What activity is Snort reporting on? (Provide a few alert headlines.)

- What is the date and time of the alert?

- What is the external IP address and port that Snort is flagging?

- What is the internal IP address and port that Snort is flagging?

#### Now, use the pcap file to answer the following questions: 

- What is the MAC Address of the internal computer involved?

- What is the host name of the internal machine?

- Can you confirm the date and time this issue occurred? Does it match the snort alert?

- Can you confirm if the Snort alert was accurate and verify that malware was downloaded?

- Would you categorize this alert as a `False Positive` or a `True Positive`?

- If this issue needs to be mitigated, what steps should be taken with the infected machine?

- What steps should be taken in regards to network security?

- Would you categorize this issue as a Web, Email or Network attack?