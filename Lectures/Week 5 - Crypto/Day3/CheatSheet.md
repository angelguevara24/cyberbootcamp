# Cryptography Day 3 Cheat Sheet

## Command Line

### Generating Hashes 

To take the hash of a string: 

  ```bash
  # Generate MD5 hash
  md5sum <<< "Example!"
  sha256sum <<< "Example!"
  ```

To generate the hash of a file:

  ```bash
  sha256sum filename
  ```

To save the output of the above command to a checksum file to send with the file:

  ```bash
  sha256sum filename > hashes
  ```

### Verifying Hashes

First, ensure the following:
- The file whose integrity you want to verify is in the current directory
- A file containing the hash of this file and its filename, in the format output by `sha256sum` and `md5sum`, is also in the current directory

Then, run:

  ```bash
  # To verify MD5 hashes
  md5sum -c hashes

  # ...Or this, to verify SHA256 hashes
  sha256sum -c hashes
  ```

## Python

### Reading Raw Bytes

To read a file as "raw bytes" (e.g., raw 1s and 0s), pass `"rb"` as the mode to `open` files with.

```python
filepath = "./my/binary/file"
with open(filepath, "rb") as file:
    contents = file.read()
```

Working with raw bytes makes it easier to work with hashes.

### Hashing Files

To get a file's hash signature, we need to use Python's `hashlib` module, best understood by example.

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

**Heads-Up**: The three lines are the bottom are required _every_ time you want to create a hash signature—you cannot reuse the `sha256` object you create initially. Doing so is a common mistake.

This means that, if you need to hash files in a loop, you should have these all three of these lines _inside_ of the loop!

### Checking if a File is a File

Python will complain if you try to read a directory as a file...Fair enough.

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

You'll need to use `os.path.isfile` in your solution for [av.py](Unsolved/av.py).

### Hashcat

For a full reference, refer to the following documentation: <https://hashcat.net/wiki/doku.php?id=example_hashes>
