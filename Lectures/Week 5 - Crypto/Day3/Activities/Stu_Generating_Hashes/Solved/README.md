# Generating Hashes on the Command Line

## Instructions

- Begin by using `md5sum` and `sha256sum` to generate the hash of a simple string, such as `"this is an example"`.
  - **Solution**: `md5sum <<< "this is an example"` and `sha256 <<< "this is an example"`.
  - What difference do you notice between the MD5 and SHA256 sums?
    - **Solution**: SHA256 produces longer hashes.

- Inspect the private key in `id_rsa` with `cat`. 
  - **Solution**: `cat id_rsa`

- Generate the SHA256 hash of this file, and save it to a file, called e.g. `private_key_hash`.
    - **Solution**: `sha256sum id_rsa > private_key_hash`

- Use GPG to sign the file containing the hash with a detached signature.
    - **Solution**: `gpg --output private_key_hash.gpg --detach-sig private_key_hash`

- Send your seat partner the file containing the hash, as well as its signature.
    - **Bonus**: Create and send a tarball containing both files, and the private key.
        - **Solution**: `tar -cvf hashes.tar .` to create the archive; `tar -xvf hashes.tar` to extract.

- Verify your partner's signature.
    - **Solution**: `gpg --verify private_key_hash.gpg private_key_hash`

- Finally, check the hash of the file using `sha256sum`.
    - **Solution**: `sha256sum -c private_key_hash` 
    
- Open the `id_rsa` file you received from your partner, and change one of the letters in the file. Try to verify the checksum. What happens?
  - **Solution**: The file won't validate! Try catching that error with the naked eye...

## Questions

Signing checksum files is a common use case for GPG. Take a look at the Ubuntu downloads page: <http://releases.ubuntu.com/18.04/>

Note the `MD5SUMS` and `SHA256` sums files. 

- What security value does a signature add beyond that furnished by the checksum?
    - **Solution**: Verifying the signature ensures the integrity of the file containing the signatures.

- Why is it particularly important to verify the integrity of images used to install operating systems?
    - **Solution**: Certain files in operating system install images are critical—for example, the corruption of even a small portion of the kernel could break the image.
