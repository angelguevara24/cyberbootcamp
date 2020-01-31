# Loud Pipes
In this exercise, you'll use `||` and `&` to bypass a simple user-input filter.

---

## Instructions
- Click **Command Injection** in the left navigation bar, and make sure your security level is set to **medium**.

- Use the `||` to:
  - Check the installed version of Perl
  - List running network services (`netstat`)
  - Create a file, then check if it was created

- Launch Burp Suite. Send an IP address through the form; intercept the request; and send it to Repeater.

- Use Repeater and the `&` operator to:
  - List the contents of `/etc`
  - List the contents of `/home`
  - Print the commands you can run with `sudo` (`sudo -L`)
  - Remember that you must encode spaces, plus signs, and ampersands in the URLs! You can use Google or the **Burp Decoder** tab for this.

- Repeat the above exercise with Intruder, but redirect ping's output to `/dev/null`. 
  - How do the responses differ? 
