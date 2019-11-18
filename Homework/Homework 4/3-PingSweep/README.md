# Ping Sweep
## Instructions
- Create a variable, called `PREFIX`, and set it equal to the script's first argument.
  - **Note**: Expect users to pass an argument like `192.168.1`—_not_ a full IP address.

- Print the message: `Scanning $PREFIX.0/24...`

- Use `seq` to write a loop that prints every number between 1 and 5.
 
- Update your loop to use `PREFIX` and the number from `seq` to print out IP addresses. For example, if `PREFIX="192.168.1"`, your loop should print `192.168.1.1`; `192.168.1.2`; etc.
  - **Hint**: You can use multiple variables in a string, as in `echo "$FIRST_VARIABLE $SECOND_VARIABLE`.

- Inside your loop, create a variable called `TARGET`. Set it equal to the IP address you created above.
  - **Hint**: Replace `echo` with `TARGET=`.

- Finally, update your loop to `ping` the `TARGET` _once_. Use the `-c` flag. When it works as expected, update your `seq` statement to generate numbers up to 255.

## Challenges
- **Challenge 1**: Redirect the output of `ping` to `/dev/null`. Then:
  - If the ping is successful, print: `$TARGET is UP`
  - If the ping is _not_ successful, print: `$TARGET is DOWN`
  - **Hint**: You can "chain" operators, like: `cat nonexistent_file && echo "File exists!" || echo "File does not exist :("`

- **Challenge 2**
  - Redirect the `$TARGET is UP` message to a file called `live_hosts`. Be sure to _append_ to the file with `>>` instead of using `>` (why?).
  - Redirect the `$TARGET is DOWN` message to a file called `down_hosts`.
  - Print the contents of each file after the loop completes.
