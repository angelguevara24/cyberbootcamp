## Student Activity: Monitoring Snort Logs and Firing Rules (0:30)

### Instructions

**Please follow the instructions located here, not the instructions on Cyberscore**

For this exercise, use the lab `Snort Signatures, IDS Tuning, and Blocking`. 
- Launch Snorby and log on with the credentials: username: `admin@business.org`, password: `password`.
- If you run into any warnings complete the following:
  - Click on `Advanced`.
  - Click on `Proceed to localhost`.

- Familiarize yourself with the UI. Note the **Low**, **Medium**, and **High Severity** counters, as well as the **Sensors**, **Severities**, and other tabs right below.

Next, you'll make Snort fire rules by sending suspicious traffic from a different machine.
  - Log into the Kali machine. Click **Resources** and then select **Kali LAN**.
  - Launch a Terminal.
  - Use `nmap` to find the IP address of the Windows machine: `nmap -sn 192.168.11.0/24`.
  - Once you have identified the IP address of the Windows machine run `ping <IP address of Windows machine>`.
  - Port-scan the Windows machine: `nmap -sS <IP address of Windows machine>`. 
  
Now, you'll see which rules were triggered in Snort.
  - Return to SNORBY on the **Security Onion** machine.
  - Note how many **Low**, **Medium**,  and **High** severity events were registered.
    - Depending on your lab environment you might need to click on each level to see the results as Snorby takes awhile to cache the results. 

Inspect the **Medium** and **Low** severity events. Answer the following below:
- What was the **source IP** of each event?
- Which **Event Signatures** were **Low** severity? Why aren't these higher severity?
- Which **Event Signatures** were **Medium** severity? Why aren't these lower or higher severity?

Return to the Kali machine, and generate the following traffic:
  - Run a full version scan against the Windows machine's top 50 ports: `nmap -sV --top-ports 50 <IP address of Windows machine>`
  - Use Nmap scripts to launch an SMB brute-force attack: `nmap --script smb-brute -p U:137,T:139 <IP address of Windows machine>`

Return to SNORBY and answer the following questions:
  - How many events of each severity do you see?
  - Which types of events qualify as **High**, **Medium**, and **Low** severity?
