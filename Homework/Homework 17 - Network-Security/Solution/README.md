# UFW Configuration

### Scenario

- You have been hired by the company "You Can't Handle the Tooth" _Dental Extraction_, to come in and set up their firewall for their Linux server. They have provided you with a VM that already has preconfigured network services, namely: SSH, telnet, Apache and FTP. The VM already has UFW enabled, with defaults set to deny all incoming and outgoing traffic. They have asked that you make configuration changes specifically...

   - Enable the `Apache Full` UFW profile
   - Allow outbound DNS
		- `Solution: ufw allow out 53`
   - Allow inbound SSH _only from the local subnet_
   		- `Solution: ufw allow from 10.0.2.0/24 to any port 22`
   - Allow inbound telnet _only from the local subnet_
      	- `Solution: ufw allow from 10.0.2.0/24 to any port 23`
   - Allow FTP _only from the local subnet_
      	- `Solution: ufw allow from 10.0.2.0/24 to any port 21`
   - Drop inbound ICMP from outside the local subnet
 		- `nano /etc/ufw/sysctl.conf` change to `net/ipv4/icmp_echo_ignore_all=1` to `net/ipv4/icmp_echo_ignore_all=0`
 		- `nano /etc/ufw/before.rules` add `-A ufw-before-input -p icmp --icmp-type echo-request –s 10.0.2.0/24 -m state --state ESTABLISHED -j ACCEPT`	
 
- You have also been asked to enable logging, at level high/info. 
	- `Solution: ufw logging high`


### Deliverables

- You are expected to submit a screenshot of your name, followed by the results of running `ufw status verbose` in your Linux terminal window. 
![images/verbose.png](images/verbose.png)
