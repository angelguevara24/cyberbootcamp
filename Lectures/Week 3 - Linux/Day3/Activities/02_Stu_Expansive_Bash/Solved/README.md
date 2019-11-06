# Expansive Bash
## Instructions

* Create a variable called `NAME`, and store your name in it. and name it whatever you want.
  * **Hint**: use the VAR=VALUE syntax.
  > **Solution**: `NAME="Jeremy"`

  * Use `echo` to print the value of your variable to the screen.
  > **Solution**: `echo $NAME`

* Use `echo` to print the full path to your home directory.
  * **Hint**: Remember that the `~` character can be expanded...
  * Note that this makes writing paths to your folders much quicker and easier.
  > **Solution**: `echo ~`

* Use `echo` with a wildcard to print out the names of everything in the current directory.
  > **Solution**: `echo *`

* Use `ls` with a wildcard to print every file in the current directory.
  > **Solution**: `ls *`

* Run: `file --help`. What does the `file` command do?
  > **Solution**: `file <FILENAME>` tells you the file type of `<FILENAME>`.

- Run: `man which`. What does the `which` command do?
  > **Solution**: `which <COMMAND>` tells you the absolute path to the executable for `<COMMAND>`.

- Use `file` and a command expansion with `which` to figure out what kind of file `ls` and `cp` are.
  - **Hint**: You'll need something like `$(which ...)` in your solution...
  > **Solution**: `file $(which ls)` and `file $(which cp)`.

## Extension
* When you open another shell, any variables you created are reset.

  * Use your Google-Fu to determine how you can create a variable that persists across 'shells'.
  * **Hint**: `export`
  > **Solution**: You can use the `export VAR=VALUE` syntax, as in: `export PATH=$PATH:$(pwd)`.
