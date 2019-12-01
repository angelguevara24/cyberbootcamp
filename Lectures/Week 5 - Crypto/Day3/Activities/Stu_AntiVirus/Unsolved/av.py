# Package imports
import hashlib
import os

# TODO: Get paths to malware sample and directory to scan

# TODO: Generate hash signature for malware

# TODO: Loop over filenames in `directory` using `os.listdir`
    # TODO: Create filepath: directory + "/" + filename

    # TODO: Check filepath is a file, not a directory, using `os.path.isfile`
        # TODO: Open `filepath` in "rb" mode
            # TODO: Hash file

            # TODO: Compare malware_hash to hash of file
