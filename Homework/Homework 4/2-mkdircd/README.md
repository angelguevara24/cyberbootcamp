# mkdircd
In this exercise, you'll write a script that:
- Creates a directory, with a name provided by the user
- Moves into that directory
- Creates a file in that directory, with a name provided by the user
- Opens the file in nano

Users will run it like:
  
  ```bash
  $ mkdircd Linux-Week-2 ClassNotes.txt
  ```

This command will create a directory called `Linux-Week-2`; create a file called `ClassNotes.txt` in `Linux-Week-2`; and open `ClassNotes.txt` in nano.

This exercise requires you to use positional parameters alongside everything you've already learned.

**Good luck!**

## Instructions
- Create a new directory, called `/usr/scripts`, and move into it.

- Create a script called `mkdircd`. Add the shebang line `#!/bin/bash`
  - **Note**: Remember that the shebang line must be the _first_ line in the file.

- Begin writing your script. It should:
  - Create a directory using the first positional parameter
  - Move into that directory
  - Create a file using the second positional parameter
  - Open this file with nano

- Give your script execution permissions.
  - **Hint**: `chmod`

 - Run `./mkdircd ExampleDirectory FirstFile` to test.
