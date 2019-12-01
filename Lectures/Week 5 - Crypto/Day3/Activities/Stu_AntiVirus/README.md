# Hash Magic

In this activity, you will use hash signatures in a Python script to create a antivirus scanner that will scan a directory for a given piece of malware.

You'll need to:
- Get the path to the malware sample to look for
- Get the path to a directory to scan for the malware
- Generate a hash signature for the malware, to compare to that of each file in the target directory
- Loop over all the files in the target directory
- Check that each file is actually a _file_, and not a directory 
- If so, generate the SHA256 hash of each file
- Compare this hash to that of the malware

## Instructions

Depending on your comfort with Python, you may:
- Create a new file, and start from scratch
- Use the commented starter file in `Unsolved/av.py`
- Use the scaffolded starter file in `Unsolved/av_scaffolded.py`.
  - The scaffold provides the code for collecting filepaths and generating a hash of the malware sample.

To be clear, this activity does _not_ use involve real malware, for obvious security reasons. Instead, you'll be testing it with the program `ls.exe`, which you've used on the command line. 

The principles at work remain identical, however, and your solution would be fully functional for identifying real malicious binaries.

To test `av.py`, pass the following paths for the malware and target directory, respectively:
- **"Malware"**: `../Resources/ls.exe`
- **Target Directory**
  - **Windows**: `C:/Program Files/Git/usr/bin`
  - **Mac**: `/usr/bin`

**Note**: Make sure you pass the correct path to the "malware". I.e., if your `av.py` lives in the same directory as `ls.exe`, pass `.` as the malware path.

This activity requires the new tools you learned in lecture. Look to your Cheat Sheet for reference.
