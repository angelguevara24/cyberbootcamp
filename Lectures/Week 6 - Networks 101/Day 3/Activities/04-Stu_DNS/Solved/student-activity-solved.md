### Students Do: DNS in Wireshark

Activity: DNS in Wireshark (Slides 22-23)

Part 1

- Open the `dns-1.pcap` file.
- You will only see replies but how many DNS requests were there?
  - 7
- When the user asked for `assets.espn.go.com`, what happened?
  - (Packet #5) `assets.espn.go.com` is an alias (CNAME) for `assets.espn.go.com.edgesuite.net` which, in turn, is an alias (CNAME) for `a1589.g.akamai.net`. The translation from that domain name to an IPv4 address (A records), returned 2 IPs: `69.31.75.194` and `69.31.75.203`.
- What is/are the IP address(es) for `a1.espncdn.com`?
  - (Packet #4) `72.246.56.35` and `72.246.56.83`.

Part 2

- Open the `dns-2.pcapng` file.
- This pcap shows a DNS query and response but something went wrong. What happened?
  - There was no IP address found for that domain name.
- Which flag in the packet signifies what went wrong?
  - The "Reply Code".
- The request went to 8.8.8.8. Did the answer come directly from 8.8.8.8?
  - No. 
