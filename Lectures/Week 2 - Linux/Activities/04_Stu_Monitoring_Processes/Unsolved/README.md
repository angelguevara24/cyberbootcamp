# Monitoring Processes
In this exercise, you will:
- Use `top` to monitor processes
- Use `kill` to stop processes
- Research signal flags used with the `kill` command

Make sure you are logged into your Ubuntu VM and follow the instructions below.

## Instructions
- Start by listing processes with `top`, and answer the questions below.
  - How many tasks have been started on the host?
  - How many of these are sleeping?
  - Which one is running?
  - Which process uses the most memory? Why?

- Press `q` to close `top`.

- Use `ps`, with flags, to list _all_ processes running on the host.
  - Which processes are running as `root`?
  - Pick out a few processes run as root and determine what do these processes do?

- Run the command `tail -f /dev/null &` to start a `tail` process. This process just follows a file to see if there are any changes made to it.  
- Now, find that process and it's process ID and kill it.
- Verify that the process is stopped.

## Extension
Linux has several ways to close programs, depending on exactly what caused it to close.

Programs close in different ways based on the **signals** they receive from the operating system.

Read about important signals at the following links:
- [SIGHUP](https://en.wikipedia.org/wiki/SIGHUP)
- [SIGTERM](https://en.wikipedia.org/wiki/Signal_(IPC)#SIGTERM)
- [SIGKILL](https://en.wikipedia.org/wiki/Signal_(IPC)#SIGKILL)

You can use the `-s` flag to send a specific signal with `kill`, e.g.: `kill -s SIGTERM 107`.

Why is sending a SIGKILL signal "dangerous"?
