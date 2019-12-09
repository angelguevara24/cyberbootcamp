# Running Snort
In this exercise, you will:
- Launch Snort on your Linux machine
- Inspect the alerts and logs it generates
- Identify which rule(s) were triggered

## Instructions
### Starting Snort
- Begin by launching Snort in packet-capture mode. Be sure to enable verbose mode, and pass the correct path to `snort.conf`.

- Open a second terminal window and run `ping 8.8.8.8`

- Watch the packet capture to verify that you're logging traffic. Then, stop Snort with `Ctrl + C`.

- Run: `snort --help | less`. Find out what the `-q` flag does.

- Restart Snort, but pass the `-q` flag, and _not_ the `-v` flag. Note what happens. Then, stop Snort.

- Find out how to enable "full Alerts".
  - **Hint**: Refer to the Snort documentation at: <http://books.gigatux.nl/mirror/snortids/0596006616/snortids-CHP-3-SECT-3.html>

- Launch Snort in quiet mode with full alerts, and put it in the background with `&`. Run `jobs` or `ps -e | grep snort` to ensure that Snort is running.

- Move to `/var/log/snort`. Check how many lines are in `alert` twice in a row with `wc -l`. Wait a few seconds, then check again.
  - **Hint**: Use `wc -l`.

- Run: `head alert`. Which two alerts were logged when you first ran Snort?

- Run: `tail alert`. Which alert(s) was/were logged most recently?

- Which IP addresses did Snort log traffic to/from?

### Finding Rules
**Note**: The below is challenging.

- Move to `/etc/snort/rules`.

- Find out which rules fired the alerts in `/var/log/snort/alert`.
  - **Hint**: Use grep to search for the name/title of each alert in `community.rules`. E.g., use `grep` to look for `UNUSUAL PING`, `ICMP ECHO`, etc.
  - Write down the `sid` of each rule that pops up. You'll find this at the very end of the rule options, as in the sample rule below.

  ```bash
  # Random rule from `local.rules`
  alert tcp any 6667 -> any any (
    msg:"C&C Server sent port scan command";
    content:"!scan";
    sid:1000008;)
  ```
