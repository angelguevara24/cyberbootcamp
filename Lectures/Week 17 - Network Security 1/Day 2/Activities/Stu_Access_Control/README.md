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

This should drop you into a root shell on the `Target` machine. Once you're in, follow the instructions below.

**Good luck!**

## Instructions

- Once you've opened your shell on the web server, use `tcpdump` to capture HTTP traffic on all interfaces. Do _not_ save it to a file. Simply take a glance at the captured packets to identify the URL of the attacking machine.
  - **Note**: This review of the previous exercise is required because the attacking machine's IP address can change between lab launches.
  - **Hint**: Use the `-n` flag to `tcpdump` to get the attacking machine's IP address.

- Then, verify that you've identified the correct IP address by capturing only HTTP traffic from the IP Address you identified.
    - This capture provides a baseline profile of what traffic from your suspicious address looks like _before_ implementing an access control policy. It should look similar to the capture from the previous step.

- Next, write a `ufw` rule to deny all traffic from the attacking IP Address you identified.
    - Refer to the following reference for examples of UFW allow and deny rules: <https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands>

- _Start_ the firewall.
  - **Hint**: Refer to the Arch Wiki linked above.
  - **Nojte**: If you get `ERROR: problem running ufw-init`, please run the command again. It should work the second time.

- Finally, verify that your change has been implemented by displaying your active firewall rules.
  - **Hint**: Check the Arch Wiki for details on how to check the _status_ of your firewall rules: <https://wiki.archlinux.org/index.php/Uncomplicated_Firewall>


- Use `tcpdump` to verify that your firewall rule is, in fact, blocking traffic from the attacker's IP Address.
