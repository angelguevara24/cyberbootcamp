## Guided Practice: Alert 3! Activity

- In this activity, you will practice responding to an alert to determine if it is a `false positive` or a `true positive` alert.

### Setup

- **Important**: All of today's exercises use live malware. Use your Ubuntu VM to work in a contained environment.

- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and malware analysis.

   - Author, Brad Duncan (2019). *Turkey and Defense* Retrieved from [https://malware-traffic-analysis.net/2018/11/13/index.html](https://malware-traffic-analysis.net/2018/11/13/index.html)

- Move to your documents folder and create an `alert_3` directory for this exercise.

- The files you need are:

  - `https://malware-traffic-analysis.net/2018/11/13/2018-11-13-traffic-analysis-exercise.pcap.zip`

  - `https://malware-traffic-analysis.net/2018/11/13/2018-11-13-traffic-analysis-exercise-alerts.zip`

- Unzip the files. The password for these files is: `infected`.

### Instructions

- In this activity, you will responding to an alert to determine if it is a `False positive` or a `True positive` alert. 

- You are provided with a snort alerts file and a pcap file.

- There is a hints section at the bottom if you get stuck. 

- Also, if you prefer to work backwards from the solution, you can access a solutions file [here](Activities/Alert_3/Solved/Readme.md).

#### Answer the following questions:

- What activity is Snort reporting on? (Provide a few alert headlines.)

- What is the date and time of this alert?

- What is the external IP address that Snort is flagging for the ET TROJAN VMProtect alert?

- What is the internal IP address that Snort is flagging for the ET TROJAN VMProtect alert?

- What is the source port for the ET TROJAN VMProtect alert?

- What is the destination port for the ET TROJAN VMProtect alert?

#### Now, use the pcap file to answer the following questions: 

- What are the MAC Addresses of the computers involved?

- What is the host name of the internal machine?

- Can you confirm the date and time this issue occurred?

- How can you confirm if the Snort alert is accurate?

- Can you safely verify whether or not malware was downloaded?

- Would you categorize this alert as a `False Positive` or a `True Positive`?

- If this issue needs to be mitigated, what steps should be taken with the infected machine?

- What steps should be taken in regards to network security?

- Would you categorize this issue as a Web, Email or Network attack?

### Hints

Refer to the following hints sections if you need additional guidance:

#### Snort Alert Hints

- Try opening the Snort alerts file with `less alerts_file.txt` or open it with Splunk.

- Pay attention to the second line of each alert for clues about what happened.

- The third line of an alert displays the IP address traffic flow.

- The fifth line of an alert displays the the port information.

#### PCAP / Wireshark Alert Hints

- Remember that most downloads are going to be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.

- Don't forget you can chain filters together with `and`, `or`, etc.

- If you find an interesting packet, right click and `Follow > TCP/UDP Stream` for more info.

- You might also find interesting info in `File > Export Objects > HTTP`.

- Command line tools like `file` and `md5sum` will help too.

- Want to see if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload).