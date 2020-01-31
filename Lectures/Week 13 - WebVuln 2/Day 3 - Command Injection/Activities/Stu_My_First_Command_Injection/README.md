# My First Command Injection
In this exercise, you'll use the semicolon operator to inject commands to a vulnerable server.

---


## Instructions
- Click the **Command Injection** vulnerability in the left navigation bar.

### Direct Injection
- Submit a valid IP address, such as `8.8.4.4` to see the form's normal behavior.

- Use the semicolon to inject commands that:
  - Dump the contents of `/etc/passwd`
  - Print the current username
  - Print the operating system and kernel version
  - Print all running processes

- Finally, change your injection to use a _bad_ IP address, such as `fake_ip`. How does the output change?

### Burp Repeater
- Enable Foxy Proxy, launch Burp Suite, and intercept a request through the IP address form.

- Send the request to Repeater. Update the IP address to use the same payloads you delivered previously.
  - Remember to encode spaces as `%20` or `+`.

- Inspect the **Response** tab to see the results.

### Burp Intruder
- Next, send the request to Intruder. Set a position around the command you're injecting. Then, use the three commands you sent previously as **Payloads**.

- Run the attack, and inspect the responses in the **Attack** pane.
