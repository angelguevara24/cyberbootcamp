# Warm-Up

## Instructions

### General Review

- Define the following terms, and give an example of each.
  - **Block Cipher**
  - **Stream Cipher**

- How does block size affect the strength of a cipher?

- How does key size affect the strength of a cipher?

- Define the following terms.
  - **Asymmetric Cryptography**
  - **Public Key**
  - **Private Key**
  - **Digital Signature**
  - **Digital Certificate**

- What should an individual do in the event they lose a private key?

### Encryption with GPG

- Create a file called `~/.secrets/passwords`. Add a line like: `Facebook fakePassword`.

- Use GPG to encrypt your passwords file.
  - **Hint**: Don't use asymmetric encryption (why?), and use your Day 2 Cheat Sheet.

- Use GPG to decrypt your passwords file, but _do not_ save the output to a file.
  - How could you use command-line tools to look for a particular password?

### Digital Signatures

- Next, sign your passwords file with a detached signature. 
  - Does this afford any advantage over simple encryption?

### Certificates and CAs

Refer to the following link when answering the questions below: <https://docs.microsoft.com/en-us/windows/desktop/seccertenroll/about-certificate-hierarchy>

- What is the motivation for designing a certificate hierarchy?

- Define **certificate chain**.

- Which steps are taken to verify each link in the certificate chain?

- What is special about the root certificate?

