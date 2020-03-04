## Student Activity: Scanning and Enumeration

Launch the **Linux Exploitation** lab instance, then complete **Part 3: Vulnerability Assessment and Research** located in CyberScore.

### Instructions

Launch the **Linux Exploitation** lab instance, then complete **Part 3: Vulnerability Assessment and Research** located in CyberScore.

- Start by using Nmap to perform host discovery on the range on the `10.0.0.0/24` subnet.

- Use Nmap to perform an intense scan on any host you discover.

- Test both machines for vulnerability to Shellshock.
  - **Hint**: Use the `uri` script argument to test `/cgi-bin`, `/cgi-bin/bin`, `/cgi-bin/status.cgi`, and any other common CGI script names you can enumerate.
  
- Identify Heartbleed in the scan results and use the Q & A section of the [Heartbleed website](http://heartbleed.com) to answer the following questions:

  - Why is it called the Heartbleed Bug?

  - What makes the Heartbleed Bug unique?

  - What is being leaked?

  - What is leaked primary key material and how to recover?

  - What is leaked secondary key material and how to recover?

  - What is leaked protected content and how to recover?

  - What is leaked collateral and how to recover?

  - What versions of the OpenSSL are affected?

  - How common are the vulnerable OpenSSL versions?
  
### References
- http://heartbleed.com/
