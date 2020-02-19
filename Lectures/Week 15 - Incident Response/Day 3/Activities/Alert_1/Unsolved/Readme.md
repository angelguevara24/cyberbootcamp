## Guided Practice: !Alert 1! (0:30)

In this exercise, you will investigate an alert file and ultimately determine if the alert is a `False Positive` or a `True Positive`

- You are provided with a Snort alerts file and a pcap file.

- There is a Hints section at the bottom of this file in case you get stuck. 

- Also, if you prefer to work backwards from the solution, you can access a solutions file [here](Activities/Alert_1/Solved/Readme.md). 

### Setup

- **Important**: All of today's exercises use live malware. Use your Ubuntu VM to work in a contained environment.

- We will use exercise files from [malware-traffic-analysis.net](malware-traffic-analysis.net). This site provides many open-source malware pcap files and activities for anyone to access and to use for practicing incident response and malware analysis.

    - Author, Brad Duncan (2019). *Timbershade*. Retrieved from [https://malware-traffic-analysis.net/2019/01/28/index.html](https://malware-traffic-analysis.net/2019/01/28/index.html)

- You may find it convenient to setup Slack on your VM, so you can access activities and links directly on your VM.

- Inside your VM, open the terminal and run `cd ~/Documents` to move to your documents folder.

- Run `mkdir alert_1` and `cd alert_1` to create and move into a working directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2019/01/28/2019-01-28-traffic-analysis-exercise.pcap.zip` and `wget https://malware-traffic-analysis.net/2019/01/28/2019-01-28-alerts-for-traffic-analysis-exercise.txt.zip` to download the required files.

- Run `unzip '*.zip' && rm *.zip` to unzip the files. 
    - The password for these files is: `infected`

### Instructions

#### Begin by examining the Snort file and answer the following questions:

- What activity is Snort reporting on? (Provide a few alert headlines.)

- What is the date and time of this alert?

- What is the external IP address that Snort is flagging for the ET Policy HTTP?

- What is the internal IP address that Snort is flagging for the ET Policy HTTP?

- What is the source port of the ET Policy HTTP?

- What is the destination port of the ET Policy HTTP?

#### Now, move into the pcap file:

- What is the MAC Address of the internal computer involved?

- What is the host name of the internal machine?

- Can you confirm the date and time this issue occurred?

- How can you confirm if the Snort alert is accurate?

- Can you safely verify whether or not malware was downloaded?

- Would you categorize this alert as a `False Positive` or a `True Positive`?

- If this issue needs to be mitigated, what steps should be taken with the infected machine?

- What steps should be taken in regards to network security?

- Would you categorize this issue as a Web, Email or Network attack?

### Hints

_Refer to the following Hints if you need additional guidance:_

#### Snort Alert Hints

- Try opening the Snort alerts file with `less alerts_file.txt` or open it with Splunk.

- Pay attention to the second line of each alert for clues regarding what happened.

- The third line of an alert displays IP address traffic flow.

- The fifth line of an alert displays the port information.

#### PCAP / Wireshark Alert Hints

- Remember that most downloads are going to be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.

- Don't forget you can chain filters together with `and`, `or`, etc.

- If you find an interesting packet, right click and `Follow > TCP/UDP Stream` for more info.

- You might also find interesting info in `File > Export Objects > HTTP`

- Command line tools like `file` and `md5sum` can be helpful too.

- Want to see if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload).
