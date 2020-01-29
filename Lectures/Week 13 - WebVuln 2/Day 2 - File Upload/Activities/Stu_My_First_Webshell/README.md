# My First Webshell
In this exercise, you will:
- Examine the form and function of a PHP webshell
- Upload a webshell to a vulnerable server
- Use Burp Suite to perform reconnaissance against the compromised host

## Instructions
### First Steps with Webshells
You do **_not_** need to know PHP to assess web applications. However, it's very useful to be familiar with:
- How PHP is inserted into web pages
- How user data is extracted from an HTTP request
- How PHP runs shell commands from server-side scripts

Understanding these concepts will prepare you for later work in web pentesting, which often requires that you modify existing PHP payloads to suit your specific needs.

Open [webshell.php](webshell.php), then answer the questions below.

---
- Look at the beginning/end of the file. How do you start/end a PHP script?

- What does the variable `$_GET` refer to?

- Consider the URL: `https://example.com?parameter=value`. 
  - How would you get the value of `param` in PHP?

- Consider the following POST body: `username=hacker&password=null`
  - How would you get the value of `username` in PHP? What about `password`?

### Uploading and Exploiting a Webshell
Use **Firefox** to navigate to `http://localhost/vulnerabilities/upload/` 

Then, follow the instructions below.

---

- Upload `webshell.php` to DVWA.

- Launch Burp Suite, and enable Foxy Proxy.

- Intercept a request to `http://localhost/hackable/uploads/webshell.php`

- Send the intercepted request to Repeater with `Ctrl + R`.

- In Repeater, add the query parameter: `cmd=ls`. You should get familiar-looking output in the response.

- Use Repeater to extract the following information from the server:
  - Read the contents of `/etc/passwd`
  - Run `id` and `whoami`
  - Determine the operating system and kernel version with `uname`
  - List all running processes with `ps aux`
    - **Note**: Recall that you must use a `+` or `%20` to send a space in a URL, e.g.: `ls -sail` becomes `ls+-sail` _or_ `ls%20-sail`.

- As a **bonus**, repeat the above exercise with Burp Intruder instead of Repeater.
