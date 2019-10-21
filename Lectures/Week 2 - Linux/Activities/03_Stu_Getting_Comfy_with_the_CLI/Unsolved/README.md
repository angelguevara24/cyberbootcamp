# Getting Comfy with the CLI

## Instructions

### Review

- Inside your VM, Move into your home directory, and then into your Documents folder.

- Create the following directories:
  - `Class_Notes`
  - `Class_Resources`

- Move into `Class_Notes`, and create a file called `Linux_Notes`.

- Create a folder called `12_Intro_to_Windows_and_Linux` in `Class_Notes`, and move `Linux_Notes` into this folder.

- Use `man rm`, and search for the `-i` flag. What does it do?

- Use `rm -i` to try to remove `Linux_Notes`, but choose _not_ to remove the file.

### Using Manpages

- Change back to your home directory, and list all the files.

- Run `ls --help | less`, and search for "all". Note the two flags you discover.

- List all files in your home directory. Write down the names of all the new files you see.

- Look at the first few lines of each of the new files.

  - Which can you read? What do you think each one does?

- Use the help page to find out how to use `ls` in "long listing format".
  - **Hint**: Run `ls --help | less`, then search for "long listing".

- Use the above two options together to list every file in your home directory, sorted according to the time they were last modified.

- Use the manpages to find out how to use `ls` to sort alphabetically.

- List every file in your home directory in alphabetical order, in long listing format.


## Bonus
- Suppose you want to use `cut` to chop up the following line in a file: `Jane;Doe;jane@gmail.com;24`. The fields contain her first and last name; email; and age, respectively.
  - Which delimiter should you use?
  - Which field do you specify if you want to get her first name?
  - Which field do you specify if you want to get her age?
  - Which field do you specify if you want to get her last name?
  - Which field do you specify if you want to get her email?
  - Which fields do you specify if you want to get her first _and_ last name?
