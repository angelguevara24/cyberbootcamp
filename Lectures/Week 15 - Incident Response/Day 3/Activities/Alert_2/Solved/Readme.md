## Solution Guide: Alert 2! Review

### Solutions: 

- What activity is Snort reporting on? (Provide a few alert headlines)

    - "MALWARE-OTHER HTTP POST request to a RAR file"

    - "FILE-EXECUTABLE Portable Executable binary file magic detected"

    - "ET POLICY Binary Download Smaller than 1 MB Likely Hostile"

    - "ETPRO TROJAN Common Downloader Header Pattern H"

    ![](Images/Snort1.jpg)
    
    ![](Images/Suratica.jpg)

- What is the date and time of the ET POLICY Binary alert?

    - **Solution:** 2018-08-11 06:10:12


- What is the external IP address that snort is flagging for the ET POLICY Binary alert?

    - **Solution:** 149.129.222.112


- What is the internal IP address that Snort is flagging for the ET POLICY Binary alert?
  
    **Solution:** 10.8.11.101

- What is the source port for the ET POLICY Binary alert?

    **Solution:** 80

- What is the destination port for the ET POLICY Binary alert?

    **Solution:** 49162

    ![](Images/SnortDateTime.jpg)


#### Use Wireshark to answer the following questions:

- What is the MAC Address of the internal computer involved?


    **Solution:** f4:b5:20:68:b1:93

- What is the host name of the internal machine?

    **Solution:** Filter for `bootp` in Wireshark and inspect the `Option: Host Name` from an `Inform` packet.

    - The host name is `Petrov2018-PC`.

    ![](Images/BOOTP.jpg)

- Can you confirm the date and time this issue occurred?

    **Solution:** pcap file shows 2018-08-11 1:20 UTC

    ![](Images/TimeStamp.jpg)

- How can you confirm if the snort alert is accurate?

    **Solution:** Following the TCP Stream of the machines in the alert shows a `POST` request to `/1.rar`.

    -  The rest of the stream shows a powershell command that downloads an executable `r53x.com/1.zip`.

    ![](Images/tcpStream.jpg)

- Can you safely verify whether or not malware was downloaded?

    **Solution:** Using `File > Export Objects > HTTP`, you can export `1.zip` and `1.rar` files

    -  Verify this is malware using `md5sum` and [Virus Total](https://virustotal.com/#/home/search).
    
    - You can also search the offending IP address at Virus Total.

    ![](Images/httpObjects.jpg)

- Can you determine which email had a malware attachment related to the Snort Alerts?

    **Solution:** Locate the `.eml` activity files that you downloaded at the start of the exercise. 
 
    - Open each email by right-clicking and choosing `Open with other application` > Thunderbird Mail

    - Save all 3 attachments from each email in the activity directory.

    ![](Images/Email1.jpg)

    - Use the `file` command to determine the file type of each file.

    - One of the files (`PIC35793.iqy`) is a text file.

    - Using the `less` command, we can see a link inside: `r53x.com/1.rar`

    -  The first email appears to be the culprit.

    ![](Images/Email2.jpg)

- Would you categorize this alert as a `False Positive` or a `True Positive`?

    **Solution:** This is categorized as a `True Positive` because we confirmed a malware infection.

- If this issue needs to be mitigated, what steps should be taken with the infected machine?

    **Solution:** The machine should be restored to a backup prior to this infection.

- What steps should be taken in regards to network security?

    **Solution:** We can block that IP Address using: `iptables --append INPUT --in-interface eth0 --source 149.129.222.112/32 --jump DROP`

    ![](Images/Iptables.jpg)

- Would you categorize this issue as a Web, Email or Network attack?

    **Solution:** This started with an email attachment so this would be an `Email Attack`

Answer any questions students have before taking a break.