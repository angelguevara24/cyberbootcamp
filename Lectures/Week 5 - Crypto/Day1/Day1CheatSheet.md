# Day 1 Cheat Sheet - Unit-Cryptography

## Key Terms

- **Plaintext**: The "raw", readable text of a message.
  - **Example**: `"Troops: Attack at dawn!"`

- **Ciphertext**: The encrypted (transformed, "gibberish") version of a message.
  - **Example**: `"asf87: -?*(1@^sz!jjx..."`, an encrypted version of the above plaintxt message.

- **Code**: Any method for concealing the contents of a message.
  - **Example**: Cartels often use slang terms to refer to contraband they're shipping, e.g.: "The grass is in the trunk," where "grass" might be a code word.

- **Cryptography**: The art and science of writing effective codes.

- **Cipher**: A set of rules for transforming a plaintext into a ciphertext, and back again.
  - **Example**: Pig Latin is a simple (and useless) cipher. It turns the plaintext "This is a message" into "Histay Isay Ay Essagemay" by moving the first consonant of each word to the end, and adding `-ay` after that.

- **Encryption**: The process of applying a cipher to a plaintext to generate an encrypted message.
  - **Example**: Generating "Histay Isay Ay Essagemay" using the Pig Latin transformation rules is an example of encryption.

- **Decryption**: The process of applying a cipher in reverse to recover plaintext from a given ciphertext.

- **Encryption Key**: A special value used to turn a plaintext into a ciphertext.
  - **Example**: We can turn the phrase "Hello" into "Ifmmp" by turning "H" into "I"; "e" into "f"; etc. In other words, we replace each letter with the next letter in the alphabet. In this case, the "key" is 1—we turn each letter of the plaintext into a letter of the ciphertext by replacing it with the letter _one_ space ahead in the alphabet.

- **Symmetric-Key Cryptography**: A method for encryption that uses the same key for encryption and decryption.
  - **Example**: Turning "Hello" into "Ifmmp" is an example of symmetric key cryptography.

- **Asymmetric-Key Cryptography**: A method for encryption that uses _different_ keys for encryption and decryption.
  - **Example**: No example was necessary for this definition, as we'll study it later. The takeaway is that symmetric methods aren't the _only_ methods.

- **Hash Signature**: A "fingerprint" of a file. In other words: A short value generated from a file, that is unique to the file.
  - **Example**: The hash signature of "Hello there" is: `e8ea7a8d1e93e8764a84a0f3df4644de`. The hash signature of "Hello there!" is: `a77b55332699835c035957df17630d28`. Even though the messages are similar, their hash signatures/"fingerprints" are completely different.

## Key Commands

### OpenSSL

#### Generating a Key and IV 

To generate a key and IV with OpenSSL:

```bash
openssl enc -nosalt -aes-256-cbc -k <your password here> -P
```

- `-nosalt` prevents OpenSSL from using a salt value
- `-aes-256-cbc` says to use 256-bit AES in CBC mode.
- `-k` allows you to specify your password on the command line.
- `-P` tells OpenSSL to print your key and IV to the command line.

#### Encrypting and Decrypting with OpenSSL

To encrypt:

  ```bash
  openssl enc -nosalt -aes-256-cbc -in <File to Encrypt> -out <Encrypted File> -base64 -K <key> -iv <iv>
  ```

To decrypt, simply add a `-d` flag and pass the encrypted file to `-in`:

  ```bash
  openssl enc -nosalt -aes-256-cbc -d -in <Encrypted File> -base64 -K <key> -iv <iv>
  ```

- `-base64` tells OpenSSL to use Base64 encoding when printing the encrypted output. This prevents your encrypted output from having non-printable characters in it.

### Python Functions

#### Reading Raw Bytes

To read a file as "raw bytes" (e.g., raw 1s and 0s), pass `"rb"` as the mode to `open` files with.

```python
filepath = "./my/binary/file"
with open(filepath, "rb") as file:
    contents = file.read()
```

Working with raw bytes makes it easier to work with hashes.

#### Hashing Files

To get a file's hash signature, we need to use Python's `hashlib` module.

```python
import hashlib

# Text to hash
# The `b` prefix makes this raw data instead of a normal string--not an important detail for now!
text = b"This is my sample text!"

# Hashing the data
sha256 = hashlib.sha256()
sha256.update(text)
hashed = sha256.hexdigest()
```

#### Checking if a File is a File

To check that a filepath represents a file and not a directory, use `os.path.isfile`.

```python
import os

path_to_file = "./MyFavoriteThings.txt"
path_to_directory = "./Pictures"

if os.path.isfile(path_to_file):
    print("This will print!")

if os.path.isfile(path_to_directory):
    print("This will not print!")
```
