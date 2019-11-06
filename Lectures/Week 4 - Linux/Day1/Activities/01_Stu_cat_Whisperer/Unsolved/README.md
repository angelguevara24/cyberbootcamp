# Cat Whisperer
## Instructions
Start by returning to the same Virtual Machine. 

- Run the command `cat < /etc/passwd`.
  - What do you see?
  - How is this different from `cat /etc/passwd`?
  - Rewrite this command using the file descriptor for `stdin`.

- Next, run: `cat << EOF`
  - After entering this command, you will get a prompt because the `cat` program is now waiting for your input.
  - Enter a few lines of text, hitting the return key each time.
  - After a few lines of text, type `EOF` and hit return. What happens?
  - Explain what you think `EOF` means.

### Bonus
- Run: `cat << EOF > my_file.txt`
  - How is this different from just `cat << EOF`?
  - Describe in detail what will happen when you complete this command.
