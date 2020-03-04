## Student Activity: Attacking Shellshock

In this exercise, you'll use Metasploit to automate the exploitation you just performed manually with Burp Suite.

#### Instructions

- Launch the **Linux Exploitation** lab.

- Complete **Part 7: Exploit Shellshock with Metasploit**

- Scan your subnet for live hosts. Identify the host(s) running an Apache HTTP server.

- Use Metasploit to search for Metasploit modules related to Shellshock.

- Use Metasploit to scan live hosts for the Shellshock vulnerability.

    **Hint**: Check the `/cgi-bin/status.cgi` endpoint URI. Look for an `auxiliary` module.

- Attempt to exploit the server with the modules related to Apache. Record which one works.
