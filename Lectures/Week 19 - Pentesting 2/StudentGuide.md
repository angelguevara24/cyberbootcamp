# Student Guide
## Pentesting Week 2 — Advanced Enumeration

### Reviewing Last Week
Last week, we got our feet wet with the first phases of a Penetration Test: **Intelligence Gathering** and **Exploitation**.

By now, you should be familiar with the following:
- **Intelligence Gathering**
  - Identify hosts vulnerable to Heartbleed.
  - Use `searchsploit` to research _manual_ exploits and scripts related to Heartbleed.
  - Perform intense scans of target hosts using Zenmap.
  - Identify specific vulnerabilities like Shellshock using Nmap scripts, such as `http-shellshock`
- **Exploitation**
  - Use Burp Suite to manually send injection payloads to servers vulnerable to Shellshock
  - Use Metasploit to exploit Heartbleed and Shellshock automatically

The **main takeaways** are:
- Pentesters follow a **methodology** when attacking targets. They _always_ begin with  **Intelligence Gathering**, then analyze what they've learned about their targets to find vulnerabilities.
- The most important **Intelligence Gathering** steps are:
  - **Host Discovery**: Reveals which hosts are on the network
  - **Port Scanning**: Reveals which ports are open on each host
  - **Version Scanning**: Reveals which services, and which versions, are running on each port
- After version scanning by _manually_ identifying **common vulnerable services**. These include:
  - Old versions of any service
  - Old operating systems
  - Login servers (SSH, telnet, etc.—these can often be brute-forced to get a user shell)
 - After manual analysis, pentesters often use Metasploit and `searchsploit` to find ways to **exploit** the target machine.

You covered a lot of tools, tactics, and procedures (TTPs, as pentesters call them), so don't feel discouraged if it hasn't all "stuck" yet: As long as you have the above takeaways in mind, you've done your work. Remembering the individual commands simply takes time:  Even professional pentesters use "cheat sheets", like the [Red Team Field Manual](https://github.com/Agahlot/RTFM/blob/master/rtfm-red-team-field-manual.pdf), to remind them which commands to run in which scenarios. It is **highly encouraged** that you print out your Pentesting cheatsheets, and keep them on hand as you work through your exercises and homework assignments. This will serve as its own "field guide", and you'll remember the commands you use most frequently.

### Topics This Week
This week builds on what you learned last week by exploring:
- More advanced scanning and enumeration techniques
- How to steal/**exfiltrate** data
- How to create custom malware to exploit arbitrary targets

These are powerful techniques used by attackers of all ilks. You'll learn several new techniques this week, which you can see listed in full below.

At the end of this week, you should be able to:
- Use Metasploit to exploit Heartbleed and Shellshock.
- Perform advanced scans with **Nmap**
- Save and organize the results of these scans with Metasploit's **workspaces** and built-in **database**
- Perform a brute-force against an SSH server with **Hydra**
- Perform reconnaissance on compromised hosts.
- Transfer files between machines using Ncat
- Manually dump information from a MySQL database
- Crack password hashes with John the Ripper
- Creating malicious binaries with `msfvenom`
- Serving files to compromised hosts via HTTP
- Running Metasploit modules through backgrounded Meterpreter sessions

### Homework This Week

Machines on a LAN send requests to the public Internet through a router, which forwards requests to the web after performing NAT, and forwards responses back to the requesting host on the LAN. This router typically has a firewall that only allows connections to/from certain ports.

Network engineers can add an additional layer of protection to the network by installing a **DMZ (demilitarized zone)**, which acts as an additional layer of protection in front of an existing network.

In this week's homework assignment, you will apply the techniques you learned in class to pivot across subnets and attack a DMZ.

### Why We Care | Job Titles Related to These Skills
Pentesting weeks are all about Penetration Testing. Penetration Testing is a high paying role with an average U.S. Salary of $95k/year. Vulnerability Aanlyst, or completing Vulnerability assessments is also a related role that pays very well.

### Links for Self Study
Here you will find links to references to use if you are having trouble and more reading to complete if you would like to dive deeper into Penetration Testing and/or Vulnerability Assessment. We recommend waiting until you've completed _all_ assignments for the unit before adding this material to your plate.
- [Red Team Field Manual](https://github.com/Agahlot/RTFM/blob/master/rtfm-red-team-field-manual.pdf)
- [Offensive Security Documentation](https://www.offensive-security.com/metasploit-unleashed/payload-types/)
