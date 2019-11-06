# File Permissions

This activity will give you an opportunity to practice inspecting and setting file permissions.

You'll use the same VM you used in the previous class.

**Good luck!**

## Instructions

### Setting File Permissions

- Inspect the permissions on the following files and directories:
  - `/etc/shadow`
  - `/etc/passwd`
  - `~/.bashrc`
  - The directories in `/home`
  - Be sure to record the file permissions for these files.

- Next, create two new directories in your `~/Documents`, called `GroupFAQs` and `PrivateData`.

- In `PrivateData`, create three new files. Use any names you'd like.
  - Restrict "group" and "other" access to these files.

- In `GroupFAQs`, create three new files. Use any names you'd like.
  - Grant "group" read access (but not write or execute), and restrict "other" access to these files.

- Change back to `~/Documents`. Update the permissions for files in `GroupFAQs` such that they have "group" read _and_ write access.
