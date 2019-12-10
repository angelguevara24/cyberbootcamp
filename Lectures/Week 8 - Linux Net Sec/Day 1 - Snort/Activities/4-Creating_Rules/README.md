# Creating Rules
In this exercise, you'll write Snort rules and test them against live traffic.

## Instructions

**Note**: After writing each rule, start Snort, then inspect the Snort `alert` file to check that it was fired.

---

- Open the `local.rules` file.
- Add the rules described below:
  - Write a rule that detects telnet traffic from the public Internet to the local subnet.
  - Write a rule that detects an attacker running a tcp scan on any port. 
      - **Hint**: Be sure to specify the correct destination port(s).

**Note**: Here's an example of the rule structure: **alert ip any any -> any any {msg “IP Packet Detected”;}**