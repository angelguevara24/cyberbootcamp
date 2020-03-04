# Vulnerability Scanning

## Instructions

**Notes**: 

- You will need to turn on your Windows 10 VM before begining. 

- By default, Vulners by default is placed into the wrong location. In order to fix this please run the following commands to get it to work `cd /usr/share/nmap/scripts/nmap-vulners/` then `cp vulners.nse ..`

Now you're ready to begin:

- Save the results of _all scans_ to: `~/nmap_exercise`. You'll need to create the directory.

- Select your Kali instance, and launch a Terminal.

- Find your IP address.

- Use Nmap to perform host discovery on your subnet.

- Use Nmap to SYN scan the live hosts you discover.

- Use Nmap to UDP scan for DNS, DHCP, and TFTP on each of the live hosts you discover.

- Use Vulners to scan each machine for vulnerabilities.

- Review the vulnerability scan output. 
  - Which machines have the most critical CVEs? 
  - What are the three the most critical vulnerabilities you discovered?
