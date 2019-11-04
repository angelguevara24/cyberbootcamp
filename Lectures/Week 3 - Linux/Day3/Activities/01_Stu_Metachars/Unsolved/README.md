# Exploring Metacharacters
## Instructions
### Metacharacters
#### Pipe
- List the contents of `/usr/bin`. Use the pipe to count how many files it contains with `wc -l`.

- Use `ps aux` to print running processes. Pipe to `grep` to find out the string `bash`. Pipe the output from `grep` to `wc -l` to count how many shells are running.
  - **Note*: You'll need two pipes for this.

#### Escaping
- Create a directory called "My Files".
  - **Note**: Pass `"My Files"` in quotes. 

- Use `touch` to create a file inside of `"My Files"`.

- Use `ls` to list files inside of `"My Files"`, but do _not_ use quotes in the directory name.
  - **Hint**: This is where you'll need the backslash.

#### Wildcards
- Use the `*` to find out how many programs in `/usr/bin` start with the letter `a`.
  - What about with the letters `b`, `s`, and `q`?

- Use `find` and the `*` to find all files that end with `.png` inside of your `~/Documents` directory.
  - **Hint**: Use the `-iname` option. Use a `*` inside of the string you pass to `iname`.
