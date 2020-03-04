# Access Control

In this exercise, you'll address the HTTP brute force attack you captured in the previous exercise by implementing a firewall rule on the target web server that drops traffic from the attacking host.

In particular, you will:
- SSH into the web server
- Use `tcpdump` to identify the IP address of the attacking machine
- Write a firewall rule that blocks traffic from that IP address

This exercise is intended to link your existing knowledge of traffic capture and analysis with the new concepts of designing and implementing firewall rules.

## Setup

This exercise requires Docker. To get started, make sure you're in `Stu_Access_Control/Resources`, and run the commands below.

  ```bash
  # Remove any running containers
  docker rm -vf $(docker ps -a -q)

  # Make sure you're in `Stu_Access_Control/Resources`
  docker-compose up -d
  docker exec -it Target bash
  ```

This should drop you into a root shell on `Target`. Once you're in, follow the instructions below.

**Good luck!**

## Instructions

- Once you've opened your shell on the web server, use `tcpdump` to capture HTTP traffic on all interfaces. Do _not_ save it to a file. Simply take a glance at the captured packets to identify the URL of the attacking machine.
  - **Solution**: `tcpdump -i any -n`

- Then, verify that you've identified the correct IP address by capturing only HTTP traffic from the IP Address you identified.
    - This capture provides a baseline profile of what traffic from your suspicious address looks like _before_ implementing an access control policy. It should look similar to the capture from the previous step.
    - **Solution**: `tcpdump -i any src 172.22.0.3 -n`. Your attacking machine's source IP may be different.

- Next, write a `ufw` rule to deny all traffic from the attacking IP Address you identified.
    - **Solution**: `ufw deny from 172.22.0.3 to any`

- _start_ the firewall.
    - **Solution**: `ufw enable`

- Finally, Verify that your change has been implemented by displaying your active firewall rules.
    - **Solution**: `ufw status verbose`

- Use `tcpdump` to verify that your firewall rule is, in fact, blocking traffic from the attacker's IP Address.
    - **Solution**: `tcpdump -i any src 172.22.0.3 port http`. Your attacking machine's source IP may be different.

## Extension

As discussed, logging suspicious network activity for post-mortem analysis is crucial for protecting networks long-term.

UFW can be configured to log all packets that it drops with the following commands:

  ```bash
  # Displays whether logging is enabled
  ufw status verbose

  # Turn on logging
  ufw logging on

  # Inspect logs of dropped packets
  less /var/log/ufw.log
  ```

The file `/var/log/ufw.log` contains details about every packet UFW drops. This allows you to scan it for artifacts, signatures, patterns, etc., which you can later be used to support forensic investigations; identify patterns and signatures for use in an IDS; etc.

You're encouraged to take the time to enable UFW logging in your Docker container, and inspect the `ufw.log` file.

As a final note—on most Linux machines, you'll have to prefix `ufw` commands with `sudo`. Today, we're running directly as root, so this isn't necessary—but keep it in mind when you configure a live box on the network!
