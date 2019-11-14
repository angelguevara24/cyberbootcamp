# Public Key Cryptography

In this activity, you'll 
- Review the structure of asymmetric algorithms
- Study hybrid cryptosystems, which use symmetric and asymmetric algorithms together
- Research TLS, a common and crucial application of hybrid cryptosystems

## Instructions

- Alice wants to use her private key to decrypt a message from Bob. Draw a diagram describing this scenario.

- Recall that symmetric key algorithms are fast, but that exchanging the secret key is difficult to do securely. Asymmetric algorithms can be used to solve this problem.
  - Suppose Bob wants to send Alice a message encrypted with AES using a secret key. In order to decrypt it, Bob must send the secret key first.
  - How might Bob use his private key to send Alice his (symmetric) secret key? Draw a diagram depicting this scenario.
  - How does Bob get the original message (the one encrypted with AES) to Alice?
  - How does Alice decrypt the original message?

## Extension

- Read the article on TLS/SSL at: <https://www.ssl.com/article/ssl-tls-handshake-overview/>
  - **Note**: Note the graphic in particular.

- Define **cipher suite**.

- Define **pre-master key**.

- What is the role of the pre-master key?

- How are the pre-master key and the shared secret key similar? How are they different?

- Compare the TLS handshake to the hybrid process you outlined above. What are the key differences?
