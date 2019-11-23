### Student Activity

Activity: TCP in Wireshark (Slide 21)

Pre-requisite:

- Students should download the `student-activity.pcapng` file

  ---

- Start Wireshark.
- Open up the provided .pcap file.
- Filter for TCP packets only.
  - `tcp`
- Find all TCP SYN packets.
  - `tcp.flags.syn eq 1` or manually count up the SYN packets.
- Find all TCP FIN packets.
  - `tcp.flags.fin eq 1` or manually count up the FIN packets.
- Filter for a single TCP stream using the "FTP" protocol.
  - Right click any packet with "FTP" in the "Protocol" field (e.g. packet #94).
  - Select "Follow" -> "TCP Stream".
- Find the 3-way handshake sequence
  - Packets number 53-55.
- Find the TCP teardown sequence
  - Packets number 107-111.
- What are the source/destination IP addresses and ports?
  - Source IP: 192.168.29.54
  - Destination IP: 90.130.70.73
  - Source Port: 34836
  - Destination Port: 21
