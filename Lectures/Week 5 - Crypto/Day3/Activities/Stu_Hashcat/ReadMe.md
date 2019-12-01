# Cracking Hashcat

  
## Instructions 

- In this exercise, you have been given the three following files:
  - `1.txt`
  - `2.txt`
  - `3.txt`

- You will be completing this activity within Kali Linux
- Your first objective is to identify what is the hash used for each file
- Once the Hash type is identified, update the 3 file names to reflect the hash type
  - For example:  If `3.txt` was determined to be using sha256, then `3.txt` would be renamed to `sha256.txt`
- Design the hashcat script with the correct flags  
- Run the script to figure out the password  


## Hints

Use the following hints to determine the hash type:
- `1.txt`: Bitcoin uses this hashing algorithm.
- `2.txt`: Windows uses this to hash its passwords.
- `3.txt`: Github uses this hash for committing items.

## Reference

The following site is a _fantastic_ resource for Hashcat's command-line flags. Refer to this once you've determined which hash algorithm corresponds to each password file.

Link: <https://hashcat.net/wiki/doku.php?id=example_hashes>
