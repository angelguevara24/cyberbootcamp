# Scanning with commix
In this exercise, you'll
- Use commix to exploit DVWA
- Study new injection payloads
- Explore commix's built-in "pseudo terminal"

---

## Prework

Before getting started, install `commix` by running the following commands:

```bash
  $ git clone https://github.com/commixproject/commix.git commix
  $ cd commix
  $ python commix.py --help
```

Please also set your DVWA security on low.

## Instructions
- Use commix to attack the command injection page.
  - Remember to specify a `--data` attribute.
  - Remember to specify a `--cookie` attribute.

- When commix identifies a successful payload, record it, and press `n` to proceed to the next one. Record 5 payloads before proceeding. **Note**: If you get dropped into a pseudo-shell automatically, simply type `back`.
  - **Payload 1**: `;echo FZYIQV$((55+15))$(echo FZYIQV)FZYIQV`
  - **Payload 2**: `;echo DZSRFQ$((18+71))$(echo DZSRFQ)DZSRFQ`
  - **Payload 3**: `%3Becho JCDNWJ$((56+32))$(echo JCDNWJ)JCDNWJ`
  - **Payload 4**: `%26echo GTAKDM$((92+10))$(echo GTAKDM)GTAKDM`
  - **Payload 5**: `|echo GLOILL$((10+65))$(echo GLOILL)GLOILL`

- For each of the payloads above, identify which character enables the injection.
  - **Hints** 
    - Look at the first character of each payload. You'll see a pattern.
    - Use **Burp Decoder**.

- Proceed to the next payload, and press `Y` when prompted to enter a pseudo-terminal.

- Press `?` to list available options. Work with a partner to research the last two options. Record definitions for each below.
  - **reverse_tcp**:
  - **bind_tcp**:

- Refer to the documentation at: <https://github.com/commixproject/commix/wiki/Reverse-Shells>
  - What does the reverse TCP handler allow you to do?

- As a **bonus**, repeat the exercise for security **medium** and/or **high**.
