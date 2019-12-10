# Creating Rules
In this exercise, you'll write Snort rules and test them against live traffic.

## Instructions

**Note**: After writing each rule, start Snort, then inspect the Snort `alert` file to check that it was fired.

---

- Open the `local.rules` file.
- Comment out all of the existing rules.
- Add the rules described below:
  - Write a rule that detects telnet traffic from the public Internet to the local subnet.
  - Write a rule that detects an attacker running a tcp scan on any port. 
      - **Hint**: Be sure to specify the correct destination port(s).

- **Bonus**: After implementing your rules, retrieve the `alert` file from your VM, and send it to the class via Slack.
