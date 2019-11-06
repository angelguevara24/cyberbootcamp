# Review
## Instructions
### Command Expansion
`which <command>` prints the absolute path to `<command>`. 

For example, `which ls` reports that the command `ls` is in the file `/usr/bin/ls`.

  ```bash
  $ which ls
  /usr/bin/ls
  ```
The `file <Target>` command tells you what kind of file `<Target>` is. For example, `file Notes.txt` tells you that `Notes.txt` is a text file.

- Use `file` and a command expansion to find out what kind of file `cat` is.
- What does `LS_PATH=$(which ls)` do?
  - **Note**: Feel free to run this in your Terminal to find out! Try running `echo $LS_PATH` after setting the variable.

---

`dirname <File Path>`  gives you the directory a file lives in. See the snippet below for examples.

  ```bash
  $ dirname /usr/bin/ls
  /usr/bin
  ```

- Use `dirname` and a command expansion with `which` to print the name of the directory that `file` lives in.
- **Bonus**: Update the above command to `cd` into the directory that `file` lives in. You'll need two command expansions!

### Redirection
Consider the command: `cat nonexistent_file 2> /dev/null`
- What will print to the Terminal? Why?

Consider the command: `cat nonexistent_file > /dev/null`
- What will print to the Terminal? Why?

Consider the command: `cat /etc/passwd > /dev/null`. Assume `/etc/passwd` exists!
- What will print to the Terminal? Why?
