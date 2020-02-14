## Activity: Wireshark Practice

- In this activity, you investigate a malware attack using a Snort alert file and a network pcap.

### Setup

- **Important**: This exercise uses live malware. Make sure to use your Ubuntu VM to work in a contained environment.

- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and/or malware analysis.

     Author, Brad Duncan (2019). *Stormtheory* Retrieved from [https://www.malware-traffic-analysis.net/2019/02/23/index.html](https://malware-traffic-analysis.net/2019/02/23/index.html)

- Inside your VM, open the terminal and run `cd ~/Documents` to move to your documents folder.

- Run `mkdir alert` and `cd alert` to create and move into a working directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise.pcap.zip` and `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise-alerts.zip` to download the needed pcaps.

- Run `unzip '*.zip' && rm *.zip` to unzip the files. The password for these files is: `infected`

### Instructions

- In this exercise, you will locate and identify malware that has infected a host.

- You are provided with a Snort alerts file and a pcap file. You can use `grep` to search Snort files or use `less` to read through them. You can also use Splunk to search them.

- Hints are located at the bottom of this exercise if you get stuck. Also, you can use [the solution file](Activities/WireSharkFollowUp/Solved/Readme.md) if you would prefer to work backwards from the answers.

- Examining the Snort file and answer the following questions:

    - What activity is Snort reporting on? (Provide a few alert headlines)

    - What is the date and time of this alert?

    - What is the external IP address that Snort is flagging for malicious activity?

    - What is the internal IP address that Snort is flagging for malicious activity?

    - What is the source port of the activity?

    - What is the destination port of the activity?

- Examine the pcap file and answer the following questions:

    - Filter the pcap file to show you the conversation between the two machines that were identified in the Snort alert.

    - What are the MAC addresses of the computers involved?

    - What is the host name of the internal machine?

    - Can you confirm the date and time that this issue occurred?

    - How can you confirm if the Snort alert is accurate?

    - Can you safely verify whether or not malware was downloaded?

    - Would you categorize this alert as a `False Positive` or a `True Positive`?

    - If this issue needs to be mitigated, what steps should be taken with the infected machine?

    - What steps should be taken in regards to network security?

    - Would you categorize this issue as a Web, Email or Network attack?

#### Snort Alert Hints

- Try opening the Snort alerts file with `less alerts_file.txt`

- Pay attention to the second line of each alert for clues about what happened.

- The third line of an alert shows the IP address traffic flow.

- The fifth line of an alert shows the port information.

#### PCAP / Wireshark Alert Hints

- Remember that most downloads are going to be `HTTP` requests, so Wireshark filters like `ip.addr eq` and `http.request` should prove helpful.

- Don't forget you can chain filters together with `and`, `or` and the like.

- If you find an interesting packet, right click and select `Follow > TCP/UDP Stream` for more info.

- You may also find interesting info in `File > Export Objects > HTTP`.

- Command line tools like `file` and `md5sum` will help too.

- Want to check if something is malicious? Visit [Virus Total](https://www.virustotal.com/#/home/upload).