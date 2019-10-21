# Linux Landmarks

In the previous exercise, you found files in a variety of different directories, such as `/home` and `/var/log`.

These are important directories on Linux systems. In this activity, you'll have an opportunity to explore these and other important locations on the file system.

## Instructions

- Move to the `/` directory, and run `ls`.
  - What's the purpose of this directory?
  - What does this directory contain?

- Move to `/etc`, and list the files it contains.
  - Use `cat` to read `/etc/passwd`.
  - `sudo cat` to read `/etc/shadow`.
  - Read `/etc/hosts`. What does this file contain? Refer to the reading if you're stuck.

- Move to `/bin`, and list the files it contains.

- Move to `/usr/bin`, and list the files it contains.
  - Look closely at the contents of these directories, specifically at the files beginning with the letters `l`, `c`, and `t`. Do you notice anything familiar?

- Move to `/var`, and list the directories it contains.
  - Some of these will be unfamiliar, but what do you think the following contain?
    - `/var/backups`:
    - `/var/tmp`:
    - `/var/log`:

- Return to `/home`. What does this directory contain?

- Move to `/tmp`. What kind of data do you think this directory contains?

## Questions

- Read the following document before working through the questions below: <http://linuxcommand.org/lc3_lts0040.php>

- What kinds of files does `/` contain?

- What kinds of files does `/etc` contain?

- What kinds of files does `/var` contain?

- What's the difference between `/tmp` and `/var/tmp`?

- What kinds of files do `/bin`, `/usr/bin`, and `/usr/sbin` contain?

- What kinds of files does `/home` contain?

- Suppose you're looking for a program called `usermod`. Which directories would you look in first?

- You've been told to find a configuration file called `fstag`. Which directory should you look in?

- An investigator tipped you that `hera` is also a malicious user. What's the first directory you'd look in to examine the files she's saved on the system?

- Which file would you read to get a list of all the users on the system?

- Which file would you read to get all users' hashed passwords?

- Suppose you've compromised a target machine, and you want to write a custom exploit while you're there. Which directory would you save it in to best cover your tracks?
  - Hint: Which directory's contents are automatically deleted on reboot?
