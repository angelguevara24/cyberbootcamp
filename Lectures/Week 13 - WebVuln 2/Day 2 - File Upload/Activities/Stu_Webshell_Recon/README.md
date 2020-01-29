# Webshell Recon
For this exercise, you'll perform some recon on the server you compromised in the previous class.

Use Firefox to navigate to DVWA. 

Then, follow the instructions below.
 
## Instructions

- Upload [webshell.php](webshell.php) to the server.

- Launch Burp Suite, and intercept a request the URL where `webshell.php` was uploaded.

- Send the request to Intruder. Set a position around the command in the request, and send payloads that will dump the following information:
  - The current user ID and group ID
  - A list of running processes running as root
  - The contents of `/etc/passwd`
  - Check if the following network tools are installed:
    - `nc`
    - `ncat`
    - `socat`
    - `curl`
    - `wget`
    - **Hint**: To check if a tool exists, check for its version with, e.g.: `nc --version`.

- Read the following Server Fault thread: <https://serverfault.com/questions/519215/what-is-the-difference-between-sbin-nologin-and-bin-false>
