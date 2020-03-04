# Vulnerability Scanning

## Instructions
- Note: You will need to turn on your Windows 10 VM before begining. 
- Note: Vulners by default is placed into the wrong location. In order to fix this please run the following commands to get it to work `cd /usr/share/nmap/scripts/nmap-vulners/` then `cp vulners.nse ..`
- Save the results of _all scans_ to: `~/nmap_exercise`. You'll need to create the directory.

- Select your Kali instance, and launch a Terminal.

- Find your IP address.
  > **Solution**: `ifconfig`. Different machines will have different IP addresses—mine was `192.168.1.15`.

- Use Nmap to perform host discovery on your subnet.
  > **Solution**: `nmap -sn 192.168.1.101/24 -oN ~/nmap_exercise/hosts.txt`

- Use Nmap to SYN scan the live hosts you discover.
  > **Solution**: `nmap -sV 192.168.1.100 192.168.1.200 192.168.1.5 192.168.1.101 -oN ~/nmap_exercise/syn.txt`

- Use Nmap to UDP scan for DNS; DHCP; and TFTP on each of the live hosts you discover.
  > **Solution**: `nmap -sU -p 53,67,68,69 192.168.1.100 192.168.1.200 192.168.1.5 192.168.1.101 -oN ~/nmap_exercise/udp.txt`

- Use Vulners to scan each machine for vulnerabilities.
  > **Solution**: `nmap -sV --script vulners 192.168.1.100 192.168.1.200 192.168.1.5 192.168.1.101 -oN ~/nmap_exercise/vulners_results.txt`

- Review the vulnerability scan output. 
  - Which machines have the most critical CVEs? 

- Consider the 5-10 worst CVEs (in terms of 1-10 severity). 
  - Which services do they pertain to? 
  - Which service appears most frequently?
  - What is this service for?

  > **Solution**: The top 5 worst CVEs in my results all pertain to Apache. This makes sense, as it's an HTTP/web server.
