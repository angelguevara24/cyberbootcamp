# Warm-Up

In this exercise, you'll review the major takeaways from yesterday's lesson, including:
  - Packet Captures with tcpdump
  - Implement `deny` rules with `ufw`

## Instructions

### Packet Captures with tcpdump

Refer to the tcpdump Primer: <https://danielmiessler.com/study/tcpdump/>

- On the Workstation, move to `/tmp`.

- Start a packet capture, and save it to the file `mystery.pcap`.
  - **Note**: Be sure to save the entire packet ("snaplength"), and listen on any interface.

- Open the capture with Wireshark, and filter for `tcp`. Right-click on one of the TCP packets, and click **Follow Stream**.
  - Based on what you know about NMap, what kind of traffic is this?
  - Identify the IP Address of the attacking machine.

### Access Control with UFW

- Implement a deny rule with UFW that blocks all traffic from the offender.

- List your firewall rules to ensure the rule was added, and use tcpdump to verify that it's in effect.
