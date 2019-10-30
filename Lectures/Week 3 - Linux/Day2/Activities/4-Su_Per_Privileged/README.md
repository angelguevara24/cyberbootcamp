# Su-per Privileged

In this activity, you'll get a chance to crack user passwords, and then use `su` to run files you ordinarily don't have access to.

- Identify users who are members of `hackers`

- Find the backup of `/etc/shadow` with "other" read permissions saved in one of their home folders.

- Copy backed-up `shadow` and remove all members who are not `hackers`

- Use `john` to crack passwords in `shadow`

- Use `su` to assume identity of another user

## Instructions

### Cracking Passwords

- What happens when you try to read `/etc/shadow`? Why does this happen?

- An administrator left a copy of `/etc/shadow` in one of the tmp directories. Find it.

- Create a new folder in your `Documents` directory, called `.hidden`, and change into it.

- Move the copied `shadow` file you found into `.hidden`, and change into `.hidden`.

- There's a program called `john-the-ripper` on your VM. Run it, and pass the shadow file as argument.

- What do you see when `john` finishes running? Record your response.

### Finding the Flag

- One of the users has a "flag" file somewhere in their home directory that is executable.
- Find out who, and what the path to the file is.

- Use the passwords you just cracked to login as the user who owns the flag.

- Move into the directory you found, and run the flag file.

- If all goes well, you should get a message verifying that you have found the flag!
