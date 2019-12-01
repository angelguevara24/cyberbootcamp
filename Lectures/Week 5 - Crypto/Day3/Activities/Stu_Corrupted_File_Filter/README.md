# Hash Magic

In this activity, you will use hash signatures in a Python script to:
- Select an uncorrupted file from a group of corrupted variants using the original file's SHA256 hash

You'll need to:
- Hard-code the SHA256 hash of `Resources/ZimmermanOriginal.txt` in a variable called `hash`
- Get a relative path to the directory to search from the user
- List all files in the target directory
- Open each file in `"rb"` mode
- Read and hash the contents
- Compare this hash to the hash of `Resources/ZimmermanOriginal.txt`
- Print a message if the document is found

## Instructions

Depending on your comfort with Python, you may:
- Create a new file, and start from scratch
- Use the commented starter file in `Unsolved/haystack.py`
- Use the scaffolded starter file in `Unsolved/haystack_scaffolded.py`.
  - The scaffolded version contains the code for looping through every file in a directory.

To test your solution, run the solution you write in `Unsolved/haystack.py` script with the path: `../Resources`. You should identify `Zimmerman3.txt` as the original file.

This activity requires the new tools you learned in lecture. Look to your Cheat Sheet for reference.
