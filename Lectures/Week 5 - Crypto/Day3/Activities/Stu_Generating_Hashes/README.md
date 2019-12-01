# Generating Hashes on the Command Line

## Instructions

- Begin by using `md5sum` and `sha256sum` to generate the hash of a simple string, such as `"this is an example"`.
  - Remember to use I/O redirection to convert a command-line argument to standard input.
    - What difference do you notice between the MD5 and SHA256 sums?

- Inspect the private key in `id_rsa` with `cat`. 

- Generate the SHA256 hash of this file, and save it to a file, called e.g. `private_key_hash`.

- Use GPG to sign the file containing the hash with a detached signature.

- Send your seat partner the file containing the hash, as well as its signature and the private key.
    - **Bonus**: Create and send a tarball containing both files.

- Verify your partner's signature.

- Finally, check the hash of the file using `sha256sum`.

- Open the `id_rsa` file you received from your partner, and change one of the letters in the file. Try to verify the checksum. What happens?

## Questions

Signing checksum files is a common use case for GPG. Take a look at the Ubuntu downloads page: <http://releases.ubuntu.com/18.04/>

Note the `MD5SUMS` and `SHA256` sums files. 

- What security value does a signature add beyond that furnished by the checksum?

- Why is it particularly important to verify the integrity of images used to install operating systems?
