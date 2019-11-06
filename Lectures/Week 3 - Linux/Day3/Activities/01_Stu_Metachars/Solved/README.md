# Exploring Metacharacters
## Instructions
### Metacharacters
#### Pipe
- List the contents of `/usr/bin`. Use the pipe to count how many files it contains with `wc -l`.
> **Solution**: `ls /usr/bin | wc -l`

- Use `ps aux` to print running processes. Pipe to `grep` to find out the string `bash`. Pipe the output from `grep` to `wc -l` to count how many shells are running.
> **Solution**: `ps aux | grep bash | wc -l`

#### Escaping
- Create a directory called "My Files".
> **Solution**: `mkdir "My Files"`


- Use `touch` to create a file inside of `"My Files"`.
> **Solution**: `touch "My Files"/example.txt`

- Use `ls` to list files inside of `"My Files"`, but do _not_ use quotes in the directory name.
> **Solution**: `ls My\ Files`

#### Wildcards
- Use the `*` to find out how many programs in `/usr/bin` start with the letter `a`.
  - What about with the letters `b`, `s`, and `q`?
  > **Solution**: `ls /usr/bin/a* | wc -l`. For the others, run, e.g., `ls /usr/bin/b* | wc -l`, etc.

- Use `find` and the `*` to find all files that end with `.png` inside of your `~/Documents` directory.
> **Solution**: `find ~/Documents -type f -iname '*.png'`
  
