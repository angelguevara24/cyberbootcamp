# Symmetric vs Asymmetric

## Instructions

### Categorization

For each of the following scenarios, determine whether Symmetric or Asymmetric cryptography is more appropriate, and which of the four goals of cryptography is most relevant to the scenario

- You're sending the final version of a treaty to Parliament, and want everyone to know that _you_ are the one who sent it.

- You're sending a letter to your spouse, and don't want anyone else to be able to read it. Assume you've already shared whichever keys you'll need.

- You need to send a message and ensure that no one tampers with it while its in transit.

- You need to encrypt data before storing it in a database, but only have limited computational power, since you're building code for a mobile phone.

### Hybrid Cryptosystems

In order for a recipient to decode a message encrypted with a symmetric key, they must, of course, acquire the symmetric key. 

But, transmitting this key securely is a serious challenge.

Recall that, with asymmetric key algorithms, you use a public key to encrypt data, and a private key to decrypt it.

Consider the following:
- You have a public key, which you share with anyone who wants to send you encrypted messages.
- You have a private key, which you can use to decrypt messages encrypted with your public key.
- Your partner has a symmetric key, which they'll use to encrypt any messages they send you.

How can you use asymmetric cryptography to safely transmit the symmetric key?
