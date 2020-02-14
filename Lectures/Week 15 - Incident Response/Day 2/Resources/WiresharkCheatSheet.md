### Incident Response CheatSheet

- When investigating an attack, a typical, high-level workflow could be:
    - Read alert from the Intrusion Detection System
        - Identify potential issue
        - Identify Source and Destination IP Addresses
        - Identify time estimate
    - Investigate pcap file with Wireshark:
        - Identify the host name of affected machine
        - Identify the MAC address of affected machine
        - Identify the source of the attack
        - Confirm that the attack was successful
            - Follow the TCP/UDP Stream
            - Extract HTTP Objects
            - Hash .exe files and check against virustotal.com

- **Important**: When investigating a real attack, it is important to upload hashes of the programs you find to VirusTotal, instead of uploading the file itself. This is because *if* the file is legitimate you may have just leaked sensitive company data. Even worse, if the file was previously unknown, VirusTotal now has a copy of it. Attackers may monitor VirusTotal to know when their software has been found so they can pivot to another attack.

### Log Searching Tips

#### GREP

- Remember that for quick searching of logs or alerts, you can easily use grep.

```bash
#Search for 'malware' inside log.text

grep 'malware' log.txt
```

```bash
#Search for 'cvc' inside log.txt

grep 'cvc' log.txt
```

```bash
#Search for 'Trojan inside log.txt'

grep 'trojan' log.txt
```

<details>
  <summary>Expand for Explanations of other filter options</summary>
  <ul>
    <li><code>-i</code>Ignores case of search pattern.
    <li><code>-n</code>Provides line numbers for each pattern that was found.
    <li><code>-P</code>Provides the entire paragraph where the pattern was found.
    <li><code>-r</code>Search recursively within a directory.
    <li><code>-v</code>Displays lines that `do not` match a pattern.
    <li><code>-W</code>Does a word search.
  </ul>
</details>

---

### Wireshark Tips

Once you find an HTTP packet or TCP packet of interest, you can get more detailed information about the entire 'conversation' between the two machines by right clicking on the packet and choosing:
#### Follow > Http Stream `OR` Follow > TCP Stream

<span style="color: red;">Red text</span> indicates communications sent by the client; i.e. the request. <br />
<span style="color: blue;">Blue text</span> indicates communications sent by the server; i.e the response.

#### See the Conversations of a pcap

- Go to `Statistics > Conversations`
    - The "IPv4" tab shows all of the IP Addresses involved in packet exchange.

#### See the number of hosts involved in a pcap

- Go to `Statistics > Endpoints`
    - The "Ethernet" tab shows a list of devices involved in the pcap.

### Wireshark Filters

#### Filter for all packets associated with a specific website

```bash
#Filter for all packets to and from ebay.com

http.host contains ebay
```

#### Filter for packets containing a specific string

```bash
#Filter for TCP packets containing 'john_doe'

tcp contains john_doe
```

#### Filter for HTTP

```bash
#Filter for HTTP Requests only

http.request
```

#### Filter for specific strings in a URI/URL

```bash
#Filter out any responses that contain javascript files

http.request.uri contains .js
```

Remember you can filter for all files using '.' and you can also filter for any other string in the URI/URL

#### Filter for all packets related to a specific IP Address

```bash
#Filter for packets comming from or going to the IP Address 172.18.0.3

ip.addr == 172.18.0.3
```

#### Filter for communication between 2 computers

```bash
#Filter for packets going between IP Address 172.18.0.3 and 172.18.0.2

ip.addr == 172.18.0.3 && ip.addr == 172.18.0.2
```
Here we are using the 'AND' operator to search for Filter 1 *AND* Filter 2.

#### Filter for packets on a specific port

```bash
#Filter for TCP OR UDP packets on port 80

tcp.port==80 || udp.port==80
```

Here we are using the 'OR' operator to filter for Filter 1 *OR* Filter 2.

#### Filter out or hide certain packets
```bash
#Filter out any icmp packets

!icmp
```
The 'NOT' operator can be used with any of the above filters to say *not* this filter.

#### Filter for only TCP handshake packets

```bash
#Filter only for SYN

tcp.flags.syn == 1
```

<details>
  <summary>Expand for Explanations of other filter options</summary>
  <ul>
    <li><code>tcp.port==</code> filter for TCP traffic related to a specific port.
    <li><code>udp.port==</code> filter for UDP traffic related to a specific port.
    <li><code>ip.dst==</code> specify a destination IP Address.
    <li><code>ip.src==</code> specify a source IP Address.
    <li><code>tcp</code> filters only for tcp packets.
    <li><code>udp</code> filters only for udp packets.
    <li><code>http</code> filters only for http packets.
    <li><code>http.request</code> filters only for http requests.
    <li><code>http.response</code> filters only for http responses.
    <li><code>||</code> the 'OR' operator.
    <li><code>&&</code> the 'AND' operator.
    <li><code>!</code> the 'NOT' operator.
  </ul>
</details>
