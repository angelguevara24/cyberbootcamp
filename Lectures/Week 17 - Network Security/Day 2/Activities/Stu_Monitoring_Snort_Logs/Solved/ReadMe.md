## Solution Guide: Monitoring Snort Logs and Firing Rules (0:30)

### Instructions

Inspect the **Medium** and **Low** severity events. Answer the questions below:
  
  - What was the **source IP** of each event? 
    - **Solution**: ICMP traffic is flagged as **Low Severity**. This is low (as opposed to "no") severity because attackers can discover machines that reply to ping requests by running ping scans.
  
  - Which **Event Signatures** were **Low** severity? Why aren't these higher severity?
    - **Solution**: ICMP traffic is flagged as **Low Severity**. This is low (as opposed to "no") severity because attackers can discover machines that reply to ping requests by running ping scans.
  
  - Which **Event Signatures** were **Medium** severity? Why aren't these lower or higher severity?
  
    **Solution:**
  
    - Snort detects Nmap's port scans, and classifies it as **Medium Severity** traffic. This is because, while not dangerous in and of itself, port scans are suggestive of reconnaissance and future malicious activity.
    - The SMB brute-force attack is flagged as **High Severity**. Unlike port or ping scans, this is an intentional _attack_, which may result in compromise of the server if successful.

Return to SNORBY, and answer the following questions.
- How many events of each severity do you see?
    - **Solution**: This is a different number depending on each instance as each one in the classroom ran a different amount of pings.

- Which types of events qualify as **High**, **Medium**, and **Low** severity?

  **Solution:**
  - Discovery scans (e.g., ping sweeps) are often flagged as **Low Severity**.
  - Port and version scans are offten flagged as **Medium Severity**, because they are often stepping stones to intentional attacks.
  - Intentional attacks are typically flagged as **High Severity**.
