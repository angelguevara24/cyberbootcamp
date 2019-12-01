# Rainbow Tables

In this activity, you'll read about the function, purpose, and limitations of rainbow tables, at: <https://www.lifewire.com/rainbow-tables-your-passwords-worst-nightmare-2487288>

## Questions

- What are rainbow tables used for?
  - **Solution**: Rainbow tables are used to efficiently crack passwords.

- Define **rainbow table**.
  - **Solution**: A rainbow table is a table of precomputed hash values, which can be used to "invert" a hash function, thus allowing attackers to identify a valid password associated with a given hash. 

- Describe the "classical" method for password cracking—i.e., the technique employed prior to the development of rainbow tables.
  - **Solution**: The classical method for cracking password hashes was simply to brute-force hash every possible plaintext until one of them produced the hash being cracked. 

- Describe how rainbow tables crack passwords.
  - **Solution**: Rainbow tables accelerate password cracking by **pre-computing** hashes, so finding the correct password is as "simple" as looking up which password is associated with the given hash.

- What is the chief disadvantage to rainbow tables?
  - **Solution**: Rainbow tables require considerable storage—often on the order of terabytes worth. In addition, there's no guarantee that a rainbow table _will_ contain a password corresponding to the hash you're attempting to crack, even if it's large.

- Identify two defense mechanisms against rainbow tables.
  - **Solution**: One would be to use algorithms stronger than MD5 or SHA1. Another is to use a **cryptographic salt** when hashing data.

- Define **crypographic salt**.
  - **Solution**: A cryptographic salt is a piece of random data added along with a message as input, which makes the hash exponentially harder to break.

