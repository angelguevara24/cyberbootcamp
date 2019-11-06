# Breaking the Chain
## Instructions
### Drills
For this exercise, you'll use `&&`, `||`, and `;` to chain commands.
- Use `;` and `echo` to print: `First Message` and `Second Message`
- Use `&&` to create a directory _and then_ move into it.
- Run `cat nonexistent`. You should get an error. Use `||` to print: `"File not found :("` after trying to read `nonexistent`.
- Determine what the following commands will print:
  - `cat /etc/shade && echo "Shadow file dumped."`
  - `ping -c 3 target.com && echo "Target is up!" || echo "Target is down..."`
  - `ping -c 3 down.ste && echo "Target is up!" || echo "Target is down..."`

### Success vs Error

* Run the command `ls /etc ; echo ' ' ; ls /dev`
    * You should see the output of each command. The echo command just adds some space between the two outputs.

* Now run the command `ls /etc && echo ' ' && ls /dev`
    * How is this different from the running the first command?
    * Is this what you expected to happen?
    * What happens if you change the command to: `ls none && echo ' ' && ls /dev`?
        * After running `ls /etc && echo ' ' && ls /dev` did you get the output you expected?

* Finally, let's look at `ls /etc || echo ' ' || ls /dev`
  * What do you expect the output of this command to be?

  * After running this command, did you get the output you expected?

  * What should happen if we change this command to: `ls none || echo ' ' || ls /dev`

