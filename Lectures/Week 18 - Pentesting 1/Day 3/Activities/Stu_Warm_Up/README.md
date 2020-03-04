## Student Activity: Warm-Up
In this exercise, you'll learn some advanced Nmap scanning techniques and review Shellshock.

Please launch the **Linux Exploitation** lab and follow the instructions below.

### Instructions

#### Nmap

- Use Nmap to perform a ping sweep of your subnet. Save the results as XML.

- Store the IP addresses Nmap discovers in a file called `live_hosts`.
  - You'll have to copy them by hand. As a bonus, you can do this in bash with `awk` and `head`.

- Run an "aggressive" scan of the top 100 ports against the hosts on the list.
  
  **Hint**: You'll need `--top-ports`. Refer to the Nmap documentation for how to perform an aggressive scan: <https://nmap.org/book/man-performance.html>

- Repeat the scan above on just one of the hosts on the network. This time, turn off host discovery and name resolution to reduce the amount of traffic you send.

#### Shellshock
- What kind of vulnerability is Shellshock? What does it allow attackers to do?

- Which headers can be used to deliver a Shellshock payload? Give an example of how one of these headers might look in a malicious request.
