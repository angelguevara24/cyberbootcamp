# Encrypting with GPG

In this activity, you'll use GNU Privacy Guard (GPG) to
- Generate a public/private keypair
- Generate a revocation certificate
- Encrypt and decrypt data

## Instructions

Create a new directory called `~/.gpg_keys/my_key` to store your work in. Be sure to move into it before beginning the exercise.

### Generating Keypairs

- Use GPG to generate an RSA keypair.

- Inspect your public keyring.

- Generate a revocation certificate. Store it in a file called `revoke.asc`.

- Export your public key with ASCII armor. Save it in a file called `your_name.gpg`, where `your_name` is, of course, your name.

- Send the `gpg` file to your seat partner in Slack.

- Upon receiving your partner's key, import it in your public keyring.

### Encryption/Decryption

- Create a file called `SecretFormula.YourName`, and write a top-secret message, which should include a number (any number will do).

- Encrypt the message with your partner's public key.

- Send the encrypted message to your partner.

- Upon receiving your partner's encrypted message, decrypt it, and verify that the number you decrypted is the number they included in the original message.

## Questions

- What is a revocation certificate?
