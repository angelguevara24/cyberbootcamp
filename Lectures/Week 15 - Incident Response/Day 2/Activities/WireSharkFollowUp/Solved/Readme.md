## Solution File: Wireshark Follow-up Practice

- In this activity, you will investigate a malware attack using a Snort alert file and a network pcap.

### Setup

**Important**: This exercise uses live malware. Start with using your Ubuntu VM to work in a contained environment.

- We will use exercise files from malware-traffic-analysis.net. This site provides many open-source malware pcap files and activities for anyone to access and use to practice incident response and/or malware analysis.
    - Author, Brad Duncan (2019). *Stormtheory* Retrieved from [https://www.malware-traffic-analysis.net/2019/02/23/index.html](https://malware-traffic-analysis.net/2019/02/23/index.html)

- Inside your VM, open the terminal and run `cd ~/Documents` to move to your documents folder.

- Run `mkdir Stormtheory` and `cd Stormtheory` to create and move into a working directory for this exercise.

- Run `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise.pcap.zip` and `wget https://malware-traffic-analysis.net/2019/02/23/2019-02-23-traffic-analysis-exercise-alerts.zip` to download the needed pcaps.

- Run `unzip *.zip && rm *.zip` to unzip the files.

- The password for these files is: `infected`

### Solutions

Examining the snort file and answer these questions:

- What activity is snort reporting on? (Provide a few alert headlines)
    - `likely Evil EXE download from dotted Quad by MSXMLHTTP"`
    - `"ET Malware Windows executable sent when remote host claims to send an image"`
    - `"ET Trojan [PTsecurity] Trickbot Data Exfiltration"`

- What is the date and time of this alert?
    - `2019-02-23 19:27`

- What is the external IP address that snort is flagging for malicious activity?
    - `209.141.55.226`

- What is the internal IP address that snort is flagging for malicious activity?
    - `10.2.23.231`

- What is the source port of the activity?
    - `80`

- What is the destination port of the activity?
    - `49195`

Examine the pcap file and answer the following questions:

- Filter the pcap file to show you the conversation between the two machines that were identified in the snort alert.
    - `http.request and ip.addr eq 209.141.55.226 and ip.addr eq 10.2.23.231`

- What is the MAC Addresses of the internal computer?
    - `While inspecting this packet, under the "Ethernet II' section", we can see that this is a likely a Windows machine with the name: "HewlettP and the MAC Address: (00:11:0a:9f:c0:2d)`

- What is the host name of the infected machine?
    - `Filter Wireshark for "bootp" which gives you "DHCP" traffic.`
    - `In the packet info, under the "Bootstrap Protocol" there is an "Option: (xx)Host Name"`
    - `This machine's host name is Ferguson-Win-PC`

- Can you confirm the date and time this issue occurred?
    - `pcap shows 2019-02-23 14:27 UTC`

- How can you confirm if the snort alert is accurate?
    - `Following the TCP stream shows binary data with "!This program cannot be run in DOS mode."`
    - `Shows the file named "troll1.jpg"`

- Can you safely verify whether or not malware was downloaded?
    - `Using "File > Export Objects > HTTP", choose the "troll1.jpg" file out of the list and save it.`
    - `Run "md5sum troll1.jpg" to hash the file.`
    - `Visit [Virus Total](https://www.virustotal.com/gui/home/upload) and paste in the hash to verify malware.`

- Would you categorize this alert as a **False Positive** or a **True Positive**?
    - `Malware was verified to be downloaded, so this snort alert is "True Positive".`

- If this issue needs to be mitigated, what steps should be taken with the infected machine?
    - `The Machine should be restored to a backup prior to this incident.`

- What steps should be taken in regards to network security? 
    - We can use Wireshark to create a firewall rule:
    - Block #IPv4 malicious address.
    - `iptables --append INPUT --in-interface etho --source 209.141.55.226/32 --jump DROP`
        
        - Remember that this is only a suggestion from Wireshark as to what rule you _could_ add to your firewall. It is not actually changing any firewall rules.

- Would you categorize this issue as a Web, Email or Network attack?
    - `This attack was propagated by visiting a malicious web link, so this is a "Web Attack".`
