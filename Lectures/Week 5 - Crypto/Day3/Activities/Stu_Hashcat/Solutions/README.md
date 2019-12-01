# Cracking Hashcat

In this exercise, you have been given the three following files:
- `1.txt`
- `2.txt`
- `3.txt`

Your objective is to identify which hash each is, then identify the correct Hashcat flags to discover the password. 

## Solutions

Use the following commands to crack each file.
- To crack `1.txt`, use: `hashcat -m 1400 -a 0 -o solved.txt sha256.txt /usr/share/wordlists/rockyou.txt --force`
- To crack `2.txt`, use: `hashcat -m 1000 -a 0 -o solved.txt ntlm.txt /usr/share/wordlists/rockyou.txt --force`
- To crack `3.txt`, use: `hashcat -m 100 -a 0 -o solved.txt sha1.txt /usr/share/wordlists/rockyou.txt --force`
